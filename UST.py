
from tkinter import *
from tkinter import filedialog
import pandas as pd

def openFile():
    filepath = filedialog.askopenfilename ()#(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
     #                                     title="Open file okay?",
      #                                    filetypes= (("text files","*.txt"),
      #                                    ("all files","*.*")))
    #file = open(filepath,'r')
    file = pd.read_csv(filepath)
    print(file)
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()

