import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import networkx as nx

def create_plots(df):
    """
    Creates multiple visualizations to explore the dataset.
    """
    # Set up visual style
    sns.set(style="whitegrid")
    
    # 1. Plot the distribution of bytes_in and bytes_out
    plot_bytes_distribution(df)
    
    # 2. Correlation heatmap for numeric features
    plot_correlation_heatmap(df)
    
    # 3. Time series plot of bytes_in and bytes_out over time
    plot_time_series(df)
    
    # 4. Network graph of source IP to destination IP
    plot_network_graph(df)

def plot_bytes_distribution(df):
    """
    Plots the distribution of 'bytes_in' and 'bytes_out'.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(df['bytes_in'], bins=30, color='blue', label='Bytes In', kde=True)
    sns.histplot(df['bytes_out'], bins=30, color='red', label='Bytes Out', kde=True)
    plt.title('Distribution of Bytes In and Bytes Out')
    plt.xlabel('Bytes')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def plot_correlation_heatmap(df):
    """
    Plots a heatmap to show the correlation between numeric features.
    """
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_df.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Matrix Heatmap')
    plt.show()

def plot_time_series(df):
    """
    Plots a time series of 'bytes_in' and 'bytes_out' over the 'creation_time'.
    """
    if 'creation_time' not in df.columns:
        print("Time series plot skipped: 'creation_time' column not found in the dataset.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['creation_time'], df['bytes_in'], label='Bytes In', marker='o', linestyle='-')
    plt.plot(df['creation_time'], df['bytes_out'], label='Bytes Out', marker='o', linestyle='-')
    plt.title('Web Traffic Analysis Over Time')
    plt.xlabel('Time')
    plt.ylabel('Bytes')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_network_graph(df):
    """
    Plots a network graph showing interactions between source IPs and destination IPs.
    """
    if 'src_ip' not in df.columns or 'dst_ip' not in df.columns:
        print("Network graph skipped: 'src_ip' or 'dst_ip' columns not found in the dataset.")
        return
    
    G = nx.Graph()

    # Add edges from source IP to destination IP
    for idx, row in df.iterrows():
        G.add_edge(row['src_ip'], row['dst_ip'])

    plt.figure(figsize=(14, 10))
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=8, node_color='skyblue', font_color='darkblue')
    plt.title('Network Interaction between Source and Destination IPs')
    plt.axis('off')  # Turn off the axis
    plt.show()
