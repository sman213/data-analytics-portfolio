# NBA Performance Modeling

**Course foundation:** MAT 243 Project Three.

## Question

How well do scoring and relative team strength explain total regular-season wins? I compared three regression models using historical team-season data from 1995 through 2015.

## Results from the original saved notebook

| Model | Predictors | R-squared |
| --- | --- | --- |
| 1 | Average Elo | 0.823 |
| 2 | Average points and average Elo | 0.837 |
| 3 | Above, plus point differential and Elo differential | 0.878 |

These values were verified against the saved Jupyter HTML output and the submitted summary report. The third model explained 87.8% of variation **within the analyzed sample**. This is not an 87.8% prediction accuracy claim or evidence of performance on unseen seasons.

I also used scatterplots, Pearson correlations, F-tests, and coefficient significance tests. In the full model, average Elo was no longer individually significant at the 1% level, illustrating that related predictors can overlap in what they explain.

## Run the portfolio adaptation

```sh
python nba-performance/analyze.py "path/to/nba_wins_data.csv"
```

`analyze.py` reproduces the three formulas with a compact interface and saves model summaries, comparison metrics, and a scatterplot figure. The course CSV was not present in the supplied folder, so it is not bundled. The new script was smoke-tested with synthetic data; original metrics above come from the saved course outputs, not a new execution on the original data.

## Interpretation

The work demonstrates model comparison and communication of statistical findings. It does not prove causation or forecast future seasons. A stronger forecasting study would use temporal validation, evaluate residuals and collinearity, and compare errors on held-out seasons.

The project follows a course-provided analytical structure. This portfolio script was reimplemented with AI assistance; the course template and full notebook are not redistributed.
