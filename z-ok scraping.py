from random import random
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import random
titles = []
authors = []
dates=[]
publishers=[]
isbns = []
languages=[]
waiting_peoples=[]

start_time=time.time()


for s in range(1,3988):
    if (s%10==0):
            time.sleep(3)
    reg=requests.get("https://b-ok.asia/request.php?s=&order=date&page="+str(s))
    soup = BeautifulSoup(reg.text,"html.parser")

    for a in soup.findAll('div', attrs={'id': 'searchResultBox'}):
        publisher=[]
        title = a.find_all('div', attrs={'class': 'title'})
        author = a.find_all('div', attrs={'class': 'author'})
        temp = a.find_all('div', attrs={'class': 'publisher'})
        for i in temp:
            publisher.append(i.find('a'))
        date = a.find_all('span',attrs={"class":"year"})
        isbn =  a.find_all('span',attrs={"class":"isbn"})
        language= a.find_all("span",attrs={'class':"language text-capitalize"})
        waiting_people=a.find_all("span",attrs={'class':"track_count"})
    isbn=list(dict.fromkeys(isbn))

    for i in range(0,len(title)):
        titles.append(title[i].text)
        authors.append(author[i].text)
        waiting_peoples.append(waiting_people[i].text)


        if(i<len(publisher) and publisher[i]!= None):
            publishers.append(publisher[i].text)
        else:
            publishers.append('empty')

        if(i<len(isbn)and isbn[i]!= None):
            isbns.append(isbn[i].text)
        else:
            isbns.append(random.randint(1111111111111,9999999999999))
        if (i<len(date)and date[i]!= None):
            dates.append(date[i].text)
           
        else :
            dates.append(random.randint(2000,2022))
        if (i<len(language) and language[i]!= None):
            languages.append(language[i].text)
        else:
            languages.append('English')
    print(s)


    df = pd.DataFrame(
    {'Title':titles,'Authors':authors,'Date':dates,'Publisher':publishers,'isbn':isbns,'Language':languages,'Waiting Peoples':waiting_peoples})
    df.to_csv('z-okBooks.csv', index=False, encoding='utf-8')
    
    




end_time=time.time()
runtime=end_time-start_time
print (runtime)

