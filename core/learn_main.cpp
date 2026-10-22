// learn_main.cpp - replay rolling-origin backtest steps through the learner
// and persist the improved state.
//   usage: learn steps.json [state_in.json] state_out.json
#include <cstdio>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "learner.hpp"

using namespace saem;

static std::string slurp(const char* path) {
  std::ifstream f(path, std::ios::binary);
  std::ostringstream ss; ss << f.rdbuf();
  return ss.str();
}

static std::vector<double> vec_from_obj(const Json& o, const std::vector<std::string>& topics) {
  std::vector<double> v(topics.size(), 0.0);
  for (size_t i = 0; i < topics.size(); ++i) v[i] = o[topics[i]].asNum(0.0);
  return v;
}

static std::vector<Paper> papers_from_json(const Json& arr, const std::vector<std::string>& topics) {
  std::vector<Paper> ps;
  if (!arr.isArr()) return ps;
  for (size_t i = 0; i < arr.size(); ++i) {
    Paper p;
    p.year = arr[i]["year"].asInt(0);
    p.share = vec_from_obj(arr[i]["share"], topics);
    ps.push_back(std::move(p));
  }
  return ps;
}

int main(int argc, char** argv) {
  if (argc < 3) { std::fprintf(stderr, "usage: learn steps.json [state_in.json] state_out.json\n"); return 2; }
  const char* state_in  = argc > 3 ? argv[2] : nullptr;
  const char* state_out = argc > 3 ? argv[3] : argv[2];

  Json steps = Json::parse(slurp(argv[1]));  // your json.hpp parse entry point
  if (!steps.isArr()) { std::fprintf(stderr, "steps.json must be a JSON array\n"); return 2; }

  // Catalog = union of topic keys, first-seen (insertion) order.
  std::vector<std::string> topics;
  auto add_keys = [&](const Json& o) {
    if (!o.isObj()) return;
    for (const auto& kv : o.obj())
      if (std::find(topics.begin(), topics.end(), kv.first) == topics.end())
        topics.push_back(kv.first);
  };
  for (size_t i = 0; i < steps.size(); ++i) {
    const Json& pa = steps[i]["papers"];
    if (pa.isArr()) for (size_t k = 0; k < pa.size(); ++k) add_keys(pa[k]["share"]);
    add_keys(steps[i]["observed"]);
  }

  LearnerState state;
  if (state_in) state = LearnerState::from_json(Json::parse(slurp(state_in)), topics);
  else { state.topics = topics; state.weights.assign(topics.size(), 1.0); }

  double first_sum = 0, last_sum = 0; size_t first_n = 0, last_n = 0;
  const size_t n = steps.size(), half = std::min<size_t>(5, n / 2 > 0 ? n / 2 : 1);
  for (size_t i = 0; i < n; ++i) {
    const Json& e = steps[i];
    const std::vector<Paper> papers = papers_from_json(e["papers"], topics);
    const std::vector<double> obs   = vec_from_obj(e["observed"], topics);
    const int year = e["year"].asInt(0);
    const double loss = state.learn_step(papers, year, obs);
    if (i < half) { first_sum += loss; ++first_n; }
    if (i + half >= n) { last_sum += loss; ++last_n; }
    std::printf("step %d year %d brier %s hl %s alpha %s\n",
                state.step, year,
                jsnum(round_sig(loss, 6)).c_str(),
                jsnum(round_sig(state.half_life, 4)).c_str(),
                jsnum(round_sig(state.prior_mass, 4)).c_str());
  }

  std::ofstream out(state_out);
  out << state.to_json().dump(2) << "\n";  // json.hpp serializer (match its name)
  if (first_n && last_n)
    std::printf("improvement: early avg %s -> late avg %s\n",
                jsnum(round_sig(first_sum / first_n, 6)).c_str(),
                jsnum(round_sig(last_sum / last_n, 6)).c_str());
  std::printf("state written to %s\n", state_out);
  return 0;
}
