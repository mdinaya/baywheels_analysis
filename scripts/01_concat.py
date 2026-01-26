import pandas as pd
import glob
import os

path = "../data"
all_files = glob.glob(os.path.join(path, "*csv"))

df_list = []

for filename in all_files:
    print(f"Loading: {filename}...")
    df = pd.read_csv(filename)
    df_list.append(df)

master_df = pd.concat(df_list, axis=0, ignore_index=True)
print(f"Succesfully merged! Total rows: {len(master_df)}")

output_dir = os.path.join("..", "data", "processed")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, "merged_baywheels_df.csv")
master_df.to_csv(output_path, index=False)

print(f"File saved to {output_path}")
