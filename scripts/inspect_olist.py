
import csv
from pathlib import Path

# Find the project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Location of our downloaded dataset
DATA_DIR = PROJECT_DIR / "data" / "source" / "olist"

EXPECTED_FILES = {
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
}

def inspect_dataset():
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Dataset directory missing: {DATA_DIR}")

    files = sorted(DATA_DIR.glob("*.csv"))
    found_files = {file.name for file in files}

    missing = EXPECTED_FILES - found_files
    if missing:
        raise FileNotFoundError(f"Missing dataset files: {sorted(missing)}")

    print("\nOLIST SOURCE DATA INSPECTION")
    print("=" * 55)

    for file in files:
        with file.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            columns = reader.fieldnames or []
            count = sum(1 for _ in reader)

        print(f"\nFile: {file.name}")
        print(f"Records: {count:,}")
        print(f"Columns ({len(columns)}): {', '.join(columns)}")
        print("-" * 55)

    print("\nDataset inspection complete!")

if __name__ == "__main__":
    inspect_dataset()
