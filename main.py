from src.download import download_and_unzip_kaggle_dataset
from src.visualize import create_plots
from src.process import process

def main():

  # Download the Data
  download_and_unzip_kaggle_dataset('jancsg/cybersecurity-suspicious-web-threat-interactions')
  
  # Import and Organize the Data
  df = process('datasets/cybersecurity-suspicious-web-threat-interactions/CloudWatch_Traffic_Web_Attack.csv')
  
  # Visualize the Data
  create_plots(df)
 
  # Splitting the data

  # Training the Models

  # Quantifying Results

  # Visualizing Results
  

if __name__ == '__main__':
  
  main()
