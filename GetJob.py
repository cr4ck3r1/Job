from bs4 import BeautifulSoup
import requests
import time 

print('Put a skill that you are not familiar with')
print('Babatek Dane ka xot sharazayt le nabe ')
unfamiliar_skill = input(' >>')
print(f'filter {unfamiliar_skill} dakat ...')

def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f'Company Name: {company_name.strip()} \n ')
            print(f'Required Skilles: {skills.strip()} \n ')
            print(f'More Info: {more_info} \n \n \n ')
            with open(f'job{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()} \n ')
                f.write(f'Required Skilles: {skills.strip()} \n')
                f.write(f'More Info: {more_info} \n \n \n ')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_waiting} minutes ...')
        time.sleep(time_wait * 60)