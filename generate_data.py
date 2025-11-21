import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Generate fake e-commerce data for 6 months
num_records = 5000
start_date = datetime(2024, 1, 1)
data = []

for i in range(num_records):
    order_id = i + 1
    order_date = start_date + timedelta(days=random.randint(0, 180))
    customer_id = random.randint(1, 1000)
    product_id = random.randint(1, 50)
    quantity = random.randint(1, 5)
    price = round(random.uniform(10, 500), 2)
    data.append([order_id, order_date, customer_id, product_id, quantity, price])

df = pd.DataFrame(data, columns=["order_id", "order_date", "customer_id", "product_id", "quantity", "price"])
df.to_csv("data/orders.csv", index=False)
print("✅ Generated new large orders.csv file with 5000 records!")
