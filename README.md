# Project H.E.A.T. (Housing Equity Analysis & Transformation)

Project H.E.A.T. analyzes **NYC 311 housing-related complaints (2021–2023)** to identify patterns of housing distress and test whether complaint volumes differ across **time, location, and complaint type**. Using **regression, ANOVA/ANCOVA**, and a **baseline predictive model**, the project demonstrates how analytics can support **proactive, equity-focused service allocation**.

---

## What this repo contains

- **Statistical analysis**
  - Regression to quantify relationships between time trends and complaint volumes
  - ANOVA to test group differences (e.g., borough, complaint type)
  - ANCOVA to test group differences while controlling for time/covariates

- **Predictive baseline**
  - A simple model to estimate near-term housing distress risk (decision support only)

- **Reproducible structure**
  - `src/` reusable cleaning + feature engineering
  - `scripts/` one-command analysis + training
  - `docs/` data dictionary, methodology, and limitations
  - `reports/figures/` exported visuals for easy review

---

## Repo structure

```text
project-heat/
├─ data/
│  └─ sample/
├─ docs/
├─ reports/
│  └─ figures/
├─ results/
├─ scripts/
└─ src/
