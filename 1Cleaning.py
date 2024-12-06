'''This coding block will be used to clean and normalize the raw dataframes in order to generate the final clean dataset.'''

# Import requisite modules
import pandas as pd
import os
from dateutil.parser import parse

# Generating variables and loading data into said variables for cleaning of legalization.csv
dfLegalization = pd.read_csv('Data\Raw\Legalization.csv')
legalDate = dfLegalization['Legalization Date']
legalCleaned = []
legalParsed = []
saleDate = dfLegalization['Sale Date']
saleCleaned = []
saleParsed = []

# Generating variables and loading data for cleaning of US_Accidents_March23.csv
dfAccidents = pd.read_csv(r'Data\Raw\Sampled.csv')
timeParsed = []
dateParsed = []

# Dropping all columns other than ID, Start_Time, Sunrise_Sunset, State
dfAccidents = dfAccidents[['ID','Start_Time','Sunrise_Sunset','State']]

# Renaming columns to better describe what we are using
dfAccidents = dfAccidents.rename(columns={'Sunrise_Sunset':'Day/Night','Start_Time':'Date'})

# Iterating through Date column and parsing the date and time, 
# then putting the times (formated hh:mm) into timeParsed and dates (formatted mm/dd/yyyy) into dateParsed
for entry in dfAccidents['Date']:
    parsedEntry = parse(entry)
    timeParsed.append(parsedEntry.strftime('%H:%M'))
    dateParsed.append(parsedEntry.strftime('%m/%d/%Y'))

# Creating a new column to hold Time value and loading the parsed time data pulled out of the Date column
dfAccidents.insert(loc=2,column='Time',value=timeParsed)

# Replacing the joined date and time value in Date column with the parsed date data only
dfAccidents['Date'] = dateParsed

print(dfAccidents)


# Iterating through lists created from legalization.csv to remove bracketed data out of each list of dates and appending them to 'Cleaned' list 
# as well as replace null values with Illegal
for entry in legalDate:
    if type(entry) == float:
        entry = 'Illegal'
        legalCleaned.append(str(entry))
    else:
        if type(entry) == str:
            index = entry.find('[')
            if index == -1:
                legalCleaned.append(entry)
            else:
                entry = entry[:index]
                legalCleaned.append(entry)

for entry in saleDate:
    if type(entry) == float:
        entry = 'Illegal'
        saleCleaned.append(entry)
    else:
        if type(entry) == str:
            index = entry.find('[')
            if index == -1:
                saleCleaned.append(entry)
            else:
                entry = entry[:index]
                saleCleaned.append(entry)

# Iterating through 'varCleaned' lists to update date format from words to mm/dd/yyyy
for entry in legalCleaned:
    if entry == 'Illegal':
        legalParsed.append(entry)
    else:
        parsedEntry = parse(entry)
        legalParsed.append(parsedEntry.strftime('%m/%d/%Y')) 

for entry in saleCleaned:
    if entry == 'Illegal':
        saleParsed.append(entry)
    elif entry == 'Never authorized':
        saleParsed.append(entry)
    elif entry == 'Not yet started':
        saleParsed.append(entry)
    else:
        parsedEntry = parse(entry)
        saleParsed.append(parsedEntry.strftime('%m/%d/%Y'))

# Replacing original column data from legalization dataframe with cleaned and parsed data 
dfLegalization['Legalization Date'] = legalParsed
dfLegalization['Sale Date'] = saleParsed