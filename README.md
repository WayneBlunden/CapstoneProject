# 'Code:You' Capstone Project: Data Analysis Pathway
This project intends to analyze traffic accident data throughout the US between 2016 and 2023. We will be looking at total accidents by state throughout the timeframe and the breakdown of accidents by night or day. It will also look at the affects (if any) of marijauna legalization on Arizona and Illinois. While there are numerous other states that have legalized marijuana these two both were legalized in 2020. They will allow for the largest amount of data on both sides of the legalization date. Utilizing the various python scripts and Jupyter notebooks in this repository we will acquire our raw data to feed into the cleaning program, clean the data for final review, and finally analyze the cleaned data to answer the previously mentioned questions and provide visualizations of that data.

## Tools Used

- GitBash/Terminal
- Python (specific libraries below)
    - Pandas
    - OS
    - Wikipedia
    - Dateutil.parser
    - MatPlotLib
    - Numpy
- Jupyter Notebooks

## Data Dictionary
A data dictionary is stored in the /Data file of the repo. This file defines the variables used throughout the various scripts, their data types and notes of what they are used for. 


## Chosen Features from Data Analysis Capstone Features List
#### Loading Data
- Scrape TWO pieces of data from anywhere on the internet and utilize it in your project
    - Scrape two tables from Wikipedia.
        - A list of minimum wage by state in US 
        - Marijuana legalization by Jurisdiction in the US and territories
- Load a file in
    - Loading in US_Accidents_March23.csv (file details in 'Needed Datafile section below)
#### Clean and Operate on the Data While Combining Them
- Clean data and perform a pandas merge with your two datasets, then calculate some new values based on the new data set
    - Cleaned and merged the two tables scraped from Wikipedia 
    - Cleaned and merged the previously created data (Legalization.csv) and the read in CSV data (US_Accidents_March23.csv)
#### Visualize/Present Your Data
- Make 3 matplotlib or seaborn visualizations to display your data
#### Best Practices
- Utilize a virtual environment and include instructions in your README on how the user should set one up
#### Interpretation of Your Data
- Annotate your .py files with well written comments and a clear README.md

<br>
<br>

# To Run the Project Start Here

## Preliminary Steps
### 1. Clone the repo from GitHub
- Create a new folder to run project in. 
- Navigate to the newly created plan folder in GitBash/Terminal and clone the repo from GitHub. The link for the repo is https://github.com/WayneBlunden/CapstoneProject.git
    - Code used to clone repo -> git clone https://github.com/WayneBlunden/CapstoneProject.git
    Note: You can use 'shift + Insert' to paste into GitHub

### 2. Needed Datafile
The dataset US_Accidents_March23 is too large to upload to GitHub so it is not included in this repo, the unzipped file is 2.84 GB before being cleaned. To run this project you will need to download the US_Accidents_March23.csv dataset. It can be downloaded from [kaggle.com](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents). Download the file and save the unzipped file into the /Data/Raw directory created when cloning the repo before you begin. The remaining dataset used in this project is generated in the project itself.

### 3. Create a virtual Environment
To isolate this project from your computer we will be running it within a virtual environment. Follow the instructions below to create and activate the virtual environment.
- Open your Terminal/GitBash and navigate to the directory you cloned the repo to
- Run the below commands to create the virtual environment, install the required libraries, and activate the virtual environment
- When you have finished running the project you can deactivate the virtual environment 

| Step | Description | Code | 
| ---- | ----------- | ---- | 
| 1    | Within GitBash/Terminal, navigate to the desired folder.    |     |
|2     | Create a virtual environment in the project folder. | python -m venv venv OR python3 -m venv venv |
|3     | Activate the virtual environment |  |
|  | Windows: | source venv/Scripts/activate |
|  | Other: | source venv/bin/activate |
| 4    | Install the required packages | pip install -r requirements.txt |
| 5    | When you are done working deactivate the environment. | deactivate |

## Data Acquisition, Cleaning, and Analysis
### 4. Run 0LegalizationDataPull.py
This script will scrape two tables from wikipedia, do some basic cleaning to prepare them for merging, merge them, and export the merged table to Legalization.csv. 
- If running directly from GitBash/Terminal rather than an IDE, the code used to run this script -> python 0LegalizationDataPull.py OR python3 0LegalizationDataPull.py

### 5. Run 1Cleaning.py
This script will utilize Pandas to remove missing values, standardize formatting for dates and column headings, and parse single date/time data points into separate values for individual columns. It will also merge the separate tables on the 'State' attribute to be used for future analysis. Finally it will output the final table to a .csv file, AccidentsFinal.csv, to be used by 2Analysis.ipynb in visualizations.
- If running directly from GitBash/Terminal rather than an IDE, the code used to run this script -> python 1Cleaning.py OR python3 1Cleaning.py
<ul>
Note: The US_Accidents_March23.csv dataset is extremely large running this script will take some time. 
</ul>

### 4. Run 2Analysis.ipynb
This script will analyze AccidentsFinal.csv for visualization. We will use Matplotlib to visualization the data upon analysis.

Note: AccidentFinal.csv, the file created while running 1Cleaning.py, is 404MB and too large to push to GitHub. Because of this it is not included in the Repo. If you run the project it will generate it but if you would prefer to just view the file it can be seen [here](https://drive.google.com/file/d/1PasKVrLbcio8Z-CqDdhGrDBgXLxK3mHa/view?usp=sharing). 

### 5. Findings
From the visualizations we found that California far outstrips all other states in number of accidents during the tracked time frame, and South Dakota had the fewest number of accidents. Our second visualization shows the larger proportion of accidents occur during the day. We also show that the number of accidents did go down in Illinois and Arizona after marijuana legalization. The assumptions can be made that California has the most accidents due to population and city sizes, and that most accidents happen during the day because that is when the most people are out. But that is all those are, assumptions. It is interesting to see that accident counts went down after marijuana legalization for the two cities listed, but ultimately the dataset is too small to draw any meaningful conclusions. These graphs do provide interesting places to begin future research and analysis projects though. 