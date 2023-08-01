#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import io
import numpy as np
import pandas as pd

def transform_data(df):
    # Fill missing values in 'Agency' with 'Unknown'
    df['Agency'] = df['Agency'].fillna('Unknown')
    
    # Remove the word "Other" from the "listing category" column
    df['Listing Category'] = df['Listing Category'].str.replace('Other ', '')
    
    # Merge "Houses" into "Townhouses"
    df['Listing Category'] = df['Listing Category'].replace('Houses', 'Townhouses')
        
    # Fill Missing values for 'Bedrooms' and 'Bathrooms' with mode
    df['Bedrooms'] = df['Bedrooms'].fillna(df['Bedrooms'].mode().iloc[0])
    df['Bathrooms'] = df['Bathrooms'].fillna(df['Bathrooms'].mode().iloc[0])
    
    # Convert the entire columns to integers (int64)
    df['Bedrooms'] = df['Bedrooms'].astype('Int64')
    df['Bathrooms'] = df['Bathrooms'].astype('Int64')

    # Split currency and price
    df[['Currency', 'Price']] = df['Price'].str.split(n=1, expand=True)

    # Convert 'Price' column to numeric type  
    df['Price'] = df['Price'].str.replace(',', '')
    df['Price'] = df['Price'].replace('[^0-9]+', np.nan, regex=True).astype('Int64')
    df['Price'] = df['Price'].where(df['Price'] >= 1000, np.nan)  # Replace unrealistically low values with NaN

    # Splitting the "Location" column into "Neighborhood" and "Location"
    df[['Neighborhood', 'Location']] = df['Location'].str.rsplit(', ', n=1, expand=True)

    # Make "Neighborhood" and "Location" the same if "Location" is None but "Neighborhood" is not None
    df['Location'] = np.where(df['Location'].isnull() & df['Neighborhood'].notnull(), df['Neighborhood'], df['Location'])

    # Drop rows with missing values in the 'Price' column
    df = df.dropna(subset=['Price'])

    # Drop the 'Neighborhood' column
    df = df.drop(['Neighborhood', 'Status Badge', 'Description', 'Name', 'Currency'], axis=1)

    # Change the column names to title case
    df.columns = df.columns.str.title()

    return df

def lambda_handler(event, context):
    # Initialize s3 client
    client = boto3.client("s3")

    # Retrieve source bucket and csv file path
    source_bucket = "pesh-de-raw-property-data"
    csv_file_path = "raw_data/property_data.csv"

    try:
        response = client.get_object(Bucket=source_bucket, Key=csv_file_path)
        # Create a pandas df
        df = pd.read_csv(io.BytesIO(response["Body"].read()))
        # Transform the dataframe
        transformed_df = transform_data(df)

        # Save to s3 bucket
        transformed_bucket = "pesh-de-cleaned-property-data"
        transformed_file_path = "transformed_data/transformed_data.csv"

        csv_buffer = io.StringIO()
        transformed_df.to_csv(csv_buffer, index=False)
        client.put_object(Bucket=transformed_bucket, Key=transformed_file_path, Body=csv_buffer.getvalue())

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

    return {
        'statusCode': 200,
        'body': "Data transformation and save completed successfully!"
    }

