import pandas as pd #imports pandas with pd as an alias
petal = pd.read_csv('Petal_Data.csv') #imports petal data into pandas
sepal = pd.read_csv('Sepal_Data.csv') #importas sepal data into pandas

all_data = pd.merge(petal, sepal, on='sample_id') #merges data based on sample_id

#creates only one species column and drops the duplicate columns
all_data = all_data.rename(columns={'species_x': 'species'})
all_data = all_data.drop(columns=['species_y', 'Unnamed: 0_x', 'Unnamed: 0_y'])

#calculates correlations on columns: sepal length/width and petal length/width
corr_matrix = all_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()

#determies locations of each correlation
sl_sw = corr_matrix.loc['sepal_length', 'sepal_width']
sl_pl = corr_matrix.loc['sepal_length', 'petal_length']
sl_pw = corr_matrix.loc['sepal_length', 'petal_width']
sw_pl = corr_matrix.loc['sepal_width', 'petal_length']
sw_pw = corr_matrix.loc['sepal_width', 'petal_width']
pl_pw = corr_matrix.loc['petal_length', 'petal_width']

#print all correlations nicely
print('Correlations:')
print('1. Sepal Length & Sepal Width:', sl_sw)
print('2. Sepal Length & Petal Width:', sl_pl)
print('3. Sepal Length & Petal Width:', sl_pw)
print('4. Sepal Width & Petal Length:', sw_pl)
print('5. Sepal Width & Petal Width:', sw_pw)
print('6. Petal Length & Petal Width:', pl_pw)

#divides data nicely
print('-------------------------------------------------------')

#identifies columns with numerical values (all variables)
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

#prints mean, median, and standarad deviation nicely
print('Averages by species:')
means_by_species = all_data.groupby('species')[numeric_cols].mean() #groups data based on 'species' and calculates the average of all values
print(means_by_species.to_string()) #prints values as strings
print('----------------------------')
print('Medians by species:')
print(all_data.groupby('species')[numeric_cols].median().to_string()) #groups data based on 'species' and calculates the median of all values
print('----------------------------')
print('Standard deviations by species:')
print(all_data.groupby('species')[numeric_cols].std().to_string()) #groups data based on 'species' and calculates the standard deviation of all values

#Answer to Part 2:
#veriscolor and virginica are the most similar species based on means, medians, and standard deviations

