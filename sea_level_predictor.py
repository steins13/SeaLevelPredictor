import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    seaData = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(13, 7))
    plt.scatter(seaData["Year"], seaData["CSIRO Adjusted Sea Level"], label="Sea Level")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(seaData["Year"], seaData["CSIRO Adjusted Sea Level"])

    plt.plot(seaData["Year"].append(pd.Series(np.arange(2014,2051))), (slope * seaData["Year"].append(pd.Series(np.arange(2014,2051)))) + intercept, color="red", label="From 1880")

    # Create second line of best fit
    seaData2 = seaData[seaData["Year"] >= 2000]

    slope, intercept, r_value, p_value, std_err = linregress(seaData2["Year"], seaData2["CSIRO Adjusted Sea Level"])
    plt.plot(seaData2["Year"].append(pd.Series(np.arange(2014,2051))), (slope * seaData2["Year"].append(pd.Series(np.arange(2014,2051)))) + intercept, color="orange", label="From 2000")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()