from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
executable_path = r'/Users/teacher/Desktop/AutomationCourses/CodeCampCourse2/2.AutomateNews/dist'

# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m-%d-%Y")

web = 'https://www.thesun.co.uk/sport/football/' # introduce path here

# Headless mode
options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to the same folder where the executable will be located
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'news{month_day_year}.csv'
final_path = os.path.join(executable_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()
