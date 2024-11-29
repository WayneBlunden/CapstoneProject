import pandas as pd
import wikipedia
import os

# Finding the current working directory and loading it into variable cwd
cwd = os.getcwd()
#print(cwd)

# Using Wikipedia library to get the URLs for the specific pages and loading into designated 'url' variable
urlLegality = wikipedia.page("Legality of cannabis by U.S. jurisdiction").url
urlStates = wikipedia.page("List_of_US_states_by_minimum_wage").url

# Reading webpage table data into designated variables
legalityTables = pd.read_html(urlLegality)
statesTables = pd.read_html(urlStates)
#print(statesTables)

# Reading the wanted tables into designated variables
legality = legalityTables[-9]
states = statesTables[0]
#print(states)

# Creating designated variables and loading it with a dataframe created from the data in designated variables
dfLegality = pd.DataFrame(legality)
dfStates = pd.DataFrame(states)
#print(dfLegality)

# Dropping unwanted columns from both dataframes
dfStates = dfStates[['State']]
dfLegality = dfLegality.drop('Legalization method',axis=1)

# Standardizing column names for future JOIN and Description
dfLegality = dfLegality.rename(columns={'Jurisdiction':'State','Effective date':'Legalization Date','Licensed sales since':'Sale Date'})

# Cleaning of entries into column 'State' for future JOIN 
dfLegality.loc[dfLegality.State == 'Washington (state)','State'] = 'Washington'

# Joining two tables
dfMerged = pd.merge(dfLegality, dfStates,how='right')
#print(dfMerged)



# Export dataframe of imported legalization data to .csv file
dfMerged.to_csv(os.path.join(cwd,'Data\Raw', 'Legalization.csv'),index=False)
#print(dfLegality)



# Removing US territories from dfLegality
#stateCombined = pd.concat([dfLegality['State'],dfStates['State']])
#uniqueValues = stateCombined.unique()




# Making Washington and Washington D.C. designations unique between tables. 
