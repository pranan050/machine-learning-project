import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def process_data_for_model(df):
    """
    Processes the DataFrame for machine learning model training.
    
    Steps:
    - Feature engineering (e.g., duration calculation)
    - Scaling numeric features
    - Encoding categorical features
    - Splitting the data into training and test sets

    Args:
        df (pd.DataFrame): The preprocessed DataFrame.

    Returns:
        X_train, X_test, y_train, y_test: Train and test splits for features and target.
    """

    # Feature Engineering: Calculate duration of the connection in seconds
    df['duration_seconds'] = (df['end_time'] - df['creation_time']).dt.total_seconds()
    
    # Define features and target variable
    features = ['bytes_in', 'bytes_out', 'duration_seconds', 'src_ip_country_code']
    target = 'detection_types'
    
    # Select relevant columns
    X = df[features]
    y = (df[target] == 'waf_rule').astype(int)  # Convert target to binary (1 for 'waf_rule', 0 otherwise)
    
    # Define a ColumnTransformer for processing numeric and categorical features
    numeric_features = ['bytes_in', 'bytes_out', 'duration_seconds']
    categorical_features = ['src_ip_country_code']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

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
