import subprocess
import zipfile
import os

def download_and_unzip_kaggle_dataset(dataset, download_path='datasets/', unzip=True):
    # Define the dataset folder name
    dataset_folder = os.path.join(download_path, dataset.split("/")[-1])
    
    # Check if dataset folder already exists
    if not os.path.exists(dataset_folder):
        print(f"Dataset not found. Downloading {dataset}...")
        
        # Ensure the download path exists
        os.makedirs(download_path, exist_ok=True)
        
        # Download the dataset using Kaggle API
        subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset, '-p', download_path])
        
        # Unzip the dataset if needed
        if unzip:
            zip_file = os.path.join(download_path, dataset.split("/")[-1] + ".zip")
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(dataset_folder)
            print(f"Dataset downloaded and unzipped at {dataset_folder}")
            
            # Optionally, delete the zip file after extraction
            os.remove(zip_file)
        else:
            print(f"Dataset downloaded to {download_path}")
    else:
        print(f"Dataset already exists at {dataset_folder}")

  
