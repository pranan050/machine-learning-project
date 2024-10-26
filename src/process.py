import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(file_path):
    # Step 1: Load the dataset
    df = pd.read_csv(file_path)
    
    # Step 2: Remove duplicate rows
    df = df.drop_duplicates()
    
    # Step 3: Convert time-related columns to datetime format
    df['creation_time'] = pd.to_datetime(df['creation_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['time'] = pd.to_datetime(df['time'])
    
    # Step 4: Standardize text data (e.g., ensure country codes are uppercase)
    df['src_ip_country_code'] = df['src_ip_country_code'].str.upper()
    
    # Step 5: Feature engineering - Calculate duration of connection
    df['duration_seconds'] = (df['end_time'] - df['creation_time']).dt.total_seconds()
    
    # Step 6: Scaling numeric features
    scaler = StandardScaler()
    numeric_features = ['bytes_in', 'bytes_out', 'duration_seconds']
    df[numeric_features] = scaler.fit_transform(df[numeric_features])
    
    # Step 7: One-Hot Encoding for categorical data (e.g., src_ip_country_code)
    encoder = OneHotEncoder(sparse=False)
    encoded_features = encoder.fit_transform(df[['src_ip_country_code']])
    encoded_columns = encoder.get_feature_names_out(['src_ip_country_code'])
    encoded_df = pd.DataFrame(encoded_features, columns=encoded_columns, index=df.index)
    
    # Step 8: Concatenate encoded features back into the original dataframe
    df = pd.concat([df, encoded_df], axis=1)
    
    # Step 9: Drop original columns that are no longer needed (e.g., src_ip_country_code)
    df = df.drop(columns=['src_ip_country_code', 'end_time'])  # Drop columns as needed
    
    # Return the preprocessed DataFrame
    return df
