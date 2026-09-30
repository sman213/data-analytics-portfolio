# Health Survey Data Preparation

**Course foundation:** DAT 223, gathering data assignment, June 2026.

## Question

Prepare health coverage, smoking, and asthma variables for later analysis. This project prepares the data; it does not establish a relationship between these factors.

## Original work

I used the LLCP 2017 codebook to select four variables, imported the course CSV into pandas, created a focused DataFrame, and checked the selected columns and sample records.

| Variable | Meaning | Usable response codes |
| --- | --- | --- |
| HLTHPLN1 | Health coverage | 1 yes, 2 no |
| ASTHMA3 | Ever told had asthma | 1 yes, 2 no |
| SMOKE100 | Smoked at least 100 cigarettes | 1 yes, 2 no |
| SMOKDAY2 | Current smoking frequency | 1 every day, 2 some days, 3 not at all |

## Portfolio extension

`prepare.py` adds explicit response-code checks and a missing/nonresponse summary. It preserves valid categories and maps other values to missing rather than treating refusal, unknown responses, or skipped questions as real measurements. These additions were developed for this portfolio, not claimed as part of the original submission.

```sh
python health-survey/prepare.py "path/to/LLCP2017 Dataset.csv"
```

Outputs are a four-column local CSV and a JSON quality summary. Raw and prepared individual survey records are excluded from this repository.

## Limits

The local course extract is not assumed to represent the full BRFSS population. SMOKDAY2 has skip patterns, so missing values should not automatically be treated as errors. The script does not apply survey weights or perform significance tests. Confirm the codebook for any replacement input before use.

[CDC 2017 BRFSS documentation](https://www.cdc.gov/brfss/annual_data/annual_2017.html) provides the original survey context. See `validation.json` for aggregate checks from the local course extract.
