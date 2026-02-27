from queue import Queue

class URLQueue:
    def __init__(self):
        self.queue=Queue()

    def put(self,url):
        self.queue.put(url)

    def get(self):
        return self.queue.get()
    
    def task_done(self):
        self.queue.task_done()

    def join(self):
        self.queue.join()