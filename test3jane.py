from tkinter import *
root = Tk()
class aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("CenTEC")
        self.root.config(background="blue")
        self.root.geometry("500x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=1000,height=700)
        self.root.minsize(width=100,height=70)
    def frame_da_tela(self):
        self.frame_1 = Frame()
        self.frame_1.place(relx= 0.1, rely= 0.1, relwidth= 0.90, relheight=0.40)

aplication()
