"""Portfolio adaptation of DAT 223 health survey preparation. No clinical inference."""
import argparse
import json
from pathlib import Path
import pandas as pd

COLUMNS = ["HLTHPLN1", "ASTHMA3", "SMOKE100", "SMOKDAY2"]
VALID = {"HLTHPLN1": {1, 2}, "ASTHMA3": {1, 2}, "SMOKE100": {1, 2}, "SMOKDAY2": {1, 2, 3}}

def prepare(source, output):
    data = pd.read_csv(source, usecols=COLUMNS)
    clean = pd.DataFrame(index=data.index)
    summary = {"rows": len(data), "variables": {}}
    for name in COLUMNS:
        raw = pd.to_numeric(data[name], errors="coerce")
        usable = raw.isin(VALID[name])
        clean[name] = raw.where(usable).astype("Int64")
        summary["variables"][name] = {
            "valid_responses": int(usable.sum()),
            "missing_or_nonresponse": int((~usable).sum()),
            "valid_codes": sorted(VALID[name]),
        }
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    clean.to_csv(output / "prepared_survey.csv", index=False)
    (output / "quality_summary.json").write_text(json.dumps(summary, indent=2))
    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Local course extract with the four BRFSS variables")
    parser.add_argument("--output", default="results/health-survey")
    args = parser.parse_args()
    print(json.dumps(prepare(args.csv, args.output), indent=2))
