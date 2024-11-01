import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('../output/noon_products.csv')


data.dropna(inplace=True)  


most_expensive = data.loc[data['Price'] == data['Price'].max()]
print("Most Expensive Product:")
print(most_expensive)

cheapest = data.loc[data['Price'] == data['Price'].min()]
print("\nCheapest Product:")
print(cheapest)

brand_counts = data['Brand'].value_counts()
print("\nNumber of Products from Each Brand:")
print(brand_counts)

seller_counts = data['Seller'].value_counts()
print("\nNumber of Products by Each Seller:")
print(seller_counts)

plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
brand_counts.plot(kind='bar', color='blue')
plt.title('Products by Brand')
plt.xlabel('Brand')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
seller_counts.plot(kind='bar', color='green')
plt.title('Products by Seller')
plt.xlabel('Seller')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('../assets/analysis_graphs.png')  
plt.show()
