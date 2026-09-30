"""Reimplementation of the three MAT 243 models for a local course dataset."""
import argparse
import json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

FORMULAS = [
    "total_wins ~ avg_elo_n",
    "total_wins ~ avg_pts + avg_elo_n",
    "total_wins ~ avg_pts + avg_elo_n + avg_pts_differential + avg_elo_differential",
]
REQUIRED = ["total_wins", "avg_elo_n", "avg_pts", "avg_pts_differential", "avg_elo_differential"]

def analyze(source, output):
    data = pd.read_csv(source)
    missing = set(REQUIRED) - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    data = data[REQUIRED].apply(pd.to_numeric, errors="raise")
    if data.isna().any().any():
        raise ValueError("Resolve missing model inputs before analysis.")
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    results = []
    for number, formula in enumerate(FORMULAS, 1):
        model = smf.ols(formula, data=data).fit()
        (output / f"model_{number}.txt").write_text(model.summary().as_text())
        results.append({"model": number, "formula": formula, "rows": int(model.nobs),
                        "r_squared": float(model.rsquared), "adjusted_r_squared": float(model.rsquared_adj)})
    (output / "model_comparison.json").write_text(json.dumps(results, indent=2))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, column, label in zip(axes, ["avg_elo_n", "avg_pts"], ["Average Elo", "Average points"]):
        ax.scatter(data[column], data["total_wins"], alpha=0.6)
        ax.set(xlabel=label, ylabel="Season wins")
    fig.tight_layout()
    fig.savefig(output / "relationships.png", dpi=160)
    plt.close(fig)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Local nba_wins_data.csv from the course")
    parser.add_argument("--output", default="results/nba")
    args = parser.parse_args()
    print(json.dumps(analyze(args.csv, args.output), indent=2))
