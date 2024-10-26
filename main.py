from src.download import download_and_unzip_kaggle_dataset
from src.preprocess import preprocess_data
from src.visualize import create_plots
from src.process import process_data_for_model
from src.random_forest import train_random_forest
import pandas as pd

def main():
    # Step 1: Download and unzip the dataset
    download_and_unzip_kaggle_dataset('jancsg/cybersecurity-suspicious-web-threat-interactions')
    
    # Step 2: Preprocess the data
    df = preprocess_data('datasets/cybersecurity-suspicious-web-threat-interactions/CloudWatch_Traffic_Web_Attack.csv')
    
    # Step 3: Visualize the data
    create_plots(df)
    
    # Step 4: Process the data for the ML model
    X_train, X_test, y_train, y_test = process_data_for_model(df)
    
    # Step 5: Train the random forest classifier
    model, accuracy, classification_report = train_random_forest(X_train, X_test, y_train, y_test)
    
    # Step 6: Output the results
    print("Model Accuracy: ", accuracy)
    print("Classification Report:\n", classification_report)

if __name__ == '__main__':
    main()
