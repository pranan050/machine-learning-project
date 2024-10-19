import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Ensure the plots folder exists
def ensure_plots_folder():
    if not os.path.exists('plots'):
        os.makedirs('plots')

# 1. Histogram of `bytes_in` and `bytes_out`
def save_bytes_histogram(df):
    ensure_plots_folder()
    plt.figure(figsize=(10, 6))
    sns.histplot(df['bytes_in'], bins=20, color='blue', label='Bytes In', kde=True)
    sns.histplot(df['bytes_out'], bins=20, color='red', label='Bytes Out', kde=True)
    plt.title('Distribution of Bytes In and Bytes Out')
    plt.xlabel('Bytes')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig('plots/bytes_histogram.png')
    plt.close()

# 2. Time Series Plot of Traffic (`bytes_in` and `bytes_out`) Over Time
def save_traffic_over_time(df):
    ensure_plots_folder()
    df['time'] = pd.to_datetime(df['time'])
    plt.figure(figsize=(12, 6))
    
    plt.plot(df['time'], df['bytes_in'], color='blue', label='Bytes In')
    plt.plot(df['time'], df['bytes_out'], color='red', label='Bytes Out')
    
    plt.title('Traffic Over Time (Bytes In and Out)')
    plt.xlabel('Time')
    plt.ylabel('Bytes')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/traffic_over_time.png')
    plt.close()

# 3. Pie Chart of Detection Types
def save_detection_types_pie(df):
    ensure_plots_folder()
    detection_counts = df['detection_types'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(detection_counts, labels=detection_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Detection Types')
    plt.axis('equal')
    plt.savefig('plots/detection_types_pie.png')
    plt.close()

# 4. Bar Plot of Traffic Grouped by Source Name
def save_traffic_by_source(df):
    ensure_plots_folder()
    traffic_by_source = df.groupby('source.name').agg({'bytes_in': 'sum', 'bytes_out': 'sum'}).reset_index()
    
    plt.figure(figsize=(10, 6))
    traffic_by_source.plot(kind='bar', x='source.name', stacked=True, color=['blue', 'red'])
    plt.title('Total Bytes In and Out by Source Name')
    plt.xlabel('Source Name')
    plt.ylabel('Bytes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/traffic_by_source.png')
    plt.close()

# 5. Heatmap of Correlation Between Numeric Columns
def save_correlation_heatmap(df):
    ensure_plots_folder()
    plt.figure(figsize=(8, 6))
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    plt.savefig('plots/correlation_heatmap.png')
    plt.close()
