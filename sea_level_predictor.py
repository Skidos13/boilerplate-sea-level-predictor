import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    
    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linear_regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x=range(1880,2051)

    y = [linear_regression.slope * i + linear_regression.intercept for i in x]
    plt.plot(x, y, 'r')

    # Create second line of best fit
     # Create second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    linear_regression_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = range(2000, 2051)
    y_recent = [linear_regression_recent.slope * i + linear_regression_recent.intercept for i in x_recent]
    plt.plot(x_recent, y_recent, 'g', label='Best fit line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()