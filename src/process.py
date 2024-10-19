

# Step 1: Read in the data
file_path = 'cybersecurity-suspicious-web-threat-interactions/CloudWatch_Traffic_Web_Attack.csv'
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

# Save cleaned data to a new CSV file
cleaned_file_path = 'cybersecurity-suspicious-web-threat-interactions/Cleaned_CloudWatch_Traffic_Web_Attack.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned data saved to {cleaned_file_path}")

