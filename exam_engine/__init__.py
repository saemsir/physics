"""Evidence-aware exam-topic recommendations for original physics lessons."""

from .engine import (
    BacktestResult,
    ExamRecord,
    Recommendation,
    ForecastResult,
    forecast_test,
    load_backtest,
    load_recommendations,
    load_topics,
    render_test_forecast,
    render_video_batch,
)

__all__ = [
    "BacktestResult",
    "ExamRecord",
    "Recommendation",
    "ForecastResult",
    "forecast_test",
    "load_backtest",
    "load_recommendations",
    "load_topics",
    "render_test_forecast",
    "render_video_batch",
]
