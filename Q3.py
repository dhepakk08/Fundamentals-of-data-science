import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Product_ID': ['PR01', 'PR02', 'PR03', 'PR04', 'PR05',
                   'PR06', 'PR07', 'PR08', 'PR09', 'PR10',
                   'PR11', 'PR12', 'PR13', 'PR14', 'PR15',
                   'PR16', 'PR17', 'PR18', 'PR19', 'PR20'],

    'Category': ['Grocery', 'Snacks', 'Dairy', 'Fruits', 'Vegetables',
                 'Grocery', 'Snacks', 'Dairy', 'Fruits', 'Vegetables',
                 'Grocery', 'Snacks', 'Dairy', 'Fruits', 'Vegetables',
                 'Grocery', 'Snacks', 'Dairy', 'Fruits', 'Vegetables'],

    'Price': [50, 30, 45, 60, 40, 80, 25, 55, 70, 35,
              90, 20, 65, 75, 45, 100, 35, 50, 80, 30],

    'Quantity_Sold': [20, 35, 18, 25, 30, 15, 40, 16, 22, 28,
                      12, 45, 14, 20, 26, 10, 32, 19, 18, 35],

    'Discount': [5, 3, 2, 5, 4, 6, 3, 2, 5, 4,
                 6, 2, 3, 5, 4, 7, 3, 2, 6, 3],

    'Revenue': [1000, 1050, 810, 1500, 1200, 1200, 1000, 880, 1540, 980,
                1080, 900, 910, 1500, 1170, 1000, 1120, 950, 1440, 1050]
}

df = pd.DataFrame(data)

# Step 2: Display and inspect the dataset
print("First Five Rows:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Calculate overall averages
print("\nOverall Averages:")
print(df[['Price', 'Quantity_Sold', 'Discount', 'Revenue']].mean())

# Step 4: Analyze category-wise sales
print("\nCategory-wise Sales:")
category_sales = df.groupby('Category')[
    ['Quantity_Sold', 'Revenue']
].sum()

print(category_sales)

# Step 5: Identify high-selling products
print("\nTop 5 Products by Quantity Sold:")
top_quantity = df.nlargest(5, 'Quantity_Sold')
print(top_quantity[['Product_ID', 'Category', 'Quantity_Sold']])

# Step 6: Identify top revenue-generating products
print("\nTop 5 Products by Revenue:")
top_revenue = df.nlargest(5, 'Revenue')
print(top_revenue[['Product_ID', 'Category', 'Revenue']])

# Step 7: Analyze average revenue by category
print("\nAverage Revenue by Category:")
print(df.groupby('Category')['Revenue'].mean())

# Step 8: Visualize category-wise revenue
category_sales['Revenue'].plot(kind='bar')

plt.title('Total Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.show()

# Step 9: Visualize quantity sold by category
category_sales['Quantity_Sold'].plot(kind='bar')

plt.title('Total Quantity Sold by Category')
plt.xlabel('Category')
plt.ylabel('Quantity Sold')
plt.show()

# Step 10: Visualize top revenue-generating products
top_revenue.plot(x='Product_ID', y='Revenue', kind='bar', legend=False)

plt.title('Top 5 Products by Revenue')
plt.xlabel('Product ID')
plt.ylabel('Revenue')
plt.show()

# Step 11: Analyze the relationship between discount and revenue
print("\nCorrelation between Discount and Revenue:")
print(df['Discount'].corr(df['Revenue']))

