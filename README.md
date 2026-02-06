# Assignment-3-Pandas
# Purpose of the Program
This program is designed to merge and analyze two of Fisher's Iris data sets to better understand species of irises, their traits (sepal length/width and petal length/width), and their relationships. 

# Input
This program is designed to take two .csv files as inputs. One is titled: Sepal_Data.csv and the other is titled: Petal_Data.csv.

# Expected Output
This program is expected to output the following:
1) Correlations between each variable (sepal length, sepal width, petal length, petal width)
2) Averages of each trait for each of the species
3) The median of each trait for each of the species
4) The standard deviations of each trait for each of the species

# Type of Execution
Data loading: loads in multiple data files and merges on sample_id
Data preparation: merges data into a single DataFrame, drops duplicate columns, determines numeric values for statistical analysis
Statistical Analysis: computes summary stats and correlation coefficients
Output and Reporting: Formats output nicely to achieve a readable and organized layout, avoids duplicate or unnecessary information

# Possible Improvements
Code could be made cleaner and more robust by using a function to location each correlation coefficient for a nice output
