'''
This segment of code will pull two tables from Wikipedia and merge them into a single table. The first table will list the marijuana legalization status of US 
    territories. The second table is a list of minimum wage values for all 50 US states and Washington DC. The merged table will display all 50 states and Washington 
    DC, those that have some form of marijuana legalization will have entries designating the Legalization Date and Sale Date (date first legal sales could be made). 
    This table is output to a .csv file [Legalization.csv]. This bit of code also does some quick preliminary cleaning to make exported dataset easier to manage in the 
    'Cleaning' stage. 
'''

import pandas as pd
import wikipedia
import os

# Finding the current working directory and loading it into variable cwd
cwd = os.getcwd()

# Using Wikipedia library to get the URLs for the specific pages and loading into designated 'url' variable
urlLegality = wikipedia.page("Legality of cannabis by U.S. jurisdiction").url
urlStates = wikipedia.page("List_of_US_states_by_minimum_wage").url

# Reading webpage table data into designated variables
legalityTables = pd.read_html(urlLegality)
statesTables = pd.read_html(urlStates)

# Reading the wanted tables into designated variables
legality = legalityTables[-9]
states = statesTables[0]

# Creating designated variables and loading it with a dataframe created from the data in designated variables
dfLegality = pd.DataFrame(legality)
dfStates = pd.DataFrame(states)

# Dropping unwanted columns from both dataframes
dfStates = dfStates[['State']]
dfLegality = dfLegality.drop('Legalization method',axis=1)

# Standardizing column names for future JOIN and Description
dfLegality = dfLegality.rename(columns={'Jurisdiction':'State','Effective date':'Legalization Date','Licensed sales since':'Sale Date'})

# Cleaning of entries into column 'State' for future JOIN 
dfLegality.loc[dfLegality.State == 'Washington (state)','State'] = 'Washington'

# Joining two tables
dfMerged = pd.merge(dfLegality, dfStates,how='right')

# Export dataframe of imported legalization data to .csv file
dfMerged.to_csv(os.path.join(cwd,'Data\Raw', 'Legalization.csv'),index=False)
