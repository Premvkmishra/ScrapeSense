import pandas as pd
import matplotlib.pyplot as plt

# Load scraped data
data = pd.read_csv('../output/noon_products.csv')

# Data Cleaning
data.dropna(inplace=True)  # Remove rows with missing values

# 1. Most Expensive Product
most_expensive = data.loc[data['Price'] == data['Price'].max()]
print("Most Expensive Product:")
print(most_expensive)

# 2. Cheapest Product
cheapest = data.loc[data['Price'] == data['Price'].min()]
print("\nCheapest Product:")
print(cheapest)

# 3. Number of Products from Each Brand
brand_counts = data['Brand'].value_counts()
print("\nNumber of Products from Each Brand:")
print(brand_counts)

# 4. Number of Products by Each Seller
seller_counts = data['Seller'].value_counts()
print("\nNumber of Products by Each Seller:")
print(seller_counts)

# Visualization - Brand and Seller distribution
plt.figure(figsize=(10,5))

# Brand distribution bar chart
plt.subplot(1, 2, 1)
brand_counts.plot(kind='bar', color='blue')
plt.title('Products by Brand')
plt.xlabel('Brand')
plt.ylabel('Count')

# Seller distribution bar chart
plt.subplot(1, 2, 2)
seller_counts.plot(kind='bar', color='green')
plt.title('Products by Seller')
plt.xlabel('Seller')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('../assets/analysis_graphs.png')  # Save graph to assets folder
plt.show()
