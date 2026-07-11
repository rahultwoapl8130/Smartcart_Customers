# -*- coding: utf-8 -*-
"""
SmartCart Customer Segmentation & Product Recommendation System
===============================================================
This script performs end-to-end customer segmentation using
K-Means and Agglomerative Clustering on e-commerce customer data.

Author: Rahul
GitHub: https://github.com/rahultwoapl8130/Smartcart_Customers
"""

# ============================================================
# 1. IMPORTS
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from kneed import KneeLocator

# ============================================================
# 2. LOAD DATA
# ============================================================
df = pd.read_csv('smartcart_customers.csv')

print("Dataset Shape:", df.shape)
print(df.head())

# ============================================================
# 3. DATA PREPROCESSING
# ============================================================

# 3.1 Handle Missing Values
df["Income"] = df["Income"].fillna(df["Income"].median())
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# ============================================================
# 4. FEATURE ENGINEERING
# ============================================================

# 4.1 Age
df["Age"] = 2026 - df["Year_Birth"]

# 4.2 Customer Tenure (days since joining)
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True)
reference_date = df["Dt_Customer"].max()
df["Customer_Tenure_Days"] = (reference_date - df["Dt_Customer"]).dt.days

# 4.3 Total Spending (sum of all product categories)
df["Total_spending"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)

# 4.4 Total Children
df["Total_Children"] = df["Kidhome"] + df["Teenhome"]

# 4.5 Simplify Education levels
df["Education"] = df["Education"].replace({
    "Basic": "Undergraduate",
    "2n Cycle": "Undergraduate",
    "Graduation": "Graduate",
    "Master": "Postgraduate",
    "PhD": "Postgraduate"
})
print("\nEducation Distribution:")
print(df["Education"].value_counts())

# 4.6 Simplify Marital Status → Living_With
df["Living_With"] = df["Marital_Status"].replace({
    "Married": "Partner",
    "Together": "Partner",
    "Single": "Alone",
    "Divorced": "Alone",
    "Widow": "Alone",
    "Absurd": "Alone",
    "YOLO": "Alone"
})
print("\nLiving_With Distribution:")
print(df["Living_With"].value_counts())

# ============================================================
# 5. DROP UNNECESSARY COLUMNS
# ============================================================
cols_to_drop = [
    "ID", "Year_Birth", "Marital_Status", "Kidhome", "Teenhome", "Dt_Customer",
    "MntWines", "MntFruits", "MntMeatProducts",
    "MntFishProducts", "MntSweetProducts", "MntGoldProds"
]
df_cleaned = df.drop(columns=cols_to_drop)
print("\nCleaned Data Shape:", df_cleaned.shape)
print(df_cleaned.columns.tolist())

# ============================================================
# 6. OUTLIER REMOVAL
# ============================================================
print("\nData size with outliers:", len(df_cleaned))
df_cleaned = df_cleaned[(df_cleaned["Age"] < 90)]
df_cleaned = df_cleaned[(df_cleaned["Income"] < 600_000)]
print("Data size without outliers:", len(df_cleaned))

# ============================================================
# 7. EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

# 7.1 Pairplot
cols_eda = ["Income", "Recency", "Age", "Total_spending", "Total_Children"]
sns.pairplot(df_cleaned[cols_eda])
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

# 7.2 Correlation Heatmap
corr = df_cleaned.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, annot_kws={"size": 6}, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# ============================================================
# 8. FEATURE ENCODING
# ============================================================
cat_cols = ["Education", "Living_With"]
ohe = OneHotEncoder()
enc_cols = ohe.fit_transform(df_cleaned[cat_cols])
enc_df = pd.DataFrame(
    enc_cols.toarray(),
    columns=ohe.get_feature_names_out(cat_cols),
    index=df_cleaned.index
)
df_cleaned = df_cleaned.dropna()
df_encoded = pd.concat([df_cleaned.drop(columns=cat_cols), enc_df], axis=1)
print("\nEncoded Data Shape:", df_encoded.shape)

# ============================================================
# 9. FEATURE SCALING
# ============================================================
x = df_encoded
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# ============================================================
# 10. PCA (Dimensionality Reduction)
# ============================================================

# 10.1 - 2D PCA
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(x_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], alpha=0.5)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("2D PCA Visualization")
plt.show()
print("2D PCA Variance Ratio:", pca_2d.explained_variance_ratio_)

# 10.2 - 3D PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(x_scaled)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], alpha=0.5)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.set_title("3D PCA Visualization")
plt.show()
print("3D PCA Variance Ratio:", pca.explained_variance_ratio_)

# ============================================================
# 11. FINDING OPTIMAL K
# ============================================================

# 11.1 Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_pca)
    wcss.append(kmeans.inertia_)

knee = KneeLocator(range(1, 11), wcss, curve="convex", direction="decreasing")
optimal_k = knee.elbow
print(f"\nOptimal K (Elbow Method): {optimal_k}")

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker="o")
plt.axvline(x=optimal_k, color="r", linestyle="--", label=f"Optimal K = {optimal_k}")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
plt.title("Elbow Method")
plt.legend()
plt.show()

# 11.2 Silhouette Score
scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_pca)
    score = silhouette_score(X_pca, labels)
    scores.append(score)

plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), scores, marker="o", color="green")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score vs Number of Clusters")
plt.show()

# 11.3 Combined Plot (Elbow + Silhouette)
k_range = range(2, 11)
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(k_range, wcss[1:], marker="o", color="blue", label="WCSS")
ax1.set_xlabel("Number of Clusters (K)")
ax1.set_ylabel("WCSS", color="blue")
ax1.set_title("Elbow Method + Silhouette Score (Combined)")
ax2 = ax1.twinx()
ax2.plot(k_range, scores[:len(k_range)], marker="x", color="red", linestyle="--", label="Silhouette")
ax2.set_ylabel("Silhouette Score", color="red")
plt.show()

# ============================================================
# 12. CLUSTERING
# ============================================================

# 12.1 K-Means Clustering (K=4)
kmeans = KMeans(n_clusters=4, random_state=42)
labels_kmeans = kmeans.fit_predict(X_pca)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=labels_kmeans, cmap="viridis")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.set_title("K-Means Clustering (K=4)")
plt.show()

# 12.2 Agglomerative Clustering (K=4)
agg_cls = AgglomerativeClustering(n_clusters=4, linkage="ward")
labels_agg = agg_cls.fit_predict(X_pca)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=labels_agg, cmap="viridis")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.set_title("Agglomerative Clustering (K=4)")
plt.show()

# ============================================================
# 13. CLUSTER CHARACTERIZATION
# ============================================================
df_cleaned.drop("labels", axis=1, errors="ignore", inplace=True)
df_cleaned["cluster"] = labels_agg

# 13.1 Cluster Distribution
pal = ["#EF4444", "#3B82F6", "#EAB308", "#22C55E"]
plt.figure(figsize=(8, 5))
sns.countplot(data=df_cleaned, x="cluster", palette=pal, hue="cluster")
plt.title("Customer Distribution Across Clusters")
plt.xlabel("Cluster")
plt.ylabel("Count")
plt.show()

# 13.2 Income vs Spending Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df_cleaned["Total_spending"],
    y=df_cleaned["Income"],
    hue=df_cleaned["cluster"],
    palette=pal
)
plt.title("Income vs Total Spending (by Cluster)")
plt.xlabel("Total Spending")
plt.ylabel("Income")
plt.show()

# 13.3 Cluster Summary Statistics
x["cluster"] = labels_agg
cluster_summary = x.groupby("cluster").mean()
print("\n" + "=" * 60)
print("CLUSTER SUMMARY")
print("=" * 60)
print(cluster_summary)
print("\n✅ Analysis Complete! 4 customer segments identified.")
