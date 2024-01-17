# Zillow Web Scrapping

Web Scrapping - Beautiful Soup
Technology used: python, beautiful soup, pandas

## Overview
This GitHub repository contains scripts and data related to the extraction and analysis of real estate data from Zillow, focusing on properties in the city of Dallas. The project involves web scraping Zillow's real estate listings using a Python script, cleaning and formatting the extracted data, and finally creating an interactive dashboard using Tableau.

## Project Goals
1. Data Extraction - Build a python script to extract all relevent data from Zillow Website
2. Data Processing: Transform and clean raw data, ensuring it is in the proper format.
3. Data Visualization : Create a fully inactactive dashboard on Tableau to display the results

## Project Components
### 1. Data Extraction Script
  - File Name: get_sale_data.py
  - Description: This Python script is responsible for combing through the HTML of Zillow's real estate listings in Dallas. It extracts housing data from each posting, spanning multiple pages of home listings. Additionally, the script crawls through linked URLs to retrieve additional information. The Beautiful Soup library is employed for effective HTML parsing.
### 2. Data Cleaning Script
  - File Name: data_cleaned.py
  - Description: Following the data extraction, this Python script processes the outputted CSV file (for_sale_data.csv). It performs data cleaning tasks, reformats information, and adds or removes columns as needed. The results are then saved into another CSV file labeled Sales_Data_Cleaned.
### 3. Tableau Dashboard
  - File Name: [Zillow Dallas Real Estate Dashboard](https://public.tableau.com/app/profile/michael.rzadki/viz/ZillowDallasRealEstateDashboard/ZillowDallasRealEstateDashboard#1)
  - Description: The cleaned data from the previous step is uploaded to Tableau, where an interactive dashboard is created. This dashboard provides a user-friendly interface for exploring and visualizing the real estate data extracted from Zillow.

## Instructions
1. Run get_sale_data.py to extract data from Zillow.
2. Execute data_cleaned.py to clean and reformat the extracted data.
3. Upload the cleaned data (Sales_Data_Cleaned.csv) to Tableau.
4. Create and explore the interactive dashboard within Tableau to gain insights into the real estate market in Dallas.

Feel free to customize and adapt the scripts for other cities or additional data points as needed. For any questions or issues, please refer to the documentation or contact the project maintainers.
