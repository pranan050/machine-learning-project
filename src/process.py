import pandas as pd

def process(file_path):
    """
    Reads a CSV file, cleans the data, and saves the cleaned data to a new file.
    
    :param file_path: Path to the input CSV file
    :param cleaned_file_path: Path to save the cleaned CSV file
    """
    # Step 1: Read in the data
    df = pd.read_csv(file_path)

    # Step 2: Display first few rows to check the data
    print("First few rows of the dataset:")
    print(df.head())

    # Step 3: Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Step 4: Clean the data
    # Drop rows with missing values (if any)
    df_cleaned = df.dropna()

    # Remove duplicates (if any)
    df_cleaned = df_cleaned.drop_duplicates()

    # Step 5: Display cleaned data summary
    print("\nCleaned data preview:")
    print(df_cleaned.head())

    return df_cleaned


