import threading
import requests
from bs4 import BeautifulSoup
import urllib.parse

class WebScraper(threading.Thread):
    def __init__(self,queue,manager):
        super().__init__()
        self.queue=queue
        self.manager=manager
        self.session=requests.Session()

        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})

    def run(self): 
        while True:
            url=None
            try:
                url=self.queue.get()

                if url is None:
                    break

                self.fetch_and_parse(url)
            except Exception as e:
                print(f"Failed to scrape. Reason:{e}")
            finally:
                self.queue.task_done()
    
    def fetch_and_parse(self,url):
        page=self.session.get(url)
        soup=BeautifulSoup(page.text,"html.parser")
        All_book_containers=soup.find_all("article",class_="product_pod") 

        for book in All_book_containers:
            title=book.find("h3").find("a")['title']
            price=book.find("p",class_="price_color").text
            rating=book.find("p",class_="star-rating")['class'][1]

            book_href = book.find("h3").find("a")['href']
            book_url = urllib.parse.urljoin(url, book_href)

            self.manager[book_url]={
                                            'title':title,
                                            'price':price,
                                            'rating':rating
            }
            

       

        next=soup.find("li",class_="next")
        if next:
            url1=next.find("a")['href']
            next_page_url=urllib.parse.urljoin(url,url1)
            self.queue.put(next_page_url)
      
            


                
        

