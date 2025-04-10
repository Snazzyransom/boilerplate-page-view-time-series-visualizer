import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import data and set index to date
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean data: filter out top 2.5% and bottom 2.5% of page views
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]

# 3. Line Plot
def draw_line_plot():
    # Use a copy of the DataFrame
    df_line = df.copy()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot line
    ax.plot(df_line.index, df_line['value'], color='red')
    
    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save and return
    fig.savefig('line_plot.png')
    return fig

# 4. Bar Plot
def draw_bar_plot():
    # Use a copy of the DataFrame
    df_bar = df.copy()
    
    # Group by year and month, calculate mean
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Create figure
    fig = df_bar_grouped.plot(kind='bar', figsize=(12, 6), width=0.8)
    
    # Customize
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    # Save and return
    plt.savefig('bar_plot.png')
    return plt.gcf()

# 5. Box Plots
def draw_box_plot():
    # Use a copy of the DataFrame
    df_box = df.copy()
    
    # Prepare data for year-wise plot
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')  # Short month names
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    # Month-wise box plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save and return
    fig.savefig('box_plot.png')
    return fig