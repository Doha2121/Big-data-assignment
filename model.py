import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv(sys.argv[1])


df_numeric = df.drop(columns=["User ID"], errors="ignore").select_dtypes(include=['number'])

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(df_scaled)

cluster_counts = df["cluster"].value_counts().sort_index()

with open("k.txt", "w") as f:
    for cluster, count in cluster_counts.items():
        f.write(f"Cluster {cluster}: {count} records\n")

print("Clustering completed. Results saved in k.txt.")
