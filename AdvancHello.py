#interface Tkinter
from tkinter import *
from tkinter import ttk

class helloApp:
    def __init__(self,master):
        self.label = ttk.Label(master,text ="Hello World!")
        self.label.grid(row=0,column=0,columnspan=2)
        ttk.Button(master, text="Issam",command = self.hello_issam).grid(row=1,column=0)
        ttk.Button(master, text="Life").grid(row=1,column=1)

    def hello_issam(self):
        self.label.configure(text = "Hello!,Issam")

    def hello_life(self):
        self.label.configure(text = "Hello!, Life")

    

def main():
    root = Tk()
    app = helloApp(root)
    root.mainloop()

if __name__=="__main__":main()
    