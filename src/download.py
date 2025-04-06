import kagglehub
import zipfile
import os
import shutil

def download_and_unzip_kaggle_dataset(dataset, download_path='datasets/', unzip=True):
    # Define the dataset folder name
    dataset_name = dataset.split("/")[-1]
    dataset_folder = os.path.join(download_path, dataset_name)
    
    # Check if dataset folder already exists
    if not os.path.exists(dataset_folder):
        print(f"Dataset not found. Downloading {dataset}...")
        
        # Ensure the download path exists
        os.makedirs(download_path, exist_ok=True)
        
        try:
            # Use kagglehub to download the dataset
            downloaded_path = kagglehub.dataset_download(dataset)
            print(f"Dataset downloaded to {downloaded_path}")
            
            if unzip:
                # Create the target directory
                os.makedirs(dataset_folder, exist_ok=True)
                
                # If downloaded_path is a directory, copy its contents
                if os.path.isdir(downloaded_path):
                    for item in os.listdir(downloaded_path):
                        src_path = os.path.join(downloaded_path, item)
                        dst_path = os.path.join(dataset_folder, item)
                        if os.path.isdir(src_path):
                            shutil.copytree(src_path, dst_path)
                        else:
                            shutil.copy2(src_path, dst_path)
                    print(f"Dataset moved to {dataset_folder}")
                # If it's a zip file, extract it
                elif downloaded_path.endswith('.zip'):
                    with zipfile.ZipFile(downloaded_path, 'r') as zip_ref:
                        zip_ref.extractall(dataset_folder)
                    print(f"Dataset unzipped to {dataset_folder}")
                else:
                    # Single file, just copy it
                    shutil.copy2(downloaded_path, dataset_folder)
                    
            return dataset_folder
            
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            print("\nTroubleshooting steps:")
            print("1. You may need to log in once with kagglehub: kagglehub.login()")
            print("2. If that doesn't work, check if the dataset is public")
            return None
    else:
        print(f"Dataset already exists at {dataset_folder}")
        return dataset_folder

# Example usage
if __name__ == "__main__":
    dataset = "jancsg/cybersecurity-suspicious-web-threat-interactions"
    result_path = download_and_unzip_kaggle_dataset(dataset)
    if result_path:
        print(f"Dataset is available at: {result_path}")
