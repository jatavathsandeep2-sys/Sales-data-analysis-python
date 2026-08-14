"""Generates a realistic synthetic retail sales dataset for the analysis project."""
import numpy as np
import pandas as pd

np.random.seed(42)

n_rows = 5000
categories = {
    "Electronics": (1500, 45000),
    "Clothing": (300, 4000),
    "Home & Kitchen": (200, 8000),
    "Beauty & Personal Care": (150, 2500),
    "Sports & Fitness": (400, 6000),
    "Books": (100, 1200),
    "Grocery": (50, 1500),
}
regions = ["North", "South", "East", "West", "Central"]
payment_modes = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Cash on Delivery"]

dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")

rows = []
order_id = 100000
for _ in range(n_rows):
    order_id += 1
    date = np.random.choice(dates)
    category = np.random.choice(list(categories.keys()), p=[0.22, 0.20, 0.16, 0.14, 0.12, 0.08, 0.08])
    low, high = categories[category]
    # seasonal boost in Oct-Dec (festive/holiday season)
    month = pd.Timestamp(date).month
    seasonal_multiplier = 1.4 if month in (10, 11, 12) else 1.0
    price = np.round(np.random.uniform(low, high) * seasonal_multiplier, 2)
    quantity = np.random.choice([1, 1, 1, 2, 2, 3], p=[0.45, 0.2, 0.15, 0.1, 0.06, 0.04])
    discount_pct = np.random.choice([0, 5, 10, 15, 20, 25], p=[0.35, 0.2, 0.2, 0.12, 0.08, 0.05])
    region = np.random.choice(regions)
    payment = np.random.choice(payment_modes, p=[0.28, 0.18, 0.32, 0.12, 0.10])
    rating = np.clip(np.round(np.random.normal(4.1, 0.7), 1), 1, 5)

    rows.append({
        "order_id": order_id,
        "order_date": pd.Timestamp(date).strftime("%Y-%m-%d"),
        "category": category,
        "unit_price": price,
        "quantity": quantity,
        "discount_pct": discount_pct,
        "region": region,
        "payment_mode": payment,
        "customer_rating": rating,
    })

df = pd.DataFrame(rows)
df["gross_sales"] = (df["unit_price"] * df["quantity"]).round(2)
df["net_sales"] = (df["gross_sales"] * (1 - df["discount_pct"] / 100)).round(2)

# introduce a small amount of realistic messiness for the cleaning step in the notebook
missing_idx = np.random.choice(df.index, size=60, replace=False)
df.loc[missing_idx, "customer_rating"] = np.nan
dup_rows = df.sample(15, random_state=1)
df = pd.concat([df, dup_rows], ignore_index=True)

df.to_csv("data/sales_data.csv", index=False)
print("Saved data/sales_data.csv with", len(df), "rows")
