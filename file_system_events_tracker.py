import sys
import time
import random
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Yash Jedhe/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")

    def on_modified(self,event):
        print(f"Hey, {event.src_path} has been modified")

    def on_moved(self,event):
        print(f"Hey, {event.src_path} has been moved")

event_Handler = FileEventHandler()

Observer.schedule(event_Handler, from_dir, recursive=True)

Observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    Observer.stop()        