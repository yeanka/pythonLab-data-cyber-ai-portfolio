from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path(__file__).with_name("sales.csv")
def main():
    df = pd.read_csv(DATA, parse_dates=["date"])
    df = df.drop_duplicates(subset=["order_id"]).dropna(subset=["quantity", "unit_price"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    print("Rows analyzed:", len(df))
    print("Total revenue:", round(df["revenue"].sum(), 2))
    print("Average order revenue:", round(df["revenue"].mean(), 2))
    print("\nRevenue by category:")
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).round(2))
    print("\nRevenue by region:")
    print(df.groupby("region")["revenue"].sum().sort_values(ascending=False).round(2))
    (df.groupby("category")["revenue"].sum().sort_values(ascending=False)
       .plot(kind="bar", title="Synthetic Revenue by Category", ylabel="Revenue"))
    plt.tight_layout()
    plt.savefig(Path(__file__).with_name("revenue_by_category.png"), dpi=150)
    print("Saved revenue_by_category.png")
if __name__ == "__main__": main()
