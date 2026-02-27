from queue_manager import URLQueue
from scraper import WebScraper
from data_manager import DataManager
import threading

def main():
    START_URL="https://books.toscrape.com/catalogue/category/books_1/index.html"
    NUM_WORKERS=10
    
    url_queue=URLQueue()
    data_manager=DataManager()

    url_queue.put(START_URL)

    threads=[]

    for _ in range(NUM_WORKERS):
        scraper=WebScraper(queue=url_queue,manager=data_manager)
        scraper.daemon = True
        scraper.start()
        threads.append(scraper)

    url_queue.join()

    data_manager.save_to_json("all_books.json")
    print("All the web scraping is done")


if __name__=="__main__":
    main()