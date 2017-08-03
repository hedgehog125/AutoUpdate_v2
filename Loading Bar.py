# Mostly from https://stackoverflow.com/questions/15323574/how-to-connect-a-progress-bar-to-a-function

import tkinter as tk
from tkinter import ttk
import threading
import queue
import time
import urllib, webbrowser

def changeLog():
    webbrowser.open("data:text/html," + urllib.parse.quote("Hello", safe='~()*!.\''))


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Test")
        self.attributes("-topmost", True)
        self.queue = queue.Queue()
        self.listbox = tk.Listbox(self, width=20, height=5)
        self.progressbar = ttk.Progressbar(self, orient='horizontal',
                                           length=300, mode='determinate')
        self.button = tk.Button(self, text="View Changelog", command=changeLog)
        self.spawnthread()
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def spawnthread(self):
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue)
        self.thread.start()
        self.periodiccall()

    def periodiccall(self):
        self.checkqueue()
        self.button.config(state="active")
        if self.thread.is_alive():
            self.after(100, self.periodiccall)

    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.listbox.insert('end', msg)
                self.progressbar.step(1)
            except Queue.Empty:
                pass


class ThreadedClient(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(100):
            time.sleep(0.1)
            msg = "Function %s finished..." % x
            self.queue.put(msg)


if __name__ == "__main__":
    app = App()
    app.mainloop()
