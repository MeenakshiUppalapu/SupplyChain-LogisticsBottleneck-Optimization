import csv
import random
from datetime import datetime, timedelta

# --- CONFIGURATION & SEEDING FOR REPLICABILITY ---
random.seed(42)
NUM_ORDERS = 5000

# --- 1. GENERATE DIM_CARRIERS ---
carriers = [
    {"carrier_id": "C01", "carrier_name": "Canada Post", "mode": "Ground"},
    {"carrier_id": "C02", "carrier_name": "FedEx Express", "mode": "Air"},
    {"carrier_id": "C03", "carrier_name": "CN Rail", "mode": "Rail"},
    {"carrier_id": "C04", "carrier_name": "Challenger Motor Freight", "mode": "Truckload"}
]

# --- 2. GENERATE DIM_PROVINCES (Canadian Hubs) ---
provinces = [
    {"province_code": "ON", "hub_city": "Brampton", "region": "Central"},
    {"province_code": "QC", "hub_city": "Montreal", "region": "East"},
    {"province_code": "BC", "hub_city": "Delta", "region": "West"},
    {"province_code": "AB", "hub_city": "Calgary", "region": "West"},
    {"province_code": "NS", "hub_city": "Halifax", "region": "Atlantic"}
]

# --- 3. GENERATE DIM_PRODUCTS ---
categories = ["Electronics", "Home Appliances", "Apparel", "Automotive", "Industrial Supplies"]
products = []
for i in range(1, 101):  # 100 Unique Products
    category = random.choice(categories)

    # Establish realistic stock parameters
    safety_stock = random.randint(50, 200)
    # Simulate a few products being critically low on inventory (Stockout risk)
    current_inventory = random.choice([random.randint(10, 45), random.randint(200, 800)])

    products.append({
        "product_id": f"P{i:03d}",
        "product_name": f"Product Alpha {i}",
        "category": category,
        "unit_weight_kg": round(random.uniform(0.5, 45.0), 2),
        "safety_stock_level": safety_stock,
        "current_inventory_level": current_inventory
    })

# --- 4. GENERATE FACT_SHIPMENTS ---
start_date = datetime(2025, 1, 1)
shipments = []

for order_id in range(10001, 10001 + NUM_ORDERS):
    product = random.choice(products)
    carrier = random.choice(carriers)
    origin = random.choice(provinces)

    # Ensure destination isn't the exact same as origin
    destination = random.choice([p for p in provinces if p["province_code"] != origin["province_code"]])

    # Date logic
    days_offset = random.randint(0, 360)
    order_date = start_date + timedelta(days=days_offset)

    # Define Target vs Actual Transit Times to simulate operational bottlenecks
    # Air is fast, Rail is slower.
    if carrier["carrier_id"] == "C02":  # Air
        target_days = random.randint(1, 2)
        # Simulate BC and NS weather/customs anomalies causing unexpected bottlenecks
        actual_days = target_days + random.choice([0, 0, 0, 1, 3]) if destination["province_code"] in ["BC",
                                                                                                       "NS"] else target_days + random.choice(
            [0, 0, 1])
    elif carrier["carrier_id"] == "C03":  # Rail
        target_days = random.randint(6, 8)
        actual_days = target_days + random.choice([0, 1, 2, 4, -1])
    else:  # Ground / Truck
        target_days = random.randint(3, 5)
        actual_days = target_days + random.choice([0, 0, 1, 2, 5])

    shipment_date = order_date + timedelta(days=1)
    delivery_date = shipment_date + timedelta(days=actual_days)

    # Financials
    quantity = random.randint(1, 15)
    base_cost = round(product["unit_weight_kg"] * quantity * random.uniform(1.5, 3.5), 2)
    # Apply heavy fuel surcharges/late penalties to delayed shipments
    shipping_cost = round(base_cost * 1.4, 2) if actual_days > target_days else base_cost

    shipments.append({
        "transaction_id": f"TXN{order_id}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "shipment_date": shipment_date.strftime("%Y-%m-%d"),
        "delivery_date": delivery_date.strftime("%Y-%m-%d"),
        "product_id": product["product_id"],
        "carrier_id": carrier["carrier_id"],
        "origin_province": origin["province_code"],
        "destination_province": destination["province_code"],
        "quantity_shipped": quantity,
        "shipping_cost_cad": shipping_cost,
        "target_transit_days": target_days,
        "actual_transit_days": actual_days
    })


# --- WRITE TABLES TO CSV ---
def write_csv(filename, fieldnames, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully generated: {filename}")


write_csv("Dim_Carriers.csv", ["carrier_id", "carrier_name", "mode"], carriers)
write_csv("Dim_Provinces.csv", ["province_code", "hub_city", "region"], provinces)
write_csv("Dim_Products.csv",
          ["product_id", "product_name", "category", "unit_weight_kg", "safety_stock_level", "current_inventory_level"],
          products)
write_csv("Fact_Shipments.csv",
          ["transaction_id", "order_date", "shipment_date", "delivery_date", "product_id", "carrier_id",
           "origin_province", "destination_province", "quantity_shipped", "shipping_cost_cad", "target_transit_days",
           "actual_transit_days"], shipments)
