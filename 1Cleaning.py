'''This coding block will be used to clean and normalize the raw dataframes in order to generate the final clean dataset.'''

# Import requisite libraries
import pandas as pd
import os
from dateutil.parser import parse



# Generating variables and loading data into said variables for cleaning of legalization.csv
cwd = os.getcwd()
dfLegalization = pd.read_csv(r'Data\Raw\Legalization.csv')
legalDate = dfLegalization['Legalization Date']
legalCleaned = []
legalParsed = []
saleDate = dfLegalization['Sale Date']
saleCleaned = []
saleParsed = []
stateAbbr = []
stateToAbbr = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "Washington, D.C.": "DC"
}
# Generating variables and loading data for cleaning of US_Accidents_March23.csv
dfAccidents = pd.read_csv(r'Data\Raw\US_Accidents_March23.csv.csv')
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

# Iterating through 'State' in dfLegalization searching for entry in the key value of stateToAbbr list 
# and appending the associated value to stateAbbr
for entry in dfLegalization['State']:
    abbr = stateToAbbr.get(entry)
    stateAbbr.append(abbr)

# Replacing original column data from legalization dataframe with cleaned and parsed data 
dfLegalization['Legalization Date'] = legalParsed
dfLegalization['Sale Date'] = saleParsed
# Replacing original state column data from legalization dataframe with abbreviated data
dfLegalization['State'] = stateAbbr

# Dropping rows with null value in 'Day/Night' column from dfAccidents
dfAccidents.dropna(subset=['Day/Night'],inplace=True)

# Merge dfAccidents and dfLegalization to make final dataframe. 
dfFinal = pd.merge(dfAccidents,dfLegalization,on='State')

dfFinal.to_csv(cwd + '/Data/Clean/AccidentsFinal.csv')
