import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_plots(df):

    save_bytes_histogram(df)
    save_traffic_over_time(df)
    save_detection_types_pie(df)
    save_traffic_by_source(df)
    save_correlation_heatmap(df)
    save_bytes_boxplot(df)
    

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


# Boxplot for Bytes In and Out (New)
def save_bytes_boxplot(df):
    ensure_plots_folder()
    plt.figure(figsize=(10, 6))
    
    sns.boxplot(data=df[['bytes_in', 'bytes_out']], palette="Set3")
    
    plt.title('Boxplot of Bytes In and Bytes Out')
    plt.ylabel('Bytes')
    plt.tight_layout()
    plt.savefig('plots/bytes_boxplot.png')
    plt.close()

# Time Series Plot with Rolling Averages
def save_traffic_with_rolling_avg(df):
    ensure_plots_folder()
    df['time'] = pd.to_datetime(df['time'])
    df['rolling_in'] = df['bytes_in'].rolling(window=60).mean()  # 1-hour window example
    df['rolling_out'] = df['bytes_out'].rolling(window=60).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['bytes_in'], color='blue', alpha=0.5, label='Bytes In')
    plt.plot(df['time'], df['bytes_out'], color='red', alpha=0.5, label='Bytes Out')
    
    # Adding rolling averages
    plt.plot(df['time'], df['rolling_in'], color='blue', label='Rolling Avg Bytes In', linewidth=2)
    plt.plot(df['time'], df['rolling_out'], color='red', label='Rolling Avg Bytes Out', linewidth=2)
    
    plt.title('Traffic Over Time with Rolling Averages')
    plt.xlabel('Time')
    plt.ylabel('Bytes')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/traffic_with_rolling_avg.png')
    plt.close()

# Distribution of Traffic by Source Types
def save_traffic_by_source_type(df):
    ensure_plots_folder()
    traffic_by_type = df.groupby('source.type').agg({'bytes_in': 'sum', 'bytes_out': 'sum'}).reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='source.type', y='bytes_in', data=traffic_by_type, color='blue', label='Bytes In')
    sns.barplot(x='source.type', y='bytes_out', data=traffic_by_type, color='red', label='Bytes Out', bottom=traffic_by_type['bytes_in'])
    
    plt.title('Traffic by Source Type')
    plt.xlabel('Source Type')
    plt.ylabel('Total Bytes')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('plots/traffic_by_source_type.png')
    plt.close()

# Time Series Plot with Anomalies Highlighted
def save_traffic_with_anomalies(df):
    ensure_plots_folder()
    df['time'] = pd.to_datetime(df['time'])

    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['bytes_in'], color='blue', label='Bytes In')
    plt.plot(df['time'], df['bytes_out'], color='red', label='Bytes Out')

    # Assuming 'anomaly' column where 1 = anomaly, 0 = normal
    anomalies = df[df['anomaly'] == 1]
    plt.scatter(anomalies['time'], anomalies['bytes_in'], color='green', label='Anomalies', marker='x', s=100)

    plt.title('Traffic Over Time with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Bytes')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/traffic_with_anomalies.png')
    plt.close()

# Bar Plot of Top 10 Sources by Total Traffic
def save_top_10_sources(df):
    ensure_plots_folder()
    df['total_bytes'] = df['bytes_in'] + df['bytes_out']
    top_10_sources = df.groupby('source.name').agg({'total_bytes': 'sum'}).nlargest(10, 'total_bytes').reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='source.name', y='total_bytes', data=top_10_sources, palette='Blues_d')
    plt.title('Top 10 Sources by Total Traffic')
    plt.xlabel('Source Name')
    plt.ylabel('Total Bytes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/top_10_sources.png')
    plt.close()

# Pairplot for numeric columns
def save_pairplot(df):
    ensure_plots_folder()
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    plt.figure(figsize=(10, 8))
    sns.pairplot(df[numeric_cols], diag_kind='kde')
    plt.suptitle('Pairplot of Numeric Columns', y=1.02)
    plt.savefig('plots/pairplot_numeric_columns.png')
    plt.close()






