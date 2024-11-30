# **Data Dictionary**
This document can be used to review the descriptions of the used columns from various datasets 

### Columns Wanted in Dataset for Analysis
 | Column Name | Column Description | How 
 |---|---|---|
 | Accident Record | ID of accident |  |
 | Street | Name of the street the accident occurred on |  |
 | City | Name of the city the accident occurred in |  |
 | County | Name of the county the accident occurred in |  |
 | State | Name of the state the accident occurred in |  |
 | Zipcode | Zipcode where accident took place |  |
 | Date | Date accident occured |  |
 | Day/Night | Whether the accident occurred during the day or night | Derived from time of accident and recorded sun up sun down times for locality |
 | ?Day of week? | Day of the week accident occured |  |
 | LegalStatus | Whether marijuana use is legal in some form in state |  |
 | LegalizationDate | Date of legalization within state |  |
 | SalesDate | Date when sales were allowed to start |  |

### **US_Accidents_March23.csv**
| Term | Description | Notes |
| ---- | ----------- | --- |
| ID   | Accident Identifier ||
| Severity | Severity of the incident | This datapoint was provided by the original source which didn't clearly define its meaning. Dataset provider can only provide an assumed definintion |
| Start_Time | Date and Time of the accident | Should break this in to two seperate columns for data analysis on individual data points |
| Description | Description of the accident | May be too subjective to be useful |
| Street | Street accident occurred on | Potential comparison column |
| City | City accident occurred in | Potential comparison column |
| County | County accident occurred in | Potential comparison column |
| State | State accident occurred in | Potential comparison column |
| Zipcode | Zipcode accident occurred in | Potential comparison column |