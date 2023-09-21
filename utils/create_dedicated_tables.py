import os
import pandas as pd
import sqlite3

# Path to the folder containing Excel files
excel_folder = 'Database'

# Path to the final SQLite database file
db_file = 'enhanced_database.db'

# Define table configurations
table_configs = {
    'communication': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('communication_id', 'TEXT'),
            ('cust_id', 'TEXT'),
            ('contact_communication_date', 'TEXT'),
            ('contact_communication_channel', 'TEXT'),
            ('contact_communication_type', 'TEXT'),
            ('contact_communication_details', 'TEXT')
        ],
        'key_column': 'row_id'
    },
    'customers': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('customer_id', 'TEXT'),
            ('first_name', 'TEXT'),
            ('middle_name', 'TEXT'),
            ('last_name', 'TEXT'),
            ('gender', 'TEXT'),
            ('date_of_birth', 'TEXT'),
            ('age', 'INTEGER'),
            ('marital_status', 'TEXT'),
            ('number_of_dependants', 'INTEGER'),
            ('email_address', 'TEXT'),
            ('mobile_phone_number', 'TEXT'),
            ('work_phone_number', 'TEXT'),
            ('home_phone_number', 'TEXT'),
            ('mailing_address1', 'TEXT'),
            ('mailing_address2', 'TEXT'),
            ('city', 'TEXT'),
            ('state', 'TEXT'),
            ('zip_postal_code', 'TEXT'),
            ('country', 'TEXT'),
            ('income_level', 'TEXT'),
            ('credit_score', 'INTEGER'),
            ('distance_nearest_branch', 'REAL')
        ],
        'key_column': 'row_id'
    },
    'interactions': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('interactions_id', 'TEXT'),
            ('cust_id', 'TEXT'),
            ('interaction_date', 'TEXT'),
            ('interaction_channel', 'TEXT'),
            ('interaction_type', 'TEXT'),
            ('interaction_details', 'TEXT')
        ],
        'key_column': 'row_id'
    },
    'life_events': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('life_events_id', 'TEXT'),
            ('cust_id', 'TEXT'),
            ('life_event_date', 'TEXT'),
            ('life_event_type', 'TEXT')
        ],
        'key_column': 'row_id'
    },
    'marketing_campaign': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('marketing_campaign_id', 'TEXT'),
            ('cust_id', 'TEXT'),
            ('marketing_campaign_response', 'TEXT'),
            ('product_interest', 'TEXT'),
            ('marketing_campaign_response_channel', 'TEXT'),
            ('marketing_campaign_cost', 'TEXT'),
            ('marketing_campaign_days', 'INTEGER'),
            ('marketing_campaign_startdate', 'TEXT'),
            ('marketing_campaign_enddate', 'TEXT')
        ],
        'key_column': 'row_id'
    },
    'products': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('product_id', 'TEXT'),
            ('cust_id', 'TEXT'),
            ('product_application_date', 'TEXT'),
            ('product', 'TEXT'),
            ('application_decision', 'TEXT')
        ],
        'key_column': 'row_id'
    },
    'transactions': {
        'columns': [
            ('row_id', 'INTEGER'),
            ('transaction_id', 'TEXT'),
            ('cust_id', 'TEXT'),
            ('transaction_date', 'TEXT'),
            ('transaction_amount', 'TEXT'),
            ('transaction_details', 'TEXT')
        ],
        'key_column': 'row_id'
    }
}

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Get a list of Excel files in the folder
excel_files = [file for file in os.listdir(excel_folder) if file.endswith('.xlsx')]

# Process each Excel file
for excel_file in excel_files:
    table_name = os.path.splitext(excel_file)[0]  # Table name without extension
    
    # Check if table configuration exists for the current file
    if table_name in table_configs:
        config = table_configs[table_name]
        
        # Read the Excel file into a DataFrame
        excel_path = os.path.join(excel_folder, excel_file)
        df = pd.read_excel(excel_path)
        
        # Convert Timestamp columns to string format
        for col in df.select_dtypes(include=['datetime64']):
            df[col] = df[col].astype(str)
        
        # Create the table in the SQLite database
        columns = ', '.join([f'{col} {dtype}' for col, dtype in config['columns']])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cursor.execute(create_table_query)
        
        # Insert data into the table
        placeholders = ', '.join(['?'] * len(config['columns']))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.executemany(insert_query, df.values.tolist())
        
        # Commit the changes
        conn.commit()

# Close the database connection
conn.close()

print("Database creation completed.")
