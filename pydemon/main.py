
import os 
import time 
import asyncio
import json
import sys
import subprocess
from sys import executable

class Pydemon():
    def __init__(self,pach=None) -> None:
        self.status = False
        self.running = None
        self.pach = pach
        self.main_filer = None
        self.ignore_filers = None
        self.name_settings = 'pydemon.json'
        self.existing_files = {}
        self.QUEUE_ = asyncio.Queue()
    
    async def print_RED(self,message): print("\033[91m {}\033[00m" .format(message))
    async def print_GREEN(self,message): print("\033[92m {}\033[00m" .format(message))
    
    async def pooling(self):
        while True:
            try:
                data = await self.QUEUE_.get()
                #new freature
                self.running.terminate()
                self.QUEUE_.task_done()
                return
            except Exception as e:
                print(f"[ERROR POOLING] {e}")
                break
            await asyncio.sleep(1)           
            
    
    async def observer(self):
        """
        Observer that analyzes all files within the directory, when a file is created it does not restart or only after the file is modified it restarts
        If you want certain files not to give kittens to trigger the restart function, just add them to ignore inside pydemon.json
        """
        while True:
            if self.status:
                #print("[Observer Online]")
                try:
                    for directory, subfolders, files in os.walk(self.pach):
                        for file_ in files:
                            if file_ not in self.ignore_filers:
                                newDirectory = str(directory+"/"+file_)
                                #fix error // in firs scan
                                newDirectory = newDirectory.replace("//","/")
                                ti_m = os.path.getmtime(newDirectory)
                                modification_date = time.ctime(ti_m)
                                if newDirectory in self.existing_files:
                                    if self.existing_files[newDirectory] != modification_date:
                                        self.existing_files[newDirectory] = modification_date
                                        await self.QUEUE_.put({"file":file_})
                                        #print(f"RESTART OBG ->{file_}")
                                else:
                                    self.existing_files[newDirectory] = modification_date
                except Exception as e:
                    trace_back = sys.exc_info()[2]
                    line = trace_back.tb_lineno
                    print('ERROR Observer {}|{}'.format(line, e))
            await asyncio.sleep(1)
    
    
    async def run_file(self,pach):
        self.running  = subprocess.Popen([executable, pach])
        await self.print_GREEN("[PYDEMON START]")
        
                
    async def main(self):
        task = []
        task.append(asyncio.create_task(self.observer()))
        while True:
            if self.pach != None:
                try:
                    with open(self.pach+'/'+self.name_settings, 'r') as settings:
                        data = json.loads(settings.read())
                        try:
                            self.main_filer = data['pydemon']['main']
                            self.ignore_filers = data['ignore']
                            #restart filer
                            asyncio.create_task(self.run_file(str(self.pach+"/"+self.main_filer)))
                            self.status = True
                            await self.pooling()
                        except Exception as e:
                            print(f'[ERROR] {e} has not been defined')
                except Exception as e:
                    print(f'[ERROR FILER NOT FOUND] as {e}')
                    self.status = False
                    task[0].cancel()
                    break
            else:
                print('[ERROR] Enter the directory where the project is located with pydemon.json.\nExemple pydemon --exec /root/project/')