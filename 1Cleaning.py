'''This coding block will be used to clean and normalize the raw dataframes Legalization.csv (dfLegalization) and US_Accidents_March23.csv (dfAccidents) 
/ in order to generate the final clean dataset (AccidentsFinal.csv).'''

# Import requisite libraries
import pandas as pd
import os
from dateutil.parser import parse

# Generating variables and loading data into said variables for cleaning of Legalization.csv
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
dfAccidents = pd.read_csv(r'Data\Raw\US_Accidents_March23.csv')
timeParsed = []
dateParsed = []

# Dropping all columns other than ID, Start_Time, Sunrise_Sunset, State from dfAccidents
dfAccidents = dfAccidents[['ID','Start_Time','Sunrise_Sunset','State']]

# Renaming columns in dfAccidents to better identify contained data
dfAccidents = dfAccidents.rename(columns={'Sunrise_Sunset':'Day/Night','Start_Time':'Date'})

# Iterating through Date column within dfAccidents and parsing the date and time, 
# then putting the times (formated hh:mm) into timeParsed and dates (formatted mm/dd/yyyy) into dateParsed
for entry in dfAccidents['Date']:
    parsedEntry = parse(entry) # parsing iterated string into datetime datatype
    timeParsed.append(parsedEntry.strftime('%H:%M'))
    dateParsed.append(parsedEntry.strftime('%m/%d/%Y'))

# Creating a new column in dfAccidents to hold Time value and loading the parsed time data pulled out of the Date column
dfAccidents.insert(loc=2,column='Time',value=timeParsed)

# Replacing the combined date and time value in Date column with the parsed date data only
dfAccidents['Date'] = dateParsed

# Iterating through lists, legalDate and saleDate, created from legalization.csv to remove bracketed data out of each list of dates and appending them to 'Cleaned' list 
# as well as replace null values with the string 'Illegal'
for entry in legalDate:
    if type(entry) == float: # if iterated data is null its type is float 
        entry = 'Illegal' # replacing all float datatypes with 'Illegal'
        legalCleaned.append(str(entry))
    else:
        if type(entry) == str: # if iterated data is a str it is not null
            index = entry.find('[') # finding the first instance of an open bracket in the iterated string
            if index == -1: # if index is '-1' open bracket does not exist in iterated string
                legalCleaned.append(entry) 
            else:
                entry = entry[:index] # slicing off the end of the iterated string at the index value
                legalCleaned.append(entry)

for entry in saleDate:
    if type(entry) == float: # if data is null its type is float 
        entry = 'Illegal' # replacing all float datatypes with 'Illegal'
        saleCleaned.append(entry)
    else:
        if type(entry) == str: # if iterated data is a str it is not null
            index = entry.find('[') # finding the first instance of an open bracket in the iterated string
            if index == -1: # if index is '-1' open bracket does not exist in iterated string
                saleCleaned.append(entry) # append iterated value to designated list
            else:
                entry = entry[:index] # slicing off the end of the iterated string at the index value
                saleCleaned.append(entry) # append iterated value to designated list

# Iterating through 'varCleaned' lists to update date format from 'Month dd, yyyy' to 'mm/dd/yyyy'
for entry in legalCleaned:
    if entry == 'Illegal': # if iterated string == Illegal appending to designated list and moving on
        legalParsed.append(entry)
    else:
        parsedEntry = parse(entry) # if iterated string is anything other than Illegal parsing it into datetime datatype
        legalParsed.append(parsedEntry.strftime('%m/%d/%Y')) # formatting datetime datatype to mm/dd/yyyy

for entry in saleCleaned:
    if entry == 'Illegal': # if iterated string == Illegal appending to designated list and moving on
        saleParsed.append(entry)
    elif entry == 'Never authorized': # if iterated string == Never authorized appending to designated list and moving on
        saleParsed.append(entry)
    elif entry == 'Not yet started': # if iterated string == Not yet started appending to designated list and moving on
        saleParsed.append(entry)
    else:
        parsedEntry = parse(entry) # if iterated string is anything other than previous if/elif statements parsing it into datetime datatype
        saleParsed.append(parsedEntry.strftime('%m/%d/%Y')) # formatting datetime datatype to mm/dd/yyyy and appending it to designated list

# Iterating through column named 'State' in dfLegalization searching for entry in the key value of stateToAbbr list 
# and appending the associated value to stateAbbr
for entry in dfLegalization['State']:
    abbr = stateToAbbr.get(entry) # searching for the iterated string in the keys of dictionary and returning the value to variable
    stateAbbr.append(abbr)

# Replacing original column data from legalization dataframe with cleaned and parsed data 
dfLegalization['Legalization Date'] = legalParsed
dfLegalization['Sale Date'] = saleParsed
# Replacing original state column data from legalization dataframe with abbreviated data for future merging
dfLegalization['State'] = stateAbbr

# Dropping rows with null value in 'Day/Night' column from dfAccidents
dfAccidents.dropna(subset=['Day/Night'],inplace=True)

# Merge dfAccidents and dfLegalization on the State column to make final dataframe. 
dfFinal = pd.merge(dfAccidents,dfLegalization,on='State')

# Exporting dfFinal dataframe to AccidentsFinal.csv and saving in the /Data/Clean files within the current working directory
dfFinal.to_csv(cwd + '/Data/Clean/AccidentsFinal.csv', index=False)