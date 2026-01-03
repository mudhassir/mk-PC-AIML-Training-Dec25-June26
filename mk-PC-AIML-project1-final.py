
# Mudhassir Khan:

# Course-end Project 1: Analyzing Customer Orders Using Python

"""
Docstring for mk-PC-AIML-Training-Dec25:
You are working as a data analyst for an e-commerce company.
Your task is to process and analyze customer orders to generate meaningful insights.
Your company sells a variety of products across different categories, such as Electronics, Clothing, and Home Essentials.
You need to determine which products are frequently purchased, classify customers based on their total spending, and analyze the most profitable product categories.

To achieve this, you will store, categorize, and analyze customer purchase data using Python's built-in data structures (lists, tuples, dictionaries, and sets) and control structures (loops and conditionals).
The final output will help business managers make data-driven decisions regarding marketing strategies and inventory management.
"""

# E-Commerce Order Analysis System

# Sample product catalog with (product_id, name, category, price)
products = {
    'Pid1': ('Laptop', 'Electronics', 999.99),
    'Pid2': ('Tablet', 'Electronics', 299.99),
    'Pid3': ('Smartphone', 'Electronics', 699.99),
    'Pid4': ('Headphones', 'Electronics', 109.99),
    'Pid5': ('Shirt', 'Clothing', 29.99),
    'Pid6': ('Denim', 'Clothing', 35.99),
    'Pid7': ('Shoes', 'Clothing', 55.99),
    'Pid8': ('Clock', 'Home Essentials', 29.99),
    'Pid9': ('Heater', 'Home Essentials', 99.99),
    'Pid10': ('Fan', 'Home Essentials', 59.99)
}

# Sample customer orders: list of tuples (customer_id, product_id, quantity)
orders = [
    ('Alex', 'Pid1', 6), ('Alex', 'Pid3', 1), ('Alex', 'Pid7', 3),
    ('Brian', 'Pid2', 5), ('Brian', 'Pid4', 2), ('Brian', 'Pid5', 1),
    ('Chad', 'Pid1', 4), ('Chad', 'Pid10', 3), ('Chad', 'Pid3', 3),
    ('Dave', 'Pid4', 1), ('Dave', 'Pid6', 2), ('Dave', 'Pid8', 3),
    ('Evan', 'Pid7', 3), ('Evan', 'Pid9', 5), ('Evan', 'Pid3', 3),
    ('Fred', 'Pid1', 3), ('Fred', 'Pid2', 3), ('Fred', 'Pid10', 1),
    ('George', 'Pid4', 6), ('George', 'Pid5', 7), ('George', 'Pid6', 1),
    ('Hamza', 'Pid8', 4), ('Hamza', 'Pid9', 8), ('Hamza', 'Pid7', 1),
    ('Ian', 'Pid2', 5), ('Ian', 'Pid3', 2), ('Ian', 'Pid1', 1),
    ('John', 'Pid10', 7), ('John', 'Pid4', 1), ('John', 'Pid5', 2)
]

def calculate_customer_spending():
    # Calculate total spending for each customer
    customer_spending = {}
    
    for customer_id, product_id, quantity in orders:
        if product_id in products:
            product_name, category, price = products[product_id]
            total_price = price * quantity
            
            if customer_id in customer_spending:
                customer_spending[customer_id] += total_price
            else:
                customer_spending[customer_id] = total_price
    return customer_spending

def classify_customers(customer_spending):
    # Classify customers based on their total spending
    customer_tiers = {'Premium': [], 'Gold': [], 'Silver': [], 'Bronze': []}
    
    for customer_id, total_spent in customer_spending.items():
        if total_spent >= 2500:
            customer_tiers['Premium'].append((customer_id, total_spent))
        elif total_spent >= 1500:
            customer_tiers['Gold'].append((customer_id, total_spent))
        elif total_spent >= 500:
            customer_tiers['Silver'].append((customer_id, total_spent))
        else:
            customer_tiers['Bronze'].append((customer_id, total_spent))
    return customer_tiers

def find_popular_products():
    # Find most frequently purchased products
    product_frequency = {}
    
    for customer_id, product_id, quantity in orders:
        if product_id in product_frequency:
            product_frequency[product_id] += quantity
        else:
            product_frequency[product_id] = quantity
    
    # Sort by quantity sold (descending)
    sorted_products = sorted(product_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_products

def analyze_category_revenue():
    # Calculate revenue by product category
    category_revenue = {}

    for customer_id, product_id, quantity in orders:
        if product_id in products:
            product_name, category, price = products[product_id]
            revenue = price * quantity
            
            if category in category_revenue:
                category_revenue[category] += revenue
            else:
                category_revenue[category] = revenue
    
    # Sort by revenue (descending)
    sorted_categories = sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)
    return sorted_categories

def get_unique_customers():
    # Return set of unique customers who made purchases
    return {customer_id for customer_id, _, _ in orders}

def comprehensive_analysis_report():
    # Generate comprehensive analysis report
    print("*" * 80)
    print("E-COMMERCE DATA ANALYSIS REPORT")
    print("*" * 80)
    print()
    
    # Customer Spending Analysis
    customer_spending = calculate_customer_spending()
    print("1. CUSTOMER SPENDING ANALYSIS:")
    print("-" * 80)
    for count, (customer_id, total) in enumerate(sorted(customer_spending.items(), key=lambda x: x[1], reverse=True), 1):
        print(f"   {count:2d}. {customer_id} spent: ${total:.2f}")
    print("")
    
    # Function to identify Customer Classification
    customer_tiers = classify_customers(customer_spending)
    print("2. CUSTOMER CLASSIFICATION BASED on SPENDING:")
    print("  'Premium' > $2500, 'Gold' > $1500, 'Silver' > $500, 'Bronze' <= $500")
    print("-" * 80)
    for tier, customers in customer_tiers.items():
        if customers:
            print(f"   {tier} Tier ({len(customers)} customers):")
            for customer_id, amount in sorted(customers, key=lambda x: x[1], reverse=True):
                print(f"      {customer_id}: ${amount:.2f}")
    print()
    
    # Function to calculate the Popular Products
    popular_products = find_popular_products()
    print("3. MOST PROFITABLE PRODUCT CATEGORIES (by quantity sold):")
    print("-" * 80)
    for i, (product_id, quantity) in enumerate(popular_products[:5], 1):
        product_name, category, price = products[product_id]
        revenue = price * quantity
        print(f"   {i}. {product_name} ({category})")
        print(f"      Units Sold: {quantity} | Revenue: ${revenue:.2f}")
    print()
    

    # Category Revenue Analysis
    category_revenue = analyze_category_revenue()
    print("4. REVENUE BY PRODUCT CATEGORY")
    print("-" * 80)
    total_revenue = sum(revenue for _, revenue in category_revenue)
    for category, revenue in category_revenue:
        percentage = (revenue / total_revenue) * 100
        print(f"   {category}: ${revenue:.2f} ({percentage:.1f}%)")
    print(f"   {'Total Revenue'}: ${total_revenue:.2f}")
    print()

    # Key Metrics
    unique_customers = get_unique_customers()
    print("5. KEY BUSINESS METRICS")
    print("-" * 80)
    print(f"   Total Customers: {len(unique_customers)}")
    print(f"   Total Orders: {len(orders)}")
    print(f"   Average Order Value: ${total_revenue / len(orders):.2f}")
    print(f"   Average Customer Value: ${total_revenue / len(unique_customers):.2f}")
    print()
    
    # Business Recommendations
    print("6. BUSINESS RECOMMENDATIONS")
    print("-" * 80)
    premium_count = len(customer_tiers['Premium'])
    if premium_count > 0:
        print(f"   • Create loyalty program for {premium_count} Premium customers")

    top_category = category_revenue[0][0]
    print(f"   • Focus marketing and stocking on {top_category} that's generating highest revenue")
    
    top_product_id = popular_products[0][0]
    top_product_name = products[top_product_id][0]
    print(f"   • Ensure adequate stock of '{top_product_name}' (best seller)")
    
    low_performers = [cat for cat, rev in category_revenue if rev < total_revenue * 0.2]
    if low_performers:
        print(f"   • Review inventory for underperforming categories: {', '.join(low_performers)}")
    
    print()
    print("*" * 80)
    print()

# Run the analysis
comprehensive_analysis_report()
