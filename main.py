import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data = {
    "Date": [
        "2025-09-01","2025-09-01","2025-09-01",
        "2025-09-02","2025-09-02","2025-09-02",
        "2025-09-03","2025-09-03","2025-09-03"
    ],
    "Item": [
        "Pizza","Burger","Pasta",
        "Pizza","Burger","Pasta",
        "Pizza","Burger","Pasta"
    ],
    "Quantity": [
        10, 15, 8,
        12, 10, 6,
        9, 14, 7
    ],
    "Price": [
        250, 120, 200,
        250, 120, 200,
        250, 120, 200
    ]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nData with Total Sales:")
print(df)

total_revenue = df["Total_Sales"].sum()
print("\nTotal Restaurant Revenue: ₹", total_revenue)

item_sales = df.groupby("Item", as_index=False)["Total_Sales"].sum()
print("\nSales by Item:")
print(item_sales)

best_selling_item = item_sales.loc[item_sales["Total_Sales"].idxmax(), "Item"]
print("\nBest Selling Item:", best_selling_item)

plt.figure(figsize=(6,4))
sns.barplot(x="Item", y="Total_Sales", data=item_sales)
plt.title("Total Sales by Item")
plt.xlabel("Food Item")
plt.ylabel("Sales (INR)")
plt.show()

daily_sales = df.groupby("Date", as_index=False)["Total_Sales"].sum()

print("\nDaily Sales:")
print(daily_sales)

plt.figure(figsize=(6,4))
sns.barplot(x="Date", y="Total_Sales", data=daily_sales, color="pink")
plt.title("Daily Restaurant Sales")
plt.xlabel("Date")
plt.ylabel("Sales (INR)")
plt.show()
