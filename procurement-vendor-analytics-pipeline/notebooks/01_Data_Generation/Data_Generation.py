

import logging
import random
import sys
import time
import psutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
from faker import Faker

# ====================== CONFIGURATION ======================
RANDOM_SEED = 42
NUM_VENDORS = 500
NUM_PRODUCTS = 100
NUM_PURCHASE_ORDERS = 100_000
NUM_VENDOR_CONTRACTS = 20_000
NUM_INVOICES = 100_000

REGIONS = ["North", "South", "East", "West", "Central"]
PAYMENT_TERMS = ["Net15", "Net30", "Net45", "Net60"]

BASE_PRODUCTS = [
    "Steel Rod", "Copper Wire", "PVC Pipe", "Industrial Paint", "Hydraulic Pump",
    "Safety Helmet", "Electric Motor", "Bearing", "Transformer Oil", "Lubricant",
    "Control Panel", "Fasteners", "Valves", "Circuit Breaker", "Gearbox",
    "Conveyor Belt", "Welding Rod", "Pressure Gauge", "Flow Meter", "Pneumatic Cylinder"
]

# ====================== SETUP ======================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

fake = Faker()
Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def get_project_root() -> Path:
    current = Path(__file__).resolve().parent

    # Search current directory and all parent directories
    for parent in [current] + list(current.parents):
        if (
            (parent / "data").is_dir()
            and (parent / "notebooks").is_dir()
        ):
            return parent

    raise FileNotFoundError(
        "Project root not found. Expected directories "
        "'data/' and 'notebooks/' were not found."
    )


def generate_vendors() -> pd.DataFrame:
    logger.info("Generating vendors...")
    vendors = []
    for i in range(1, NUM_VENDORS + 1):
        vendor_id = f"V{str(i).zfill(4)}"
        vendors.append({
            "vendor_id": vendor_id,
            "vendor_name": fake.company(),
            "region": random.choice(REGIONS)
        })
    return pd.DataFrame(vendors)


def generate_products() -> pd.DataFrame:
    """Generate unique products with categories and realistic base prices."""
    logger.info("Generating products...")

    categories = [
        "Mechanical",
        "Electrical",
        "Fluid",
        "Safety",
        "Structural",
        "Instrumentation"
    ]

    products = []
    existing_products = set()

    while len(products) < NUM_PRODUCTS:
        category = random.choice(categories)
        base_product = random.choice(BASE_PRODUCTS)
        suffix = random.choice([
            "",
            " Heavy Duty",
            " Premium",
            " Standard",
            " Kit"
        ])

        item_name = f"{category} {base_product}{suffix}".strip()

        # Fast uniqueness check
        if item_name in existing_products:
            continue

        existing_products.add(item_name)

        # More realistic category-based pricing
        if category == "Mechanical":
            base_price = round(random.uniform(500, 4500), 2)
        elif category == "Electrical":
            base_price = round(random.uniform(200, 3000), 2)
        elif category == "Fluid":
            base_price = round(random.uniform(100, 2500), 2)
        elif category == "Safety":
            base_price = round(random.uniform(20, 500), 2)
        elif category == "Structural":
            base_price = round(random.uniform(300, 3500), 2)
        else:  # Instrumentation
            base_price = round(random.uniform(250, 4000), 2)

        products.append({
            "item_name": item_name,
            "category": category,
            "base_price": base_price
        })

    logger.info(f"Generated {len(products):,} unique products.")

    return pd.DataFrame(products)


def generate_purchase_orders(vendors_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Generating purchase orders...")

    vendor_region_map = vendors_df.set_index("vendor_id")["region"].to_dict()

    po_ids = [f"PO{str(i).zfill(6)}" for i in range(1, NUM_PURCHASE_ORDERS + 1)]
    vendor_ids = np.random.choice(vendors_df["vendor_id"].values, NUM_PURCHASE_ORDERS, p=np.random.dirichlet(np.ones(NUM_VENDORS) * 4))
    item_names = np.random.choice(products_df["item_name"].values, NUM_PURCHASE_ORDERS)
    quantities = np.random.randint(1, 501, NUM_PURCHASE_ORDERS)

    start_date = datetime(2022, 1, 1)
    end_date = datetime(2025, 12, 31)
    po_dates = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(NUM_PURCHASE_ORDERS)]

    regions = [vendor_region_map.get(v, random.choice(REGIONS)) for v in vendor_ids]

    return pd.DataFrame({
        "po_id": po_ids,
        "vendor_id": vendor_ids,
        "item_name": item_names,
        "quantity": quantities,
        "po_date": po_dates,
        "region": regions
    })


def generate_vendor_contracts(
    vendors_df: pd.DataFrame,
    products_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Generate realistic vendor contracts with correlated pricing,
    payment terms, and effective dates.
    """
    logger.info("Generating vendor contracts...")

    contracts = []

    # Vendor-specific payment terms
    vendor_payment_terms = {
        vendor_id: random.choice(PAYMENT_TERMS)
        for vendor_id in vendors_df["vendor_id"]
    }

    for contract_num in range(1, NUM_VENDOR_CONTRACTS + 1):

        vendor = vendors_df.sample(1).iloc[0]
        product = products_df.sample(1).iloc[0]

        base_price = product["base_price"]

        # Contract prices stay close to product base price
        contract_price = round(
            base_price * random.uniform(0.92, 1.08),
            2
        )

        effective_date = (
            datetime(2021, 1, 1)
            + timedelta(days=random.randint(0, 1460))
        ).date()

        contracts.append({
            "contract_id": f"CON{contract_num:06d}",
            "vendor_id": vendor["vendor_id"],
            "item_name": product["item_name"],
            "category": product["category"],
            "contract_price": contract_price,
            "payment_terms": vendor_payment_terms[vendor["vendor_id"]],
            "effective_date": effective_date
        })

    contracts_df = pd.DataFrame(contracts)

    logger.info(
        f"Generated {len(contracts_df):,} vendor contracts."
    )

    return contracts_df



def generate_invoices(
    po_df: pd.DataFrame,
    contracts_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Generate invoices based on purchase orders and vendor contracts.

    Business Rules
    --------------
    - Invoice date is always after PO date.
    - Invoice amount is based on the latest contract price.
    - 90% invoices match contract price.
    - 10% are intentionally overcharged.
    """

    logger.info("Generating invoices...")

    sampled_pos = (
        po_df.sample(
            n=NUM_INVOICES,
            replace=True,
            random_state=RANDOM_SEED
        )
        .reset_index(drop=True)
    )

    # Always use the latest contract
    latest_contracts = (
        contracts_df
        .sort_values("effective_date")
        .drop_duplicates(
            subset=["vendor_id", "item_name"],
            keep="last"
        )
    )

    merged = sampled_pos.merge(
        latest_contracts[
            [
                "vendor_id",
                "item_name",
                "contract_price"
            ]
        ],
        on=["vendor_id", "item_name"],
        how="left"
    )

    fallback_price = pd.Series(
    np.random.uniform(50, 800, len(merged)),
    index=merged.index
    )

    merged["contract_price"] = merged["contract_price"].fillna(fallback_price)

    # 90% normal invoices
    # 10% intentionally overcharged
    price_multiplier = np.where(
        np.random.rand(len(merged)) < 0.90,
        np.random.uniform(0.98, 1.02, len(merged)),
        np.random.uniform(1.08, 1.20, len(merged))
    )

    invoice_amount = np.round(
        merged["quantity"]
        * merged["contract_price"]
        * price_multiplier,
        2
    )

    # Vectorized invoice dates
    invoice_dates = (
        pd.to_datetime(sampled_pos["po_date"])
        + pd.to_timedelta(
            np.random.randint(
                5,
                45,
                len(sampled_pos)
            ),
            unit="D"
        )
    ).dt.date

    payment_status = np.random.choice(
        [
            "Paid",
            "Pending",
            "Overdue"
        ],
        size=len(sampled_pos),
        p=[0.72, 0.18, 0.10]
    )

    invoices_df = pd.DataFrame({
        "invoice_id": [
            f"INV{i:06d}"
            for i in range(1, len(sampled_pos) + 1)
        ],
        "po_id": sampled_pos["po_id"],
        "vendor_id": sampled_pos["vendor_id"],
        "invoiced_amount": invoice_amount,
        "invoice_date": invoice_dates,
        "payment_status": payment_status
    })

    logger.info(
        f"Generated {len(invoices_df):,} invoices."
    )

    return invoices_df

def inject_data_quality_issues(
    df: pd.DataFrame,
    dataset_name: str
) -> pd.DataFrame:
    """
    Inject realistic data quality issues into a dataset.

    Issues Introduced
    -----------------
    - 2% duplicate records
    - 2% missing values
    - Mixed case values
    - Leading/trailing whitespace
    - Negative invoice amounts
    - Invalid payment terms
    - Invalid dates
    """

    logger.info(f"Injecting data quality issues into {dataset_name}...")

    df = df.copy()

    # -------------------------
    # Duplicate Rows (2%)
    # -------------------------
    duplicate_count = int(len(df) * 0.02)

    if duplicate_count > 0:
        duplicate_rows = df.sample(
            n=duplicate_count,
            random_state=RANDOM_SEED
        )

        df = pd.concat(
            [df, duplicate_rows],
            ignore_index=True
        )

    # Current dataframe size
    current_size = len(df)

    # -------------------------
    # Missing Values (2%)
    # -------------------------
    nullable_columns = [
        "vendor_id",
        "quantity",
        "po_id",
        "invoiced_amount"
    ]

    for column in nullable_columns:

        if column in df.columns:

            idx = np.random.choice(
                df.index,
                size=int(current_size * 0.02),
                replace=False
            )

            df.loc[idx, column] = np.nan

    # -------------------------
    # Mixed Case
    # -------------------------
    if "region" in df.columns:

        idx = np.random.choice(
            df.index,
            size=int(current_size * 0.10),
            replace=False
        )

        df.loc[idx, "region"] = (
            df.loc[idx, "region"]
            .astype(str)
            .str.lower()
        )

    # -------------------------
    # Extra Whitespace
    # -------------------------
    if "vendor_id" in df.columns:

        idx = np.random.choice(
            df.index,
            size=int(current_size * 0.02),
            replace=False
        )

        df.loc[idx, "vendor_id"] = (
            " "
            + df.loc[idx, "vendor_id"].astype(str)
            + " "
        )

    # -------------------------
    # Negative Invoice Amount
    # -------------------------
    if "invoiced_amount" in df.columns:

        idx = np.random.choice(
            df.index,
            size=int(current_size * 0.008),
            replace=False
        )

        df.loc[idx, "invoiced_amount"] = (
            -df.loc[idx, "invoiced_amount"].abs()
        )

    # -------------------------
    # Invalid Payment Terms
    # -------------------------
    if "payment_terms" in df.columns:

        idx = np.random.choice(
            df.index,
            size=int(current_size * 0.01),
            replace=False
        )

        df.loc[idx, "payment_terms"] = "Net999"

        # -------------------------
    # Invalid Dates (0.6%)
    # -------------------------
    invalid_dates = [
        "2025-13-45",
        "2024-99-99",
        "9999-99-99"
    ]

    for column in df.columns:

        if "date" in column.lower():

            # Convert datetime column to object so invalid strings can be stored
            df[column] = df[column].astype("object")

            idx = np.random.choice(
                df.index,
                size=max(1, int(current_size * 0.006)),
                replace=False
            )

            df.loc[idx, column] = np.random.choice(
                invalid_dates,
                size=len(idx)
            )
    return df


def print_validation_report(datasets: Dict[str, pd.DataFrame]) -> None:
    """
    Print a validation summary for all generated datasets.
    """

    print("\n" + "=" * 90)
    print("                    DATA VALIDATION REPORT")
    print("=" * 90)

    for dataset_name, df in datasets.items():

        total_rows = len(df)
        total_columns = len(df.columns)
        duplicate_count = df.duplicated().sum()
        total_nulls = df.isnull().sum().sum()

        duplicate_pct = (
            (duplicate_count / total_rows) * 100
            if total_rows else 0
        )

        null_pct = (
            (total_nulls / (total_rows * total_columns)) * 100
            if total_rows and total_columns else 0
        )

        memory_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)

        print(f"\n{dataset_name.replace('_', ' ').title()}")
        print("-" * 90)
        print(f"Rows               : {total_rows:,}")
        print(f"Columns            : {total_columns}")
        print(f"Duplicate Rows     : {duplicate_count:,} ({duplicate_pct:.2f}%)")
        print(f"Total Null Values  : {total_nulls:,} ({null_pct:.2f}%)")
        print(f"Memory Usage       : {memory_mb:.2f} MB")

        print("\nColumn Data Types")
        print(df.dtypes.to_string())

        print("-" * 90)

    print("\nValidation completed successfully.")
    print("=" * 90)


def save_csv(df: pd.DataFrame, filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)
    logger.info(f"Saved {len(df):,} records → {filepath.name}")


def main() -> None:
    """
    Main pipeline execution.
    """
    start_time = time.perf_counter()

    try:
        logger.info("=" * 80)
        logger.info("PROCUREMENT DATA GENERATION PIPELINE STARTED")
        logger.info("=" * 80)

        project_root = get_project_root()
        raw_dir = project_root / "data" / "raw"

        logger.info(f"Project Root : {project_root}")
        logger.info(f"Output Folder: {raw_dir}")

        # -------------------------------
        # STEP 1
        # -------------------------------
        logger.info("[STEP 1/5] Generating Vendors & Products...")

        vendors_df = generate_vendors()
        products_df = generate_products()

        logger.info(
            f"Completed | Vendors: {len(vendors_df):,} | Products: {len(products_df):,}"
        )

        # -------------------------------
        # STEP 2
        # -------------------------------
        logger.info("[STEP 2/5] Generating Purchase Orders...")

        po_df = generate_purchase_orders(
            vendors_df,
            products_df
        )

        logger.info(
            f"Completed | Purchase Orders: {len(po_df):,}"
        )

        # -------------------------------
        # STEP 3
        # -------------------------------
        logger.info("[STEP 3/5] Generating Vendor Contracts...")

        contracts_df = generate_vendor_contracts(
            vendors_df,
            products_df
        )

        logger.info(
            f"Completed | Contracts: {len(contracts_df):,}"
        )

        # -------------------------------
        # STEP 4
        # -------------------------------
        logger.info("[STEP 4/5] Generating Invoices...")

        invoices_df = generate_invoices(
            po_df,
            contracts_df
        )

        logger.info(
            f"Completed | Invoices: {len(invoices_df):,}"
        )

        # -------------------------------
        # STEP 5
        # -------------------------------
        logger.info("[STEP 5/5] Injecting Data Quality Issues...")

        po_df = inject_data_quality_issues(
            po_df,
            "purchase_orders"
        )

        contracts_df = inject_data_quality_issues(
            contracts_df,
            "vendor_contracts"
        )

        invoices_df = inject_data_quality_issues(
            invoices_df,
            "invoices"
        )

        logger.info("Data quality issues injected successfully.")

        datasets = {
            "purchase_orders": po_df,
            "vendor_contracts": contracts_df,
            "invoices": invoices_df
        }

        # -------------------------------
        # Validation
        # -------------------------------
        print_validation_report(datasets)

        # -------------------------------
        # Save Files
        # -------------------------------
        logger.info("Saving CSV files...")

        save_csv(
            po_df,
            raw_dir / "purchase_orders.csv"
        )

        save_csv(
            contracts_df,
            raw_dir / "vendor_contracts.csv"
        )

        save_csv(
            invoices_df,
            raw_dir / "invoices.csv"
        )

        # -------------------------------
        # Metrics
        # -------------------------------
        execution_time = time.perf_counter() - start_time

        process = psutil.Process()

        memory_mb = (
            process.memory_info().rss
            / (1024 ** 2)
        )

        total_records = (
            len(po_df)
            + len(contracts_df)
            + len(invoices_df)
        )

        logger.info("=" * 80)
        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("=" * 80)

        logger.info(f"Execution Time : {execution_time:.2f} sec")
        logger.info(f"Memory Usage   : {memory_mb:.2f} MB")
        logger.info(f"Total Records  : {total_records:,}")
        logger.info(f"Output Path    : {raw_dir.resolve()}")

        print("\n✅ Data generation completed successfully!")

    except Exception:
        logger.exception("Pipeline execution failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()