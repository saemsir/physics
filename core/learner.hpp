// learner.hpp - online self-improving forecaster for the Saem exam engine.
// State persists as JSON (json.hpp); every persisted double prints in the
// shortest round-trip, JavaScript-compatible form (numfmt.hpp), so the C++
// core, the Python engine and any JS dashboard read identical numbers.
#pragma once
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include "json.hpp"
#include "numfmt.hpp"

namespace saem {

inline double brier_loss(const std::vector<double>& p, const std::vector<double>& o) {
  double s = 0;
  for (size_t t = 0; t < p.size(); ++t) { double d = p[t] - o[t]; s += d * d; }
  return s;
}

inline double clampd(double v, double lo, double hi) { return v < lo ? lo : (v > hi ? hi : v); }

struct Paper { int year = 0; std::vector<double> share; };  // normalized topic mix

struct LearnerState {
  // ---- learnable parameters ----
  double half_life  = 8.0;   // recency half-life in years (lambda)
  double prior_mass = 1.0;   // per-topic Dirichlet prior mass (alpha)
  double eta        = 0.15;  // EG learning rate
  std::vector<std::string> topics;
  std::vector<double> weights;  // relative prior direction, mean 1

  // ---- optimizer memory ----
  int    step = 0, tune_phase = 0, dir_hl = -1, dir_pm = -1;
  double half_life_step = 1.0, prior_mass_step = 0.25;
  double prev_loss = -1.0, loss_ema = -1.0;
  bool   freeze_scalars = false;
  Json   history = Json::array();

  void renorm_weights() {
    if (weights.empty()) return;
    double mean = 0; for (double w : weights) mean += w;
    mean /= static_cast<double>(weights.size());
    if (mean <= 0) { weights.assign(weights.size(), 1.0); return; }
    for (double& w : weights) w /= mean;
  }
  void clamp_all() {
    half_life  = clampd(half_life, 2.0, 30.0);
    prior_mass = clampd(prior_mass, 0.25, 4.0);
    eta        = clampd(eta, 0.02, 0.5);
    for (double& w : weights) w = clampd(w, 0.2, 5.0);
    renorm_weights();
  }

  // ---- model: p = (alpha + m) / (alpha0 + W), m reweighted by current lambda ----
  std::vector<double> predict(const std::vector<Paper>& papers, int as_of) const {
    const size_t K = topics.size();
    std::vector<double> m(K, 0.0); double W = 0;
    const double k = std::log(2.0) / half_life;
    for (const Paper& p : papers) {
      const double w = std::exp(-k * static_cast<double>(as_of - p.year));
      W += w;
      for (size_t t = 0; t < K && t < p.share.size(); ++t) m[t] += w * p.share[t];
    }
    double a0 = 0; for (double w : weights) a0 += prior_mass * w;
    const double denom = a0 + W;
    std::vector<double> out(K, 0.0);
    if (denom > 0)
      for (size_t t = 0; t < K; ++t) out[t] = (prior_mass * weights[t] + m[t]) / denom;
    return out;
  }

  // ---- one online learning step: predict -> measure -> update -> remember ----
  double learn_step(const std::vector<Paper>& papers, int as_of,
                    const std::vector<double>& observed) {
    const std::vector<double> p = predict(papers, as_of);
    const double loss = brier_loss(p, observed);
    const size_t K = topics.size();

    // (1) EG on prior direction: under-predicted topics grow multiplicatively.
    for (size_t t = 0; t < K; ++t)
      weights[t] *= std::exp(-eta * (p[t] - observed[t]));
    renorm_weights();

    // (2) pattern search, one scalar per step: keep good moves, flip+shrink bad.
    if (!freeze_scalars) {
      if (prev_loss >= 0 && loss > prev_loss) {
        if (tune_phase == 0) { dir_hl = -dir_hl; half_life_step  *= 0.5; }
        else                 { dir_pm = -dir_pm; prior_mass_step *= 0.5; }
      }
      if (tune_phase == 0)
        half_life = clampd(half_life + dir_hl * half_life_step, 2.0, 30.0);
      else
        prior_mass = clampd(prior_mass + dir_pm * prior_mass_step, 0.25, 4.0);
      tune_phase ^= 1;
    }

    // (3) memory: EMA, decaying lr, capped human-readable history.
    loss_ema = (loss_ema < 0) ? loss : 0.8 * loss_ema + 0.2 * loss;
    eta = std::max(0.02, eta * 0.995);
    for (double& w : weights) w = clampd(w, 0.2, 5.0);
    ++step;
    prev_loss = loss;

    Json rec = Json::object();
    rec.set("step", step);
    rec.set("year", as_of);
    rec.set("brier", round_sig(loss, 6));
    rec.set("half_life_years", round_sig(half_life, 4));
    rec.set("prior_mass", round_sig(prior_mass, 4));
    rec.set("loss_ema", round_sig(loss_ema, 6));
    history.push(rec);
    if (history.size() > 50) {
      Json tail = Json::array();
      const Json::Arr& a = history.arr();
      for (size_t i = a.size() - 50; i < a.size(); ++i) tail.push(a[i]);
      history = tail;
    }
    return loss;
  }

  // ---- persistence: json.hpp safe accessors make old/partial states safe ----
  Json to_json() const {
    Json o = Json::object();
    o.set("schema_version", 1);
    o.set("engine", std::string("saem-online-learner"));
    o.set("review_status", std::string("draft"));  // teacher gate
    o.set("step", step);
    o.set("half_life_years", half_life);
    o.set("half_life_step", half_life_step);
    o.set("prior_mass", prior_mass);
    o.set("prior_mass_step", prior_mass_step);
    o.set("eta", eta);
    o.set("loss_ema", loss_ema);
    o.set("freeze_scalars", freeze_scalars);
    Json tw = Json::object();
    for (size_t i = 0; i < topics.size(); ++i) tw.set(topics[i], weights[i]);
    o.set("topic_weights", tw);
    o.set("history", history);
    return o;
  }

  static LearnerState from_json(const Json& j, const std::vector<std::string>& catalog) {
    LearnerState s;
    s.topics = catalog;
    s.weights.assign(catalog.size(), 1.0);
    s.step            = j["step"].asInt(0);
    s.half_life       = j["half_life_years"].asNum(8.0);
    s.half_life_step  = j["half_life_step"].asNum(1.0);
    s.prior_mass      = j["prior_mass"].asNum(1.0);
    s.prior_mass_step = j["prior_mass_step"].asNum(0.25);
    s.eta             = j["eta"].asNum(0.15);
    s.loss_ema        = j["loss_ema"].asNum(-1.0);
    s.freeze_scalars  = j["freeze_scalars"].asBool(false);
    const Json& tw = j["topic_weights"];
    if (tw.isObj())
      for (size_t i = 0; i < catalog.size(); ++i)
        s.weights[i] = tw[catalog[i]].asNum(1.0);
    s.clamp_all();
    return s;
  }
};

}  // namespace saem
