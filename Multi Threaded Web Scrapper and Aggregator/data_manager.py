import json
import threading

class DataManager:
    def __init__(self):
        self.data={}
        self.threading_lock=threading.Lock()
       
    def __setitem__(self,key,value):
        with self.threading_lock:
            self.data[key]=value

    def __getitem__(self,key):
        return self.data[key]
    
    def save_to_json(self,filename):
        with self.threading_lock:
            with open(filename,'w',encoding='utf-8') as file:
                json.dump(self.data,file,indent=4,ensure_ascii=False)
            print(f"[DataManager] Data successfully saved to {filename}")


    