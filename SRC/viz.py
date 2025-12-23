import matplotlib.pyplot as plt

def plot_monthly_trend(df):
    """
    Plot monthly total housing complaints.
    """
    trend = df.groupby("year_month")["count"].sum()

    plt.figure(figsize=(10, 5))
    trend.plot()
    plt.title("Monthly Housing Complaints (NYC 311)")
    plt.xlabel("Month")
    plt.ylabel("Number of Complaints")
    plt.tight_layout()
    plt.show()
