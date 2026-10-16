import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] <= df['value'].quantile(.975)) & (df['value'] >= df['value'].quantile(.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(df.index, df['value'], 'r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df1 = df.copy()
    df1['year'] = df1.index.year
    df1['month'] = df1.index.month
    df_bar = df1.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    x = np.arange(len(df_bar.index))
    width = .8 / 12
    month_names = list(calendar.month_name)[1:]
    offsets = (np.arange(12) - (12-1) / 2) * width

    fig, ax = plt.subplots(figsize =(12,6))

    for i, (month_num, month_name) in enumerate(zip(df_bar.columns, month_names)):
        ax.bar(x + offsets[i], df_bar[month_num], width, label=month_name)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_xticks(x)
    ax.set_xticklabels(df_bar.index)
    ax.legend(title='Months', loc = 'upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)


    fig, ax = plt.subplots(1,2, figsize=(12,6))
    sns.boxplot(data = df_box, x='year', y='value', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1], order=month_order)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
