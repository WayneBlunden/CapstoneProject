import pandas as pd
import wikipedia
import os

# Finding the current working directory and loading it into variable cwd
cwd = os.getcwd()
#print(cwd)


# Using Wikipedia library to get the URL for the specific page and loading it to variable 'url'
url = wikipedia.page("Legality of cannabis by U.S. jurisdiction").url

# Reading webpage table data into variable 'webpage_tables'
webpage_tables = pd.read_html(url)

# Reading the list of US states and territories where marijuana consumption is legalized into variable 'legality'
legality = webpage_tables[-9]

# Creating a variable, dfLegality, and loading it with a dataframe created from the data in variable 'legality'
dfLegality = pd.DataFrame(legality)

#export dataframe of imported legalization data to .csv file
dfLegality.to_csv(os.path.join(cwd,'Data\Raw', 'Legalization.csv'),index=False)
print(dfLegality)

