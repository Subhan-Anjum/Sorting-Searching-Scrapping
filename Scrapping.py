from asyncio import run
from random import random
from tracemalloc import start
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

article_titles=[]
article_author=[]
Journal_Citations=[]
PMIDs=[]
links = []

runtime = 0

Books=[]
Articles=[]

def Articleprint():
    row =0
    print(Articles)
    self.Scrapping_tableWidget.setColumnCount(5)
    self.setRowCount(len(Articles))
    self.setHorizontalHeaderLabels(["Title","Authors","Journal Citations","PMIDs","links"])
    for article in Articles:
        self.Scrapping_tableWidget.setItem(row,0,self.QTableWidgetItem(str(article['Title'])))
        self.Scrapping_tableWidget.setItem(row,1,self.QTableWidgetItem(str(article['Authors'])))
        self.Scrapping_tableWidget.setItem(row,2,self.QTableWidgetItem(str(article['Journal Citations'])))
        self.Scrapping_tableWidget.setItem(row,3,self.QTableWidgetItem(str(article['PMIDs'])))
        self.Scrapping_tableWidget.setItem(row,4,self.QTableWidgetItem(str(article['links'])))
        row=row+1


def z_OkScrapping():
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

        end_time=time.time()
        runtime = end_time - start_time 
        make2DBooks()
        df = pd.DataFrame(
        {'Title':titles,'Authors':authors,'Date':dates,'Publisher':publishers,'isbn':isbns,'Language':languages,'Waiting Peoples':waiting_peoples})
        df.to_csv('z-okBooks.csv', index=False, encoding='utf-8')
    return True


def MergeScraping(array,start,end):
        start_time=time.time()
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
            end_time=time.time()
            runtime = end_time - start_time 
            return (titles1+titles2,authors1+authors2,dates1+dates2,publishers1+publishers2,isbns1+isbns2,languages1+languages2,waiting_peoples1+waiting_peoples2)

        else :
            titles1="empty"
            authors1="empty"
            dates1="empty"
            publishers1="empty"
            isbns1="empty"
            languages1="empty"
            waiting_peoples1='empty'
            reg=requests.get(str(array[start][0]))
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
            make2DBooks()
            df = pd.DataFrame(
            {'Title':titles,'Authors':authors,'Publication Date':dates,'Publisher':publishers,'isbn':isbns,'Languages':languages,'Waiting Peoples':waiting_peoples  })
            df.to_csv('ArchieveBooks.csv', index=False, encoding='utf-8')
            return (titles1,authors1,dates1,publishers1,isbns1,languages1,waiting_peoples1)       
        
def ArchieveScrapping():
    df = pd.read_csv('archive.csv' )           
    list1 = df.values.tolist()
    (titles,authors,dates,publishers,isbns,languages,waiting_peoples)=MergeScraping(list1,0,len(list1))

def ArticleScrapping():
    df = pd.read_csv('Articleslinks.csv' )           
    ArticlesLinks = df.values.tolist() 

    start_time=time.time()

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
                article_titles.append(temp)
                article_author.append(author.text)
                Journal_Citations.append(Journal_Citation.text)
                PMIDs.append(PMID.text)
                links.append('https://pubmed.ncbi.nlm.nih.gov/'+title.get('href'))

            end_time=time.time()
            runtime = end_time - start_time
            make2DArticles()
            Articleprint()
            df = pd.DataFrame(
            {'Title':article_titles,'Authors':article_author,'Journal Citations':Journal_Citations,'PMIDs':PMIDs,'links':links})
            df.to_csv('ABCDEF.csv', index=False, encoding='utf-8')
         
def make2DBooks():
    for i in range(0,len(titles)):
        Temp={'Title':'empty','Authors':'empty','Date':'empty','Publisher':'empty','isbn':12,'Language':'empty','Waiting Peoples':0}
        Temp['Title']=titles[i]
        Temp['Authors']=str(authors[i])
        Temp['Date']=dates[i]
        Temp['Publisher']=publishers[i]
        Temp['ISBN']=isbns[i]
        Temp['Language']=languages[i]
        Temp['Waiting Peoples']=waiting_peoples[i]
        Books.append(Temp)       
        

def make2DArticles():
    for i in range(0,len(article_titles)):
        Temp={'Title':'empty','Authors':'empty','Journal Citations':'empty','PMIDs':0,'links':'empty'}
        Temp['Title']=article_titles[i]
        Temp['Authors']=article_author[i]
        Temp['Journal Citations']=Journal_Citations[i]
        Temp['PMIDs']=PMIDs[i]
        Temp['links']=links[i]
        Articles.append(Temp)

def scrapping(Text):
    if Text == 'Books':
       if z_OkScrapping() == True:
            ArchieveScrapping()
    elif Text == 'Articles':
        ArticleScrapping()

