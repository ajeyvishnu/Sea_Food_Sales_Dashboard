#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:30:33 2024

@author: ajayvishnu
"""

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# Define the lists of values for different columns
products = ['Shrimp', 'Salmon', 'Tuna', 'Crab', 'Lobster', 'Oyster', 'Squid', 'Octopus', 'Mussels', 'Cod']
warehouses = ['New York', 'Florida', 'California', 'Texas', 'Chicago']
shipping_companies = [fake.company() for _ in range(5)]
customers = ['Costco', 'Walmart', 'Sam\'s Club', 'Target', 'Amazon', 'Kroger', 'Walgreens', 'Best Buy', 'Home Depot', 'Lowe\'s']
cities = ['New York City, New York', 'Los Angeles, California', 'Chicago, Illinois', 'Houston, Texas',
          'Philadelphia, Pennsylvania', 'Phoenix, Arizona', 'San Antonio, Texas', 'San Diego, California',
          'Dallas, Texas', 'San Francisco, California', 'Austin, Texas', 'Boston, Massachusetts',
          'Seattle, Washington', 'Denver, Colorado', 'Miami, Florida']


start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate fake data
data = {
    'Product': [random.choice(products) for _ in range(40000)],
    'Order ID': np.random.randint(10000, 99999, size=40000),
    'Item Processing cost': np.random.uniform(1,5, size=40000),
    'Weight': np.random.uniform(100, 1000, size=40000),
    'Revenue': np.random.uniform(1000, 10000, size=40000),
    'Profit': np.random.uniform(100, 1000, size=40000),
    'Warehouse': [random.choice(warehouses) for _ in range(40000)],
    'Inventory': np.random.uniform(100, 1000, size=40000),
    'Customer': [random.choice(customers) for _ in range(40000)],
    'City': [random.choice(cities) for _ in range(40000)],
    'Shipping Company': [random.choice(shipping_companies) for _ in range(40000)],
    'Order Date': [fake.date_time_between(start_date=start_date, end_date=end_date) for _ in range(40000)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Additional KPIs
df['Cost per unit'] = df['Item Processing cost'] / df['Weight']
df['Profit margin'] = (df['Profit'] / df['Revenue']) * 100
df['Average order size'] = df.groupby('Order ID')['Weight'].transform('sum')
df['Inventory turnover'] = df['Weight'] / df['Inventory']

# Save DataFrame to CSV
df.to_csv('/Users/ajayvishnu/Downloads/seafood_data_with_kpis.csv', index=False)
