from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
def main():
    df=pd.read_csv(Path(__file__).with_name("tickets.csv"))
    print("Ticket count:",len(df))
    print("\nTickets by category:\n",df["category"].value_counts())
    print("\nMean resolution hours by priority:\n",df.groupby("priority")["resolution_hours"].mean().round(2))
    print("\nStatus distribution:\n",df["status"].value_counts(normalize=True).mul(100).round(1).astype(str)+"%")
    df.groupby("category")["resolution_hours"].median().sort_values().plot(kind="bar",title="Median Resolution Time by Category",ylabel="Hours")
    plt.tight_layout(); plt.savefig(Path(__file__).with_name("resolution_by_category.png"),dpi=150)
if __name__ == "__main__": main()
