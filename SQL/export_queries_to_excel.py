import sqlite3
import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "companies.db"
QUERIES_DIR = BASE_DIR / "queries"
OUTPUT_PATH = BASE_DIR / "query_outputs.xlsx"

# Connect to DB
conn = sqlite3.connect(DB_PATH)

# Function to run and export a query
def run_query_to_sheet(query_file, writer):
    query_name = query_file.stem.replace("_", " ").title()  # sheet name
    print(f"🟦 Running {query_name}...")

    # Read SQL content
    with open(query_file, "r") as f:
        sql = f.read()

    try:
        df = pd.read_sql_query(sql, conn)
        df.to_excel(writer, sheet_name=query_name[:31], index=False)
        print(f"✅ Exported {query_name} to Excel sheet")
    except Exception as e:
        print(f"❌ Error in {query_name}: {e}")

# Create Excel writer
with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
    for q in QUERIES_DIR.glob("*.sql"):
        run_query_to_sheet(q, writer)

conn.close()
print(f"\n🎉 All queries exported successfully to: {OUTPUT_PATH}")
