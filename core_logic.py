import pandas as pd
from datetime import datetime

def safe_data_cutoff(
    file_path,
    sheet_name,
    column,
    condition,
    value,
    max_row=None,
    backup=True
):
    # Load data
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
    
    original_count = len(df)

    # Apply max row limit
    if max_row:
        df = df.iloc[:max_row - 1]  # row 1 is header

    # Convert value if date
    try:
        value = pd.to_datetime(value)
        df[column] = pd.to_datetime(df[column], errors='coerce')
    except:
        pass

    # Filtering logic
    if condition == "<":
        mask = df[column] < value
    elif condition == ">":
        mask = df[column] > value
    elif condition == "=":
        mask = df[column] == value
    elif condition == "contains":
        mask = df[column].astype(str).str.contains(str(value), na=False)
    else:
        raise ValueError("Invalid condition")

    to_delete = df[mask]
    cleaned_df = df[~mask]

    # Backup
    if backup and not to_delete.empty:
        backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        to_delete.to_excel(backup_file, index=False)

    # Save cleaned data
    output_file = "cleaned_output.xlsx"
    cleaned_df.to_excel(output_file, index=False)

    print(f"Deleted rows: {len(to_delete)}")
    print(f"Remaining rows: {len(cleaned_df)}")
    print(f"Saved to: {output_file}")

'''
# sample
safe_data_cutoff(
    file_path="data.xlsx",
    sheet_name="Dec2Jan-QueueStat",
    column="Date",
    condition="<",
    value="2025-01-01",
    max_row=24444
)
'''