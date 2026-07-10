import argparse
import sqlite3
from tabulate import tabulate

# ---------------------------------------
# Database Connection
# ---------------------------------------
DB_NAME = "ecommerce.db"

def connect_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Exception as e:
        print(f"Database Connection Error: {e}")
        exit()


# ---------------------------------------
# SQL Queries
# ---------------------------------------
queries = {

    "revenue": """
    SELECT
        c.customer_name,
        ROUND(SUM(oi.total_amount),2) AS total_revenue
    FROM customers_clean c
    JOIN orders_clean o
        ON c.customer_id = o.customer_id
    JOIN order_items_clean oi
        ON o.order_id = oi.order_id
    GROUP BY c.customer_name
    ORDER BY total_revenue DESC
    LIMIT 10;
    """,

    "top_products": """
    SELECT
        p.product_name,
        SUM(oi.quantity) AS quantity_sold,
        ROUND(SUM(oi.total_amount),2) AS revenue
    FROM products_clean p
    JOIN order_items_clean oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
    ORDER BY revenue DESC
    LIMIT 10;
    """,

    "top_customers": """
    SELECT
        c.customer_name,
        ROUND(SUM(oi.total_amount),2) AS spending
    FROM customers_clean c
    JOIN orders_clean o
        ON c.customer_id=o.customer_id
    JOIN order_items_clean oi
        ON o.order_id=oi.order_id
    GROUP BY c.customer_name
    ORDER BY spending DESC
    LIMIT 10;
    """,

    "aov": """
    SELECT
        c.customer_type,
        ROUND(AVG(order_total),2) AS average_order_value
    FROM
    (
        SELECT
            o.order_id,
            o.customer_id,
            SUM(oi.total_amount) AS order_total
        FROM orders_clean o
        JOIN order_items_clean oi
            ON o.order_id=oi.order_id
        GROUP BY o.order_id,o.customer_id
    ) x
    JOIN customers_clean c
        ON x.customer_id=c.customer_id
    GROUP BY c.customer_type;
    """,

    "retention": """
    SELECT
        customer_id,
        COUNT(order_id) AS total_orders
    FROM orders_clean
    GROUP BY customer_id
    ORDER BY total_orders DESC
    LIMIT 10;
    """,

    "segmentation": """
    SELECT
        customer_type,
        COUNT(*) AS total_customers
    FROM customers_clean
    GROUP BY customer_type;
    """
}


# ---------------------------------------
# Execute Query
# ---------------------------------------
def run_report(report):

    conn = connect_db()
    cursor = conn.cursor()

    if report not in queries:
        print("\nInvalid Report Name\n")
        print("Available Reports:")
        for r in queries.keys():
            print("-", r)
        return

    try:
        cursor.execute(queries[report])

        rows = cursor.fetchall()

        if not rows:
            print("\nNo Records Found\n")
            return

        headers = [i[0] for i in cursor.description]

        print("\n")
        print(tabulate(rows,
                       headers=headers,
                       tablefmt="grid"))
        print()

    except Exception as e:
        print(f"\nError : {e}")

    finally:
        conn.close()


# ---------------------------------------
# Main
# ---------------------------------------
def main():

    parser = argparse.ArgumentParser(
        description="E-Commerce Analytics Reporting Tool"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="""
Available Reports:

revenue
top_products
top_customers
aov
retention
segmentation
"""
    )

    args = parser.parse_args()

    run_report(args.report)


if __name__ == "__main__":
    main()