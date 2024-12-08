# Code:You Capstone Project: Data Analysis Pathway
This project intends to analyze traffic accident data throughout the US between 2016 and 2023. It will also look at the affect of marijauna legalization on accidents in those states where it has been made legal in some form. Utilizing the various python scripts in this repository we will acquire our raw data to feed into the cleaning program, clean the data for final review, and finally use the cleaned data to answer several questions and provide visualizations of that data.

### Tools Used

GitBash/Terminal
??Database tool??
This project was conducted using python, focusing on the Pandas library, to generate and clean the data for analysis. Tableau was used for final visualizations. 
Other libraries used throughout the project
 - OS
 - Wikipedia
 - Dateutil.parser

## Start Here

### 1. Clone the repo from GitHub
- Create a new folder to run project in. 
- Clone the repo from GitHub. The link for the repo is https://github.com/WayneBlunden/CapstoneProject.git

### 2. Needed Datafile
Before you can begin running the project you will need to download the **US_Accidents_March23.csv** dataset. **US_Accidents_March23.csv** can be downloaded from [kaggle.com](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents). Download the zip file and save the unzipped file into the /Data/Raw directory created when cloning the repo

### 3. Create a virtual Environment
- Open your Terminal/GitBash and navigate to the directory you cloned the repo to
- Run the below commands to create the virtual environment, install the required libraries, and activate the virtual environment. 

| Step | Description | Code | 
| ---- | ----------- | ---- | 
| 1    | Navigate to the desired folder in gitbash/terminal. Clone the Repo to your machine   |     |
|2     | Create a virtual environment in the project folder. | python3 -m venv venv |
|3     | Activate the virtual environment |  |
|  | Windows: | source venv/Scripts/activate |
|  | Other: | source venv/bin/activate |
| 4    | Install the required packages | pip install -r requirements.txt |
| 5    | When you are done working deactivate the environment | deactivate |



### 4. Data Discovery
Jupyter notebook was utilized to complete the data discovery of US_Accidents_March23.csv. During discovery we reviewed which columns can be used for our analysis based off of the needed datapoints. We checked the format of the data in the columns and looked for any null values.  

### 5. Cleaning Phase
You will run the python script labeled **Cleaning.py**. This script will run through the tasks listed below to generate a final clean data set to use with our visualizations and analysis.
- Load previously made legalization.csv 
- Pull data from 'Legalization Date' and 'Sale Date' columns into individual lists for iteration. This is done to prevent iterating through the dataframe directly. 
    - Remove bracketed numbers located in some dates
    - Replace previous 'null' entries
    - Reformat listed dates into yyyy-mm-dd format to match US_Accidents_March23 dataset's date format
    - Replace original Legalization Date and Sale Date columns with the recently cleaned and formated lists
- Load US_Accidents_March23.csv 
    - Drop extraneous columns

### 4. Analysis ?????

### 5. Visualization

### 6. ?Profit?