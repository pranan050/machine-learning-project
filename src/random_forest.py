import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def train_random_forest(X_train, X_test, y_train, y_test):
    """
    Train a Random Forest classifier on the given training data, evaluate it on the test data,
    and return the trained model, accuracy, and classification report.

    Parameters:
    - X_train (DataFrame): Training features.
    - X_test (DataFrame): Test features.
    - y_train (Series): Training labels.
    - y_test (Series): Test labels.

    Returns:
    - model (RandomForestClassifier): The trained Random Forest model.
    - accuracy (float): The accuracy of the model on the test data.
    - classification_report (str): A detailed classification report of the model.
    """
    
    # Initialize the Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    rf_classifier.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = rf_classifier.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    return rf_classifier, accuracy, report

def process_data_for_model(df):
    """
    Preprocess and split the data into training and testing sets for the model.

    Parameters:
    - df (DataFrame): The input dataframe containing the features and target.

    Returns:
    - X_train (DataFrame): Training features.
    - X_test (DataFrame): Test features.
    - y_train (Series): Training labels.
    - y_test (Series): Test labels.
    """
    
    # Feature selection: Extract relevant features
    features = ['bytes_in', 'bytes_out', 'scaled_duration_seconds']  # Modify as needed
    target = 'is_suspicious'
    
    # Extract features and target
    X = df[features]
    y = df[target]
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Feature scaling using StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test
