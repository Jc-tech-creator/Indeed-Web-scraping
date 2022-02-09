# Indeed-Web-scraping
Some Indeed Web Scraping code of mine as part of my previous internship.
If you are interested in web scraping, especially web scraping, these can be viewed as coding sample to draw useful insights and data from indeed websites.
These Indeed web scraping is achieved using Python. The main function I use is Beautifulsoup and Requests. The coding file is python scripts ending in ‘py.’.
I include my scraping code in IT, Healthcare as well as Finance & insurance indutry here. 
These codes not only do data scraping, but also some data cleaning and transformation to make it better for modeling.
I developed all these codes by myself and it takes me months. Indeed web scraping is somewhat difficult specially the job description parts. Also the html may change each year, so if you have any question, let me know in comments.
Some key points you may need to know: 
1. The data appending mode: ‘mode='a', index=False, header=False’ don’t include any headers, it is used to append new day data without headings. 
2. Give some sleep time to each loop is super important, if the coding crush at some time, try to add more sleep time for each loop, especially the loop changing pages.
3. Q and L are addictive dictionaries, Q is for job titles, L is for location. the scraping result would be combination from those dictionary.If you want to add job titles and location, please add them in these two dictionaries. '%20' is recommended for words seperation, they are not necessary though.
4. Each dataframe is saved to corresponding csv file for instance, if q='data_scientist',l='los_Angeles', the resulting file name would be 'indeed_IT_data_scientist_los_Angeles.csv'.
5. I recommend you run large web scraping file on EC2 with AWS(cloud computing), which I did in that internship.
