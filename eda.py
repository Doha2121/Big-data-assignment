import sys
import pandas as pd
import os

df = pd.read_csv(sys.argv[1])

insights = [
    f"Dataset shape: {df.shape}",
    f"Column names: {df.columns.tolist()}",
    f"Summary statistics:\n{df.describe()}",
    f"Number of males: {len(df[df['Gender'] == 0])}, Number of females: {len(df[df['Gender'] == 1])}",
    f"Purchased Distribution: \n{df['Purchased'].value_counts()}"
]

for i, insight in enumerate(insights):
    with open(f"/home/doc-bd-a1/eda-in-{i+1}.txt", "w") as f:
        f.write(insight)

os.system("python3 vis.py /home/doc-bd-a1/res_dpre.csv")
