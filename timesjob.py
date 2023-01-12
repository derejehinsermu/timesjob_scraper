from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

print('put some skill that you are unfamiliar with')
#extract the job description based on your skills that are not familiar with you
unfamiliar_skill = input('unfamiliar skills:').split( )

def scrapper():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup

def main_scraper(soup):
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for item in jobs:
        published_date = item.find('span',class_='sim-posted').span.text
        if 'few'in published_date:
            company_name = item.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = item.find('span',class_='srp-skills').text.replace(' ','')
            more_info = item.header.h2.a['href']

            a_match = [True for match in unfamiliar_skill if match in skills]
            if True not in a_match:
                job = {
                'Company Name': company_name.strip(),
                'skills': skills.strip(),
                'More info': more_info

                }
                joblist.append(job)
    return

joblist = []
c = scrapper()
main_scraper(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('Times_job.csv')

