import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

rfm = pd.read_csv("data/rfm_data.csv")

X = rfm[["Recency", "Frequency", "Monetary"]]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(X_scaled)

rfm.to_csv(
    "data/customer_segments.csv",
    index=False
)

print("Segmentation Completed")