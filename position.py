from tkinter import Tk, BOTH
import tkinter
import tkinter as tk
from tkinter.ttk import Frame, Button, Style, Label
 
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()
 
    def initUI(self):
        self.parent.title("Размещение элементов")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
 
        self.label_1 = tk.Label(self, text="Label_1", bg="orange")
        self.label_2 = tk.Label(self, text="Label_2", bg="yellow")

        self.label_1.place(x=20, y=20, width=150, height=100)
        self.label_2.place(x=120, y=100, width=150, height=100)

        rezButton = Button(self, text="Разместить", command=self.clicked)
        rezButton.place(x=410, y=250, width=80, height=40)

    def clicked(self):
       self.label_2.place(x=110, y=130, width=150, height=100)
        
def main():
    root = tkinter.Tk()
    root.geometry("500x300+700+300")
    root.resizable(False, False)
    Example(root)
    root.mainloop()
 
 
 
if __name__ == '__main__':
    main()
