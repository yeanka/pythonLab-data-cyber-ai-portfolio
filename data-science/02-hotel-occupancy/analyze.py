from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
def main():
    path = Path(__file__).with_name("hotel_monthly.csv")
    df = pd.read_csv(path)
    df["occupancy_rate_pct"] = (df["avg_occupied_rooms_per_day"] / df["available_rooms_per_day"] * 100).round(1)
    df["estimated_daily_room_revenue_ngn"] = df["avg_occupied_rooms_per_day"] * df["average_room_rate_ngn"]
    print(df.to_string(index=False))
    print("\nMean occupancy rate:", round(df["occupancy_rate_pct"].mean(), 1), "%")
    ax = df.plot(x="month", y="occupancy_rate_pct", marker="o", legend=False, title="Illustrative Monthly Occupancy")
    ax.set_ylabel("Occupancy (%)"); plt.xticks(rotation=45); plt.tight_layout()
    plt.savefig(Path(__file__).with_name("occupancy_trend.png"), dpi=150)
if __name__ == "__main__": main()
