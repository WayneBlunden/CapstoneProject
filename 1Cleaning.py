'''This coding block will be used to clean and normalize the raw dataframes in order to generate the final clean dataset.'''

# Import requisite modules
import pandas as pd
import os
from dateutil.parser import parse

# generating variables and loading data into said variables
legalization = pd.read_csv('Data\Raw\Legalization.csv')
legalDate = legalization['Legalization Date']
legalCleaned = []
legalParsed = []
saleDate = legalization['Sale Date']
saleCleaned = []
saleParsed = []

# Iterating through created lists to remove bracketed data out of each list of dates and appending them to 'Cleaned' list as well as replace null values with Illegal
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
        legalParsed.append(parsedEntry.strftime('%Y-%m-%d')) 

for entry in saleCleaned:
    if entry == 'Illegal':
        saleParsed.append(entry)
    elif entry == 'Never authorized':
        saleParsed.append(entry)
    elif entry == 'Not yet started':
        saleParsed.append(entry)
    else:
        parsedEntry = parse(entry)
        saleParsed.append(parsedEntry.strftime('%Y-%m-%d'))

# Replacing original column data from legalization dataframe with cleaned and parsed data 
legalization['Legalization Date'] = legalParsed
legalization['Sale Date'] = saleParsed

print(legalization)








