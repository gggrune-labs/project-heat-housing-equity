import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

def monthly_counts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate complaints by month, borough, and complaint type.
    """
    out = (
        df.groupby(["year_month", "borough", "complaint_type"])
        .size()
        .reset_index(name="count")
    )

    out["month_index"] = range(len(out))
    return out

def regression(df: pd.DataFrame):
    """
    OLS regression:
    count ~ time + borough + complaint type
    """
    model = smf.ols(
        "count ~ month_index + C(borough) + C(complaint_type)",
        data=df
    ).fit()
    return model

def anova(df: pd.DataFrame):
    """
    ANOVA: test mean differences in complaint volume by borough.
    """
    model = smf.ols("count ~ C(borough)", data=df).fit()
    return sm.stats.anova_lm(model, typ=2)

def ancova(df: pd.DataFrame):
    """
    ANCOVA: borough differences controlling for time.
    """
    model = smf.ols("count ~ month_index + C(borough)", data=df).fit()
    return sm.stats.anova_lm(model, typ=2)
