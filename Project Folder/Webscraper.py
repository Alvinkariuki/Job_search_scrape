from bs4 import BeautifulSoup
import requests
import json


URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

response = requests.get(URL)

content = BeautifulSoup(response.content, 'html.parser')

results = content.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')


python__jobs = results.find_all(
    'h2', string=lambda text: 'test' in text.lower())

job_with_link = {}
for job_specif in python__jobs:
    link = job_specif.find('a')['href']
    job_listing = {
        job_specif.text.strip(): link
    }
    job_with_link.update(job_listing)

""""
with open('joblinks.json', 'w') as outfile:
    json.dump(job_with_link, outfile)
"""
