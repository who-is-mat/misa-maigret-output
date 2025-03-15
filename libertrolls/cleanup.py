import os
import pandas as pd

for file in os.listdir("."):
    if file.endswith(".csv"):
        csv_path = os.path.join(".", file)
        df = pd.read_csv(csv_path)

        if "http_status" in df.columns:
            filtered_df = df[df["http_status"] <= 399]
            filtered_df.to_csv(csv_path, index=False)
            print(f"File overwritten: {csv_path}")
        else:
            print(f"The file {file} does not contain the 'http_status' column")