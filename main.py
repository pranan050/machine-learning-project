from src.download import download_and_unzip_kaggle_dataset
from src.process import process

def main():

  # Download the Data
  download_and_unzip_kaggle_dataset('jancsg/cybersecurity-suspicious-web-threat-interactions')
  
  # Import and Organize the Data
  df = process('datasets/cybersecurity-suspicious-web-threat-interactions/CloudWatch_Traffic_Web_Attack.csv')
  
  # Visualize the Data
  

if __name__ == '__main__':
  
  main()
