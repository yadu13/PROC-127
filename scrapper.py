from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium import webdriver 
 

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Webdriver
browser = webdriver.Chrome()  # Initializing Chrome WebDriver
browser.get(START_URL)  # Opening the specified URL in the browser

time.sleep(2)  # Adding a delay to allow the page to fully load

scraped_data = []  # List to store extracted stars data

soup=BeautifulSoup(browser.page_source,"html.parser")

#VERY IMP: The class "wikitable" and <tr> data is at the time of creation of this code. 
# This may be updated in future as the page is maintained by Wikipedia. 
# Understand the page structure as discussed in the class & perform Web Scraping from scratch.

# Find <table>
bright_star_table = soup.find("table", attrs={"class", "wikitable"})
# Find <tbody>
table_body = bright_star_table.find('tbody')
# Find <tr>
table_rows = table_body.find_all('tr')

# Get data from <td>
for row in table_rows:
 table_cols = row.find_all('td')
# print(table_cols)
temp_list = []
for col_data in table_cols:
# Print Only colums textual data using ".text" property
# print(col_data.text)
# Remove Extra white spaces using strip() method
 data = col_data.text.strip()
# print(data)
temp_list.append(data)
# Append data to star data list
stars_data = []
stars_data.append(temp_list)
for i in range(0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]
    required_data = [Star_names, Distance, Mass, Radius, Lum] 
    stars_data.append(required_data)


headers=["Starname","Distance","Mass","Radius","Luminosity"]

stars_df_1=pd.DataFrame(stars_data,columns=headers)

stars_df_1.to_csv("scrapped_data.csv",index=True,index_label=id)
