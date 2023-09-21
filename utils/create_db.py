import os
import pandas as pd
import sqlite3

# Path to the folder containing Excel files
excel_folder = 'Database'

# Path to the SQLite database file
db_file = 'output_database.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Get a list of Excel files in the folder
excel_files = [file for file in os.listdir(excel_folder) if file.endswith('.xlsx')]

# Process each Excel file
for excel_file in excel_files:
    table_name = os.path.splitext(excel_file)[0]  # Table name without extension
    
    # Read the Excel file into a DataFrame
    excel_path = os.path.join(excel_folder, excel_file)
    df = pd.read_excel(excel_path)
    
    # Convert Timestamp columns to string format
    for col in df.select_dtypes(include=['datetime64']):
        df[col] = df[col].astype(str)
    
    # Create the table in the SQLite database
    columns = ', '.join([f'{col} TEXT' for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(create_table_query)
    
    # Insert data into the table
    placeholders = ', '.join(['?'] * len(df.columns))
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.executemany(insert_query, df.values.tolist())
    
    # Commit the changes
    conn.commit()

# Close the database connection
conn.close()

print("Conversion completed.")