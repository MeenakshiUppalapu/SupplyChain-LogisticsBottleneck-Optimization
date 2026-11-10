-- =====================================================================
-- QUERY 1: Carrier SLA Breach & Freight Cost Leakage
-- Metric Focused: On-Time Delivery (OTD) % & Financial Penalties
-- =====================================================================
WITH shipment_perf AS (
    SELECT 
        s.transaction_id,
        s.shipping_cost_cad,
        c.carrier_name,
        c.mode AS transit_mode,
        s.target_transit_days,
        s.actual_transit_days,
        -- Binary flag indicating a Service Level Agreement (SLA) violation
        CASE WHEN s.actual_transit_days > s.target_transit_days THEN 1 ELSE 0 END AS is_delayed
    FROM 'Fact_Shipments.csv' AS s
    INNER JOIN 'Dim_Carriers.csv' AS c 
        ON s.carrier_id = c.carrier_id
)
SELECT 
    carrier_name,
    transit_mode,
    COUNT(transaction_id) AS total_dispatched_shipments,
    SUM(is_delayed) AS total_delayed_shipments,
    -- Calculate precise On-Time Delivery percentage
    ROUND(((COUNT(transaction_id) - SUM(is_delayed)) / COUNT(transaction_id)) * 100, 2) AS on_time_delivery_pct,
    -- Isolate capital locked or wasted on failing routes
    ROUND(SUM(CASE WHEN is_delayed = 1 THEN shipping_cost_cad ELSE 0 END), 2) AS delayed_freight_expenditure
FROM shipment_perf
GROUP BY carrier_name, transit_mode
ORDER BY on_time_delivery_pct ASC;
-- =====================================================================
-- QUERY 2: Inventory Safety Stock Disruption Analysis
-- Metric Focused: Stockout Risks & Inventory Health Index
-- =====================================================================
SELECT 
    category,
    COUNT(product_id) AS total_unique_sku_count,
    ROUND(AVG(safety_stock_level), 0) AS average_target_safety_stock,
    ROUND(AVG(current_inventory_level), 0) AS average_current_warehouse_stock,
    -- Isolate SKUs that have breached minimum protection protocols
    SUM(CASE WHEN current_inventory_level < safety_stock_level THEN 1 ELSE 0 END) AS skus_at_immediate_stockout_risk,
    -- Percentage of product group currently exposed to supply gaps
    ROUND((SUM(CASE WHEN current_inventory_level < safety_stock_level THEN 1 ELSE 0 END) / COUNT(product_id)) * 100, 2) AS category_exposure_rate_pct
FROM 'Dim_Products.csv'
GROUP BY category
ORDER BY skus_at_immediate_stockout_risk DESC;