import random
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
titles = []
authors = []
dates = []
publishers=[]
isbns=[]
languages=[]
waiting_peoples=[]


df = pd.read_csv('archive.csv' )           
list1 = df.values.tolist() 



def MergeScraping(array,start,end):
    if start != end:
        q = (start + end)//2
        titles1 = []
        authors1 = []
        dates1 = []
        publishers1=[]
        isbns1=[]
        languages1=[]
        waiting_peoples1=[]
        titles2 = []
        authors2 = []
        dates2 = []
        publishers2=[]
        isbns2=[]
        languages2=[]
        waiting_peoples2=[]
        (titles1,authors1,dates1,publishers1,isbns1,languages1,waiting_peoples1)=MergeScraping(array, start, q)
        (titles2,authors2,dates2,publishers2,isbns2,languages2,waiting_peoples2)=MergeScraping(array, q + 1, end)
        print (q)
        return (titles1+titles2,authors1+authors2,dates1+dates2,publishers1+publishers2,isbns1+isbns2,languages1+languages2,waiting_peoples1+waiting_peoples2)

    else :
        titles1="empty"
        authors1="empty"
        dates1="empty"
        publishers1="empty"
        isbns1="empty"
        languages1="empty"
        waiting_peoples1='empty'
        reg=requests.get(str(list1[start][0]))
        soup = BeautifulSoup(reg.text,"html.parser")

        for a in soup.findAll('main', attrs={'id': 'maincontent'}):
            title = a.find('span', attrs={'class': 'breaker-breaker'})
            author = a.find('a', attrs={'rel': 'nofollow'})
            date = a.find('span', attrs={'itemprop': 'datePublished'})
            publisher = a.find('span', attrs={'itemprop': 'publisher'})

            if title != None:
                titles1=title.text
            else :
                titles1='empty'
            if author != None:
                authors1=author.text
            else :
                authors1='empty'
            if date != None:
                dates1=date.text
            else :
                dates1='empty'
            if publisher != None:
                publishers1=publisher.text
            else :
                publishers1='empty'



        for a in soup.find_all('dt'):
            temp=''
            if a.text == 'Language':
                language=a.find_next('a', attrs={'rel': 'nofollow'})
                languages1=language.text
        if (languages1 == "empty"):
            languages1="empty"
        isbns1=random.randint(111111111111,999999999999)
        isbns.append(isbns1)
        waiting_peoples1=random.randint(1,3000)
        waiting_peoples.append(waiting_peoples1)
        titles.append(titles1)
        authors.append(authors1)
        dates.append(dates1)
        publishers.append(publishers1)
        languages.append(languages1)
        df = pd.DataFrame(
        {'Title':titles,'Authors':authors,'Publication Date':dates,'Publisher':publishers,'isbn':isbns,'Languages':languages,'Waiting Peoples':waiting_peoples  })
        df.to_csv('ArchieveBooks.csv', index=False, encoding='utf-8')
        return (titles1,authors1,dates1,publishers1,isbns1,languages1,waiting_peoples1)
        
    




start_time=time.time()
(titles,authors,dates,publishers,isbns,languages,waiting_peoples)=MergeScraping(list1,0,len(list1))
end_time=time.time()
runtime=end_time-start_time
print (runtime)

