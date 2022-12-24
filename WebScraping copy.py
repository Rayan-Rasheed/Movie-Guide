from time import sleep
from types import NoneType
from selenium import webdriver 
from bs4 import BeautifulSoup 
import pandas as pd
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe') 
movieNameA=[]
certificateA=[]
durationA=[]
genreA=[]
ratingA=[]
yearA=[]
directorA=[]
actorA=[]
grossA=[]
votesA=[]
start_time=time.time()
link="/search/title/?release_date=1600-01-01,2030-12-31&user_rating=1.0,10.0&num_votes=0,&runtime=0,2000&adult=include&count=250&after=WzkyMjMzNzIwMzY4NTQ3NzU4MDcsInR0NzgwNDUxMCIsODg3MDAxXQ%3D%3D&ref_=adv_nxt"
for i in range(0,100000,251):
    driver.get("https://www.imdb.com/"+link) 
    time.sleep(3)
    file=open(file="link.txt",mode='a')
    file.write(link+'\n')
    content = driver.page_source 
    soup = BeautifulSoup(content)  
    linkNext=soup.find('a',attrs={'class':'lister-page-next next-page'})
    link=linkNext['href']
    Data=soup.find_all('div',attrs={'class':'lister-item mode-advanced'})
    for check in Data:
        m=check.find_all('a')
        name=m[2].text
        movieNameA.append(name) 
        year=check.find('span',attrs={'class':'lister-item-year text-muted unbold'}).text.strip()
        a=""
        for iter in year:
            if iter.isdigit():
                a=a+iter
        yearA.append(a[:4]) 
        certificate=check.find('span',attrs={'class':'certificate'})
        if certificate is not None:
            certificateA.append(certificate.text.strip())
        else:
            certificateA.append("None")   
        durationfull=check.find('span',attrs={'class':'runtime'})
        if durationfull is not None:
            duration=(durationfull.text.strip()).split()[0] #get minutes
            durationA.append(duration)
        else:
            durationA.append("")
        genre=check.find('span',attrs={'class':'genre'})
        if genre is not None:
            genreA.append(genre.text.strip())
        else:
            genreA.append("None")
        rating=check.find('div',attrs={'class':'inline-block ratings-imdb-rating'})
        if rating is not None:  
            ratingA.append(rating.text.strip())
        else:
            ratingA.append("")
        #votes=check.find('span',attrs={'name':'nv'}).text.strip()
        #votesA.append(votes)
        paras=check.find('p', attrs={'class':''}).text.strip()
        directorActor=""
        director=""
        actor=""        
        if(paras!=""):
            if '|' in paras:
                directorActor=paras.split('|')
                director=directorActor[0].split(':')[1].strip()
                a=directorActor[1].split(':')[1].strip()
                actor=''.join(a.splitlines())
            else:
                director=""
                if  len(paras.split(':'))>1:
                 a=paras.split(':')[1].strip()
                 actor=''.join(a.splitlines())
                else:
                    actor=""
            directorA.append(director)
            actorA.append(actor)
        else:
            directorA.append("")
            actorA.append("")
        
        Values=check.find_all('span',attrs={'name':'nv'})
        if(len(Values)>0):
            votes=Values[0]
            votesA.append(votes.text)
            if(len(Values)==1):
                grossA.append("")
            else:
                Gross=Values[1]
                grossA.append(Gross.text) 
        else:
            votesA.append("")
            grossA.append("")
           
        #print(name,year[1:5],duration,genre,rating,director+" :"+actor)
        
    da={'Movie Names':movieNameA,'Certificate':certificateA,'Duration':durationA,'Genre':genreA,'Rating':ratingA,'Years':yearA,'Director':directorA,'Actors':actorA,'Gross':grossA,'Votes':votesA}
    df=pd.DataFrame.from_dict(da)
    df.to_csv('data19.csv',index=False)

end_time=time.time()-start_time
print(end_time)

#Storing Data in a CSV File using Dictionary and the pandas Library

