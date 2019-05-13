
#Import Statements
from bs4 import BeautifulSoup
from csv import writer
from selenium import webdriver
import time

# webpage url
url = 'https://angel.co/incubators'
# opening the chrome browser
browser = webdriver.Chrome()
# browser display specific url
browser.get(url)
# waiting for 10 seconds for the web files(css,images,js,scss,etc)
time.sleep(10)
# storing all html information into html variable 
html = browser.page_source
# Using beautifulSoup library
soup = BeautifulSoup(html, 'html.parser')

# searching and storing all the div's with a 'base name'
companies = soup.findAll(class_="base item")

# creating a new csv file with headers to store the data
with open('companyData.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['CompanyName', 'Location', 'Joined Date','Followers']
    csv_writer.writerow(headers)
    csv_writer.writerow('\n')

    # iterating through companies using foreach loop
    for company in companies:
            # Getting Company Name
            companyName = company.find(class_='name').get_text().replace('\n', '')
            # Geeting Location
            location = company.find(class_='tags').get_text().replace('\n','')
            # Getting Joined Date
            joinedDate = company.find(class_='column joined').find(class_="value").get_text().replace('\n','')
            # Getting followers
            followers = company.find(class_='column followers').find(class_="value").get_text().replace('\n','')
            # Writting every record into csv file
            csv_writer.writerow([companyName, location, joinedDate,followers])




#Additional Code, 'Could have been done this way'

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#from urllib.request import urlopen, Request
#headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) '
#                                    'AppleWebKit/604.1.38 (KHTML, like Gecko) '
#                                    'Version/11.0 Mobile/15A372 Safari/604.1',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'en-US,en;q=0.8',
#        'Connection': 'keep-alive'}
#reg_url = 'https://angel.co/incubators'
#req = Request(url=reg_url, headers=headers) 
#html = urlopen(req).read()
#soup = BeautifulSoup(html, 'html.parser') 
#print(soup) 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!