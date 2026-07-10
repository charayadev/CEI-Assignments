import pandas as pd
from faker import Faker
import random
import numpy as np
from datetime import datetime, timedelta
import os

# Set seeds for reproducibility
random.seed(42)
Faker.seed(42)
fake = Faker()

# Create output directory
os.makedirs('data/raw', exist_ok=True)

def generate_customers(n=700):
    """Generate customers.csv with realistic data and intentional quality issues."""
    data = []
    customer_types = ['REGULAR', 'PREMIUM', 'VIP']
    weights = [0.7, 0.2, 0.1]
    
    for i in range(1, n + 1):
        customer_id = f"CUST{str(i).zfill(5)}"
        # Mixed casing and occasional extra spaces
        name = fake.name()
        if random.random() < 0.4:
            name = name.upper() if random.random() < 0.5 else name.lower()
        if random.random() < 0.1:
            name = " " + name + " "
        
        email = fake.email()
        # 2% invalid emails
        if random.random() < 0.02:
            email = email.replace("@", "") + ".invalid"
        
        # 2% missing phones
        phone = fake.phone_number() if random.random() > 0.02 else None
        
        gender = random.choice(['Male', 'Female', 'Other'])
        city = fake.city()
        state = fake.state()
        country = fake.country()
        
        registration_date = fake.date_between_dates(
            date_start=datetime(2021, 1, 1), 
            date_end=datetime(2025, 6, 30)
        ).strftime('%Y-%m-%d')
        
        customer_type = random.choices(customer_types, weights=weights)[0]
        
        data.append({
            'customer_id': customer_id,
            'customer_name': name,
            'email': email,
            'phone': phone,
            'gender': gender,
            'city': city,
            'state': state,
            'country': country,
            'registration_date': registration_date,
            'customer_type': customer_type
        })
    
    df = pd.DataFrame(data)
    # Additional issues: leading/trailing spaces in some columns
    df['city'] = df['city'].apply(lambda x: " " + x if random.random() < 0.05 else x)
    return df

def generate_products(n=300):
    """Generate products.csv with realistic categories and intentional issues."""
    categories = {
        'Electronics': ['Smartphones', 'Laptops', 'Headphones', 'Tablets', 'Cameras'],
        'Fashion': ['Clothing', 'Footwear', 'Accessories', 'Watches', 'Jewelry'],
        'Home': ['Kitchenware', 'Furniture', 'Decor', 'Lighting', 'Bedding'],
        'Books': ['Fiction', 'Non-Fiction', 'Academic', 'Children', 'Comics'],
        'Sports': ['Fitness', 'Outdoor', 'Team Sports', 'Cycling', 'Water Sports'],
        'Beauty': ['Skincare', 'Makeup', 'Haircare', 'Fragrance', 'Personal Care'],
        'Furniture': ['Living Room', 'Bedroom', 'Dining', 'Office', 'Outdoor']
    }
    
    brands = ['Apple', 'Samsung', 'Nike', 'Sony', 'Adidas', 'IKEA', 'Amazon Basics', 
              'Puma', 'Lenovo', 'Philips', 'Dove', 'Loreal', 'Penguin', 'HarperCollins']
    
    data = []
    for i in range(1, n + 1):
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category])
        
        product_id = f"PROD{str(i).zfill(5)}"
        # Mixed case and extra spaces in names
        base_name = f"{fake.word().capitalize()} {subcategory}"
        if random.random() < 0.3:
            product_name = base_name.upper()
        elif random.random() < 0.3:
            product_name = " " + base_name + " "
        else:
            product_name = base_name
        
        brand = random.choice(brands)
        
        # Price logic based on category
        if category == 'Electronics':
            cost_price = round(random.uniform(5000, 80000), 2)
        elif category in ['Furniture', 'Home']:
            cost_price = round(random.uniform(2000, 45000), 2)
        elif category == 'Books':
            cost_price = round(random.uniform(100, 1500), 2)
        else:
            cost_price = round(random.uniform(300, 8000), 2)
        
        # Markup
        markup = random.uniform(1.3, 2.8)
        selling_price = round(cost_price * markup, 2)
        
        stock_quantity = random.randint(0, 500)
        
        data.append({
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'subcategory': subcategory,
            'brand': brand,
            'cost_price': cost_price,
            'selling_price': selling_price,
            'stock_quantity': stock_quantity
        })
    
    df = pd.DataFrame(data)
    # Introduce duplicate products (rare)
    if len(df) > 5:
        dup_idx = random.sample(range(len(df)), 3)
        for idx in dup_idx:
            df.loc[len(df)] = df.iloc[idx].copy()
            df.loc[len(df)-1, 'product_id'] = f"PROD_DUP_{random.randint(100,999)}"
    
    return df

def generate_orders(customers_df, n=5000):
    """Generate orders.csv with realistic dates and quality issues."""
    data = []
    payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Net Banking', 'Cash on Delivery']
    statuses = ['PLACED', 'SHIPPED', 'DELIVERED', 'CANCELLED', 'RETURNED']
    status_weights = [0.05, 0.05, 0.70, 0.08, 0.12]  # Approx realistic distribution
    
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2025, 12, 31)
    
    customer_ids = customers_df['customer_id'].tolist()
    
    for i in range(1, n + 1):
        order_id = f"ORD{str(i).zfill(6)}"
        customer_id = random.choice(customer_ids)
        
        # Most dates realistic, few future, few malformed
        if random.random() < 0.97:
            order_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
            date_str = order_date.strftime('%Y-%m-%d')
        else:
            # Malformed or future
            if random.random() < 0.6:
                date_str = order_date.strftime('%d/%m/%Y')  # wrong format
            else:
                future_date = end_date + timedelta(days=random.randint(10, 180))
                date_str = future_date.strftime('%Y-%m-%d')
        
        payment_method = random.choice(payment_methods)
        status = random.choices(statuses, weights=status_weights)[0]
        
        shipping_city = fake.city()
        shipping_state = fake.state()
        shipping_country = fake.country()
        region_code = f"R{random.randint(1, 20):02d}"
        
        data.append({
            'order_id': order_id,
            'customer_id': customer_id,
            'order_date': date_str,
            'payment_method': payment_method,
            'status': status,
            'shipping_city': shipping_city,
            'shipping_state': shipping_state,
            'shipping_country': shipping_country,
            'region_code': region_code
        })
    
    df = pd.DataFrame(data)
    
    # Introduce 5% NULL customer_id
    null_count = int(len(df) * 0.05)
    null_indices = random.sample(range(len(df)), null_count)
    for idx in null_indices:
        df.at[idx, 'customer_id'] = None
    
    # Duplicate some orders
    dup_count = int(len(df) * 0.015)
    for _ in range(dup_count):
        dup_row = df.sample(1).iloc[0].copy()
        dup_row['order_id'] = f"DUP_{dup_row['order_id']}"
        df = pd.concat([df, pd.DataFrame([dup_row])], ignore_index=True)
    
    return df

def generate_order_items(orders_df, products_df, n=12000):
    """Generate order_items.csv with relationships and quality issues."""
    data = []
    order_ids = orders_df['order_id'].tolist()
    product_ids = products_df['product_id'].tolist()
    
    # Create multiple items per order on average
    current_order_idx = 0
    while len(data) < n:
        order_id = order_ids[current_order_idx % len(order_ids)]
        num_items = random.randint(1, 6)  # realistic items per order
        
        for _ in range(num_items):
            if len(data) >= n:
                break
                
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 5)
            
            # Quality issues
            if random.random() < 0.03:
                quantity = -quantity  # negative qty
            elif random.random() < 0.02:
                quantity = 0
            
            # Get selling price from products
            prod_row = products_df[products_df['product_id'] == product_id]
            if not prod_row.empty:
                unit_price = float(prod_row.iloc[0]['selling_price'])
            else:
                unit_price = round(random.uniform(100, 5000), 2)
            
            # Discounts realistic (higher for fashion)
            discount_percent = round(random.uniform(0, 35), 2)
            if random.random() < 0.02:  # rare invalid discount
                discount_percent = round(random.uniform(110, 150), 2)
            
            item_id = f"ITEM{str(len(data)+1).zfill(7)}"
            
            data.append({
                'item_id': item_id,
                'order_id': order_id,
                'product_id': product_id,
                'quantity': quantity,
                'unit_price': unit_price,
                'discount_percent': discount_percent
            })
        
        current_order_idx += 1
    
    df = pd.DataFrame(data)
    
    # Introduce invalid references occasionally
    invalid_count = int(len(df) * 0.015)
    for _ in range(invalid_count):
        idx = random.randint(0, len(df)-1)
        if random.random() < 0.5:
            df.at[idx, 'product_id'] = f"INVALID_PROD_{random.randint(10000,99999)}"
        else:
            df.at[idx, 'order_id'] = f"INVALID_ORD_{random.randint(10000,99999)}"
    
    # Duplicate some rows
    dup_count = int(len(df) * 0.01)
    for _ in range(dup_count):
        dup_row = df.sample(1).iloc[0].copy()
        dup_row['item_id'] = f"DUP_{dup_row['item_id']}"
        df = pd.concat([df, pd.DataFrame([dup_row])], ignore_index=True)
    
    return df

def main():
    print("Starting E-Commerce Dataset Generation...")
    
    # Generate datasets
    customers_df = generate_customers(700)
    products_df = generate_products(300)
    orders_df = generate_orders(customers_df, 5000)
    order_items_df = generate_order_items(orders_df, products_df, 12000)
    
    # Save to CSV
    customers_df.to_csv('data/raw/customers.csv', index=False)
    products_df.to_csv('data/raw/products.csv', index=False)
    orders_df.to_csv('data/raw/orders.csv', index=False)
    order_items_df.to_csv('data/raw/order_items.csv', index=False)
    
    # Print summary
    print(f"Total customers: {len(customers_df)}")
    print(f"Total products: {len(products_df)}")
    print(f"Total orders: {len(orders_df)}")
    print(f"Total order_items: {len(order_items_df)}")
    print("\nDataset Generation Completed Successfully")
    
    # Display first 5 rows of each
    print("\n=== Customers (first 5 rows) ===")
    print(customers_df.head())
    print("\n=== Products (first 5 rows) ===")
    print(products_df.head())
    print("\n=== Orders (first 5 rows) ===")
    print(orders_df.head())
    print("\n=== Order Items (first 5 rows) ===")
    print(order_items_df.head())

if __name__ == "__main__":
    main()