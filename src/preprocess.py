
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

def preprocess_data(file_path):
    """
    Preprocesses the data by cleaning, transforming, and engineering features.
    
    Args:
    - file_path (str): The file path of the dataset.
    
    Returns:
    - pd.DataFrame: The preprocessed DataFrame.
    """
    # Step 1: Load the dataset
    df = pd.read_csv(file_path)
    
    # Step 2: Data Cleaning
    # Remove duplicates if any
    df = df.drop_duplicates()
    
    # Convert relevant columns to datetime
    df['creation_time'] = pd.to_datetime(df['creation_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['time'] = pd.to_datetime(df['time'])
    
    # Standardize the text column 'src_ip_country_code' to uppercase
    df['src_ip_country_code'] = df['src_ip_country_code'].str.upper()
    
    # Step 3: Feature Engineering
    # Calculate duration of each connection in seconds
    df['duration_seconds'] = (df['end_time'] - df['creation_time']).dt.total_seconds()
    
    # Step 4: Scaling Numerical Features
    scaler = StandardScaler()
    numerical_features = ['bytes_in', 'bytes_out', 'duration_seconds']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    # Step 5: Encoding Categorical Features
    encoder = OneHotEncoder(sparse=False, drop='first')  # Drop first to avoid multicollinearity
    encoded_features = encoder.fit_transform(df[['src_ip_country_code']])
    encoded_feature_names = encoder.get_feature_names_out(['src_ip_country_code'])
    
    # Convert encoded features to a DataFrame and concatenate with the original DataFrame
    encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=df.index)
    df = pd.concat([df, encoded_df], axis=1)
    
    # Step 6: Drop unnecessary columns
    columns_to_drop = ['src_ip', 'dst_ip', 'rule_names', 'observation_name', 'source.meta', 
                       'source.name', 'creation_time', 'end_time', 'time', 'src_ip_country_code']
    df.drop(columns=columns_to_drop, inplace=True)
    
    # Return the preprocessed DataFrame
    return df
