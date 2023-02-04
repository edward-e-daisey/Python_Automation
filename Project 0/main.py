# Name: Edward E. Daisey
# Date: February 2nd, 2023
# Description: This is an example of task automation using Python.

import pandas as pd

# Purpose - Load the inventory file into a Pandas dataframe
df = pd.read_excel('inventory.xlsx')

# Purpose - Calculate number of products per supplier
products_per_supplier = df.groupby('Supplier')['Product Number'].count().to_dict()
print(products_per_supplier)

# Purpose - Calculate total value of inventory per supplier
df['Inventory'] = pd.to_numeric(df['Inventory'], errors='coerce')
df['Inventory'] = df['Inventory'].astype(float)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Price'] = df['Price'].astype(float)
total_value_per_supplier = df.groupby('Supplier')[['Inventory', 'Price']].agg({'Inventory': 'sum', 'Price': 'mean'}).eval('Inventory * Price').round(2).to_dict()
print(total_value_per_supplier)

# IN PROGRESS - Find products with inventory less than 10
# products_under_10_inv = df[df['Inventory'] < 10]['Product Number'].to_dict()
# print(products_under_10_inv)

# Purpose - Calculate the total inventory price
inventory_price = df['Inventory Price'] = df['Inventory'] * df['Price']
print(inventory_price[0]) 
# Note - Change [n] to the desired inventory price you want 
# to determine. E.g., [n] = 0 cooresponds to Product Number 1, [n] = 2
# cooresponds to Product Number 2.

# Purpose - Save the updated file
df.to_excel('inventory_final.xlsx', index=False)
