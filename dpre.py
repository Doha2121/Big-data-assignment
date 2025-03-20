import sys
import pandas as pd
import numpy as np
import os
import subprocess

df = pd.read_csv(sys.argv[1])

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

df.drop(columns=["User ID"], errors="ignore", inplace=True)

try:
    df["Salary_Category"] = pd.qcut(df["EstimatedSalary"], q=3, labels=["Low", "Medium", "High"], duplicates="drop")
except ValueError:
    df["Salary_Category"] = "Medium"  

output_file = "/home/doc-bd-a1/res_dpre.csv"
df.to_csv(output_file, index=False)

print(f" Data preprocessing complete. Saved as {output_file}")

try:
    subprocess.run(["python3", "eda.py", output_file], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running eda.py: {e}")
