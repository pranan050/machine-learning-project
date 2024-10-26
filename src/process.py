import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def process_data_for_model(df):
    """
    Processes the DataFrame for machine learning model training.
    
    Steps:
    - Feature engineering (e.g., duration calculation if possible)
    - Scaling numeric features
    - Encoding categorical features
    - Splitting the data into training and test sets

    Args:
        df (pd.DataFrame): The preprocessed DataFrame.

    Returns:
        X_train, X_test, y_train, y_test: Train and test splits for features and target.
    """

    # Feature Engineering: Calculate duration if both 'creation_time' and 'end_time' columns exist
    if 'creation_time' in df.columns and 'end_time' in df.columns:
        df['creation_time'] = pd.to_datetime(df['creation_time'], errors='coerce')
        df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce')
        df['duration_seconds'] = (df['end_time'] - df['creation_time']).dt.total_seconds()
    else:
        # If the duration column cannot be created, set a placeholder value (e.g., median or fixed value)
        print("Duration calculation skipped: 'creation_time' or 'end_time' column not found.")
        df['duration_seconds'] = 0  # Placeholder value; update this if other relevant information is available

    # Define features and target variable
    features = ['bytes_in', 'bytes_out', 'duration_seconds', 'src_ip_country_code']
    target = 'detection_types'
    
    # Ensure required columns exist
    missing_features = [feature for feature in features if feature not in df.columns]
    if missing_features:
        raise ValueError(f"Missing columns in the dataset: {missing_features}")

    # Select relevant columns
    X = df[features]
    y = (df[target] == 'waf_rule').astype(int)  # Convert target to binary (1 for 'waf_rule', 0 otherwise)
    
    # Define a ColumnTransformer for processing numeric and categorical features
    numeric_features = ['bytes_in', 'bytes_out', 'duration_seconds']
    categorical_features = ['src_ip_country_code']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )
    
    # Create a pipeline that first transforms the data and then applies the preprocessor
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor)
    ])
    
    # Fit and transform the data
    X_processed = pipeline.fit_transform(X)
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test
