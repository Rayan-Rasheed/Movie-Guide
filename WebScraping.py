from time import sleep
from types import NoneType
from selenium import webdriver 
from bs4 import BeautifulSoup 
import pandas as pd
import time
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
# def WebScraping(totalTime,running):
#     driver = webdriver.Chrome(executable_path='chromedriver.exe') 
    
#     start_time=time.time()
#     file=open(file="link.txt",mode='r')
#     link=file.readline()
#     file.close()
#     #link="/search/title/?country_of_origin=IN&after=WzE5ODQ2NDYsInR0MDI1NjQzOSIsNzU0MDFd&ref_=adv_nxt"

#     while(running):
        
#         driver.get("https://www.imdb.com/"+link) 
#         time.sleep(3)
#         file=open(file="link.txt",mode='w')
#         file.write(link+'\n')
#         content = driver.page_source 
#         soup = BeautifulSoup(content)  
#         linkNext=soup.find('a',attrs={'class':'lister-page-next next-page'})
#         link=linkNext['href']
#         Data=soup.find_all('div',attrs={'class':'lister-item mode-advanced'})
#         for check in Data:
#             name=check.h3.a.text
#             movieNameA.append(name) 
#             year=check.find('span',attrs={'class':'lister-item-year'}).text.strip()
#             a=""
#             for iter in year:
#                 if iter.isdigit():
#                     a=a+iter
#             yearA.append(a[:4]) 
#             certificate=check.find('span',attrs={'class':'certificate'})
#             if certificate is not None:
#                 certificateA.append(certificate.text.strip())
#             else:
#                 certificateA.append("None")   
#             durationfull=check.find('span',attrs={'class':'runtime'})
#             if durationfull is not None:
#                 duration=(durationfull.text.strip()).split()[0] #get minutes
#                 durationA.append(duration)
#             else:
#                 durationA.append("")
#             genre=check.find('span',attrs={'class':'genre'})
#             if genre is not None:
#                 genreA.append(genre.text.strip())
#             else:
#                 genreA.append("None")
#             rating=check.find('div',attrs={'class':'inline-block ratings-imdb-rating'})
#             if rating is not None:  
#                 ratingA.append(rating.text.strip())
#             else:
#                 ratingA.append("")
#             #votes=check.find('span',attrs={'name':'nv'}).text.strip()
#             #votesA.append(votes)
#             paras=check.find('p', attrs={'class':''}).text.strip()
#             directorActor=""
#             director=""
#             actor=""        
#             if(paras!=""):
#                 if '|' in paras:
#                     directorActor=paras.split('|')
#                     director=directorActor[0].split(':')[1].strip()
#                     a=directorActor[1].split(':')[1].strip()
#                     actor=''.join(a.splitlines())
#                 else:
#                     director=""
#                     if  len(paras.split(':'))>1:
#                         a=paras.split(':')[1].strip()
#                         actor=''.join(a.splitlines())
#                     else:
#                         actor=""
#                 directorA.append(director)
#                 actorA.append(actor)
#             else:
#                 directorA.append("")
#                 actorA.append("")
            
#             Values=check.find_all('span',attrs={'name':'nv'})
#             if(len(Values)>0):
#                 votes=Values[0]
#                 votesA.append(votes.text)
#                 if(len(Values)==1):
#                     grossA.append("")
#                 else:
#                     Gross=Values[1]
#                     grossA.append(Gross.text) 
#             else:
#                 votesA.append("")
#                 grossA.append("")
            
#             #print(name,year[1:5],duration,genre,rating,director+" :"+actor)
            
#         da={'Movie Names':movieNameA,'Certificate':certificateA,'Duration':durationA,'Genre':genreA,'Rating':ratingA,'Years':yearA,'Director':directorA,'Actors':actorA,'Gross':grossA,'Votes':votesA}
#         df=pd.DataFrame.from_dict(da)
#         end_time=time.time()-start_time
#         totalTime +=end_time
#         return (df,totalTime)
#         #df.to_csv('data24.csv',index=False)

    


