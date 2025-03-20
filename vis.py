import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv(sys.argv[1])

# Ensure required columns exist
required_columns = {"Age", "EstimatedSalary", "Purchased"}
if not required_columns.issubset(df.columns):
    print(f"Error: Missing required columns. Found: {df.columns.tolist()}")
    sys.exit(1)

# Convert necessary columns to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["EstimatedSalary"] = pd.to_numeric(df["EstimatedSalary"], errors="coerce")

# Drop any remaining NaN values
df.dropna(subset=["Age", "EstimatedSalary"], inplace=True)

# Ensure the output directory exists
output_dir = "/home/doc-bd-a1/service-results"
os.makedirs(output_dir, exist_ok=True)  # ✅ Creates directory if missing

# Plot visuals
plt.figure(figsize=(12, 6))

# Histogram for Age Distribution
plt.subplot(1, 2, 1)
sns.histplot(df["Age"], bins=10, kde=True, color="blue")
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Scatterplot for Age vs Estimated Salary
plt.subplot(1, 2, 2)
sns.scatterplot(x=df["Age"], y=df["EstimatedSalary"], hue=df["Purchased"], palette="coolwarm")
plt.title("Age vs Estimated Salary (Purchased Highlighted)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
