#!/usr/bin/env python
# coding: utf-8

# In[36]:


import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import datetime
# these are some libraries needed to be installed on ec2 which I believed are already done.
base_link='https://www.indeed.com'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
#user-agent
Q=['Information%20Security%20Analysts','software%20engineer','Computer%20Network%20architects','Database%20Administators','Data%20architect','web%20developer','web%20interface%20designers','operation%20analyst','Data%20Scientist','Business%20Intelligence%20Analysts']
L=['Los%20Angeles','San%20Francisco','Seattle','San%20Jose']
# these are addictive dictionary, Q is for job titles, L is for location. the scraping result would be combination from those dictionary.'%20' is recommended for words seperation, they are not necessary though
for q in Q:#First For Loop
    for l in L:#Second For LOOP
       df=pd.DataFrame(columns=['Title_key','Title','City','Company','Location','Date','Desc'])# columns created for dataframe
       for j in range(0,60,10):##here (0,60,10) means that the scraping will starts from page'start=0' to page'start=60', it exceeds the updated pages of all jobs, No worries,the actual scraping would stop when there is no 'next page'.
         r=requests.get("https://www.indeed.com/jobs?q="+q+"&l="+l+"&radius=0&fromage=1&start={}".format(j),headers=headers)
         # q is elements from dictionary Q, l is elements from dictionary L
         soup=BeautifulSoup(r.text,'html.parser')
         ii=soup.find('tbody',id='resultsBodyContent')
         windows=ii.find_all('a',href=True,id=True)
         # the logic of finding all jobs window is find certain 'T-body', and then find those T-body with 'a'tag and href
         for window in windows: ##for each job window
           href=window['href']
           new_link=base_link + href
           # the key steps to find the job description, since it extract the new link of each job posting
           #title=window.find('h2').text.strip()(the alternative methods to get title)
           titlekey=q.replace("%20"," ")
           titlekey1=q.replace("%20","_")
           city=l.replace("%20"," ")
           city1=l.replace("%20","_")
           company=window.find('span',class_='companyName').text
           #scrape each elements from each job
           location=window.find('div',class_='companyLocation').text
           date=window.find('span',class_='date').text
           r=requests.get(new_link, headers=headers)
           #go to the deeper layer, scrape the new link to get job description
           soup1=BeautifulSoup(r.text,'html.parser')
           title=soup1.find('div',class_='jobsearch-JobInfoHeader-title-container').text
           Desc=soup1.find('div',class_='jobsearch-jobDescriptionText').text.strip()
           df = df.append({'Title_key':titlekey,'Title':title,'City':city,'Company':company,'Location':location,'Date':date,'Desc':Desc},ignore_index=True)
           #append the dataframe
           time.sleep(10)
         time.sleep(20)
         try:
           next_page=soup.find('a',{'aria-label':'Next'})
         except AttributeError:
           break
         ## this above step is to break the whole for loop when reach the end of the all pages, when there is no 'next page'
       df=df.drop_duplicates()
       v=[]
       for i in df['Date']:
         if re.findall(r'[0-9]',i):
           b=''.join(re.findall(r'[0-9]',i))
           #convert string int to int and subtract from today's date and format
           g=(datetime.datetime.today()-datetime.timedelta(int(b))).strftime('%m-%d-%Y')
        
           v.append(g)
         else:
          v.append(datetime.datetime.today().strftime('%m-%d-%Y'))
       #convert to datetime format, and add a date column
       df['Date']=v
       p=[]
       for i in df['Desc']:
         if ('python'in i)or ('Python'in i):
           p1='1'
         else:
          p1='0'
         p.append(p1)
       df['Python']=p
       j=[]
       for i in df['Desc']:
         if ('Java'in i)or ('java'in i):
           j1='1'
         else:
           j1='0'
         j.append(j1)
       df['Java']=j
       s=[]
       for i in df['Desc']:
         if ('SQL'in i)or ('sql'in i):
           s1='1'
         else:
           s1='0'
         s.append(s1)
       df['SQL']=s
       df=df.drop_duplicates()
       df=df.drop_duplicates(subset=['Title','Company','Date'])
       df=df.drop(columns=['Desc'])
       df.to_csv("indeed_IT_"+titlekey1+"_"+city1+".csv", mode='a', index=False, header=False)  
       #this line save the dataframe to the corresponding csvfile for instance, if q='data_scientist',l='los_Angeles', the resulting file name would be 'indeed_data_scientist_los_Angeles.csv' and the new file will beuploaded to s3
       time.sleep(30)
    time.sleep(30)
    #give some sleep time to each loop is super important, if the coding crush at some time, try to add more sleep time for each loop.

