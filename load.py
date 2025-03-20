import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python3 load.py <dataset-path>")
    sys.exit(1)

dataset_path = sys.argv[1]

try:
    print(f"Loading dataset from {dataset_path} ...")
    df = pd.read_csv(dataset_path)

    print("Dataset loaded successfully!")
    print(df.head())  # Show first few rows

    output_path = "res_load.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved loaded dataset to {output_path}")

    # Call next script
    import subprocess
    subprocess.run(["python3", "dpre.py", output_path])

except Exception as e:
    print(f"Error: {e}")
