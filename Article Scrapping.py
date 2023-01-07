from random import random
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import random

titles = []
authors = []
Journal_Citations=[]
PMIDs=[]
links = []
df = pd.read_csv('Articleslinks.csv' )           
ArticlesLinks = df.values.tolist() 

start_time=time.time()
z=0

for i in range(len(ArticlesLinks)):
    URl=ArticlesLinks[i][0]
    for s in range(1,1000):
        if (s%10==0):
            time.sleep(3)
        if s==1:
            reg=requests.get(URl)
        else:
            reg=requests.get(URl+'&page='+str(s))
        soup = BeautifulSoup(reg.text,"html.parser")

        for a in soup.findAll('div', attrs={'class': 'docsum-wrap'}):

            title = a.find('a', attrs={'class': 'docsum-title'})
            author = a.find('span', attrs={'class': 'docsum-authors full-authors'})
            Journal_Citation = a.find('span', attrs={'class': 'docsum-journal-citation full-journal-citation'})
            PMID = a.find('span', attrs={'class': 'docsum-pmid'})

            temp=''
            for i in range(0,len(title.text)):
                if (title.text[i]!=' ' and title.text[i]!='\n'):
                    temp=temp+title.text[i]
            titles.append(temp)
            authors.append(author.text)
            Journal_Citations.append(Journal_Citation.text)
            PMIDs.append(PMID.text)
            links.append('https://pubmed.ncbi.nlm.nih.gov/'+title.get('href'))

        print(z+1)
        z=z+1
        df = pd.DataFrame(
        {'Title':titles,'Authors':authors,'Journal Citations':Journal_Citations,'PMIDs':PMIDs,'links':links})
        df.to_csv('ABCDEF.csv', index=False, encoding='utf-8')
    
    




end_time=time.time()
runtime=end_time-start_time
print (runtime)

