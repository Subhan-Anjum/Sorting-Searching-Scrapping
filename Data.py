import pandas as pd
import funcs
df = pd.read_csv('BOOKS.csv')

Books_Title = df['Title'].values.tolist()
Books_Authors = df['Authors'].values.tolist()
Books_Date = df['Date'].values.tolist()
Books_Publisher = df['Publisher'].values.tolist()
Books_isbn = df['isbn'].values.tolist()
Books_Language = df['Language'].values.tolist()
Books_Waiting_Peoples = df['Waiting Peoples'].values.tolist()

BOOKS=[]
def make2DBooks():
    for i in range(0,len(Books_Title)):
        Temp={'Title':'empty','Authors':'empty','Date':'empty','Publisher':'empty','isbn':12,'Language':'empty','Waiting Peoples':0}
        Temp['Title']=Books_Title[i]
        Temp['Authors']=str(Books_Authors[i])
        Temp['Date']=Books_Date[i]
        Temp['Publisher']=Books_Publisher[i]
        Temp['ISBN']=Books_isbn[i]
        Temp['Language']=Books_Language[i]
        Temp['Waiting Peoples']=Books_Waiting_Peoples[i]
        BOOKS.append(Temp)
    return BOOKS


BOOKS=make2DBooks()


df = pd.read_csv('ARTICLES.csv' )

Articles_Title = df['Title'].values.tolist()
Articles_Authors= df['Authors'].values.tolist()
Articles_Journal_Citations = df['Journal Citations'].values.tolist()
Articles_PMIDs = df['PMIDs'].values.tolist()
Articles_links = df['links'].values.tolist()

ARTICLES=[]
def make2DArticles():
    for i in range(0,len(Articles_Title)):
        Temp={'Title':'empty','Authors':'empty','Journal Citations':'empty','PMIDs':0,'links':'empty'}
        Temp['Title']=Articles_Title[i]
        Temp['Authors']=Articles_Authors[i]
        Temp['Journal Citations']=Articles_Journal_Citations[i]
        Temp['PMIDs']=Articles_PMIDs[i]
        Temp['links']=Articles_links[i]
        ARTICLES.append(Temp)
    return ARTICLES


ARTICLES=make2DArticles()
# ARTICLES=funcs.InsertionSort(ARTICLES,0,len(ARTICLES),'PMIDs')
# for i in range(len(ARTICLES)):
#     print(ARTICLES[i]['PMIDs'])


