# 'Code:You' Capstone Project: Data Analysis Pathway
This project intends to analyze traffic accident data throughout the US between 2016 and 2023. It will also look at the affects (if any) of marijauna legalization on accidents in those states where it has been made legal in some form. Utilizing the various python scripts in this repository we will acquire our raw data to feed into the cleaning program, clean the data for final review, and finally analyze the cleaned data to answer several questions and provide visualizations of that data.

## Tools Used

- GitBash/Terminal
- Python (specific libraries below)
    - Pandas
    - OS
    - Wikipedia
    - Dateutil.parser
- Tableau

## Chosen Features from Data Analysis Capstone Features List
#### Loading Data
- Scrape TWO pieces of data from anywhere on the internet and utilize it in your project
    - Scrape two tables from Wikipedia
#### Clean and Operate on the Data While Combining Them
- Clean your data and perform a pandas merge with your two datasets, then calculate some new values based on the new data set
    - Cleaned and merged the two tables scraped from Wikipedia 
    - Cleaned and merged the above data (Legalization.csv) and the read in CSV data (US_Accidents_March23)
#### Visualize/Present Your Data
- Make a Tableau dashboard to display your data
#### Best Practices
- Utilize a virtual environment and include instructions in your README on how the user should set one up
#### Interpretation of Your Data
- Annotate your .py files with well written comments and a clear README.md

<br>
<br>

# To Run the Project Start Here

### 1. Clone the repo from GitHub
- Create a new folder to run project in. 
- Navigate to the newly created plan folder in GitBash/Terminal and clone the repo from GitHub. The link for the repo is https://github.com/WayneBlunden/CapstoneProject.git

### 2. Needed Datafile
Before you can begin running the project you will need to download the **US_Accidents_March23.csv** dataset. This dataset was too large to be included in the repo itself. **US_Accidents_March23.csv** can be downloaded from [kaggle.com](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents). Download the file and save the unzipped file into the /Data/Raw directory created when cloning the repo

### 3. Create a virtual Environment
- Open your Terminal/GitBash and navigate to the directory you cloned the repo to
- Run the below commands to create the virtual environment, install the required libraries, and activate the virtual environment. 

| Step | Description | Code | 
| ---- | ----------- | ---- | 
| 1    | Within GitBash/Terminal, navigate to the desired folder.    |     |
|2     | Create a virtual environment in the project folder. | python3 -m venv venv |
|3     | Activate the virtual environment |  |
|  | Windows: | source venv/Scripts/activate |
|  | Other: | source venv/bin/activate |
| 4    | Install the required packages | pip install -r requirements.txt |
| 5    | When you are done working deactivate the environment | deactivate |

### 4. Run 0LegalizationDataPull.py
This script will scrape two tables from wikipedia, do some basic cleaning to prepare them for merging, merge them, and export the merged table to Legalization.csv. 

### 5. Run 1Cleaning.py
This script will clean Legalization.csv and US_Accidents_March23.csv, merge the two tables, and export them to AccidentsFinal.csv.

<ul>
Note: The US_Accidents_March23.csv dataset is extremely large running this script will take some time. 
</ul>

### 4. Run 2Analysis.py 
This script will analyze AccidentsFinal.csv for visualization.

### 5. Visualization
Tableau was used to visualize the data, you can find the dashboard [here](www.dashboardURL.com)

### 6. ?Profit?