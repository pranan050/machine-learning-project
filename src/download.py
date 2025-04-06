import subprocess
import zipfile
import os
import time

def download_and_unzip_kaggle_dataset(dataset, download_path='datasets/', unzip=True):
    # Parse dataset info
    dataset_owner, dataset_name = dataset.split("/")
    dataset_folder = os.path.join(download_path, dataset_name)
    zip_path = os.path.join(download_path, f"{dataset_name}.zip")
    
    # Check if dataset folder already exists
    if not os.path.exists(dataset_folder):
        print(f"Dataset not found. Attempting to download {dataset}...")
        
        # Ensure the download path exists
        os.makedirs(download_path, exist_ok=True)
        
        # Attempt a direct download using curl without authentication
        # Note: This may not work for all datasets as most require authentication
        download_url = f"https://www.kaggle.com/datasets/download/{dataset_owner}/{dataset_name}"
        
        # Add a user agent to appear like a regular browser
        curl_cmd = [
            'curl', '-L', '-o', zip_path,
            '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            download_url
        ]
        
        print("Executing curl command...")
        result = subprocess.run(curl_cmd, capture_output=True, text=True)
        
        # Check if the download was successful
        if result.returncode != 0 or not os.path.exists(zip_path) or os.path.getsize(zip_path) < 1000:  # Assuming a valid zip is at least 1KB
            print(f"Direct download failed. Error: {result.stderr}")
            print("\nAlternative download methods:")
            print("1. Create a Kaggle account and download manually from: "
                  f"https://www.kaggle.com/datasets/{dataset_owner}/{dataset_name}")
            print("2. Set up Kaggle API credentials: https://www.kaggle.com/docs/api")
            return False
        
        # Unzip the dataset if needed
        if unzip:
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(dataset_folder)
                print(f"Dataset downloaded and unzipped at {dataset_folder}")
                
                # Optionally, delete the zip file after extraction
                os.remove(zip_path)
            except zipfile.BadZipFile:
                print("Downloaded file is not a valid zip file. Authentication might be required.")
                return False
        else:
            print(f"Dataset downloaded to {download_path}")
        
        return True
    else:
        print(f"Dataset already exists at {dataset_folder}")
        return True

# Example usage
if __name__ == "__main__":
    dataset = "jancsg/cybersecurity-suspicious-web-threat-interactions"
    success = download_and_unzip_kaggle_dataset(dataset)
    
    if not success:
        print("\nAlternative approach: You could try downloading using a direct browser download.")
        print("1. Visit the dataset page in your browser")
        print("2. Click the 'Download' button")
        print("3. Save the file and then use the zipfile module to extract it")
