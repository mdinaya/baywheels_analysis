import pandas as pd
import os

df = pd.read_csv("../data/processed/merged_baywheels_df.csv")

df["started_at"] = pd.to_datetime(df["started_at"])
df["ended_at"] = pd.to_datetime(df["ended_at"])

df["start_hour"] = df["started_at"].dt.hour
df["start_day"] = df["started_at"].dt.day_name()
df["start_month"] = df["started_at"].dt.month

df["route_id"] = df["start_station_name"].astype(str) + df["end_station_name"].astype(
    str
)

output_dir = os.path.join("..", "data", "processed")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, "cleaned_baywheels_df.csv")
df.to_csv(output_path, index=False)

print(f"File saved to {output_path}")
