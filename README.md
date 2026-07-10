# 🛒 SmartCart — AI-Powered Product Recommendation System

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![ML](https://img.shields.io/badge/ML-K--Means%20%7C%20Agglomerative-blueviolet)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

> A real-world Product Recommendation Web Application powered by **Machine Learning Customer Segmentation**. Built with Python (Scikit-Learn) for analysis and pure HTML/CSS/JavaScript for a premium, code-free frontend.

🔗 **Live Demo:** [https://rahultwoapl8130.github.io/Smartcart_Customers/](https://rahultwoapl8130.github.io/Smartcart_Customers/)

---

## 🚀 Features

- **AI-Powered Clustering** — Uses K-Means & Agglomerative Clustering to segment 2,200+ customers into 4 distinct groups.
- **Personalized Recommendations** — Enter your profile and instantly get product recommendations tailored to your cluster.
- **Premium UI** — Glassmorphism design, animated gradients, responsive layout, and smooth micro-animations.
- **No Code Visible** — The end-user sees only a beautiful, interactive interface — no Python, no Jupyter.
- **100% Free Hosting** — Deployed on GitHub Pages with zero server costs.

---

## 🧠 How It Works

### Phase 1: Machine Learning (Python)

1. **Data Cleaning** — Handled missing values, removed outliers.
2. **Feature Engineering** — Created `Age`, `Customer_Tenure_Days`, `Total_Spending`, `Total_Children`, simplified `Education` and `Living_With`.
3. **Encoding & Scaling** — One-Hot Encoding for categorical features, StandardScaler for normalization.
4. **PCA** — Reduced dimensionality to 3 principal components for visualization.
5. **Clustering** — Applied both K-Means and Agglomerative Clustering (k=4, determined via Elbow Method + Silhouette Score).

### Phase 2: Frontend (HTML/CSS/JS)

The ML cluster boundaries are translated into simple JavaScript rules, so the app runs **100% client-side** with zero backend dependencies.

---

## 📊 Customer Segments (4 Clusters)

| Cluster | Name | Profile | Recommendations |
|---------|------|---------|-----------------|
| **0** | 🛒 Balanced Shopper | Average income, moderate spending | Fresh Meat, Table Wine, Fish, Essentials |
| **1** | 👑 Premium VIP | High income, high spending | Vintage Champagne, Gold Membership, Gourmet Seafood |
| **2** | 💰 Smart Saver | Low income, budget-conscious | Mega Deals, Seasonal Fruits, Sweet Treats, Coupons |
| **3** | 🔥 Trendsetter | Moderate income, high spending | Trending Wines, Gift Boxes, Imported Chocolates |

---

## 📁 Project Structure

```
smartcart_customers/
├── index.html                 # Frontend Web Application (single file)
├── smartcart_customers.py     # Python ML Script (data analysis & clustering)
├── smartcart_customers.csv    # Dataset (2,240 customers × 22 features)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Data Science** | Python, Pandas, NumPy, Matplotlib, Seaborn |
| **Machine Learning** | Scikit-Learn (KMeans, AgglomerativeClustering, PCA, StandardScaler) |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Vanilla JavaScript |
| **Fonts** | Google Fonts (Inter) |
| **Hosting** | GitHub Pages (Free) |

---

## ⚙️ Run Locally

### Python Analysis
```bash
pip install -r requirements.txt
python smartcart_customers.py
```

### Frontend
Simply open `index.html` in any browser — no server needed!

---

## 🌐 Deploy on GitHub Pages

1. Push your code to a GitHub repository.
2. Go to **Settings → Pages**.
3. Under **Branch**, select `main` and `/ (root)`.
4. Click **Save** — your site will be live in ~1 minute!

---

## 📊 Dataset

- **Source:** SmartCart E-Commerce Customer Data
- **Records:** 2,240 customers
- **Features:** 22 columns including demographics, spending categories, purchase channels, and campaign responses.

---

## 👨‍💻 Author

**Rahul** — [GitHub Profile](https://github.com/rahultwoapl8130)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
