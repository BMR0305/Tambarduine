from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import GUI

compiler = Tk()
compiler.geometry('800x600')
compiler.title('My Fantastic IDE')
compiler.resizable(False, False)

myGUI = GUI.GUI(compiler)

compiler.mainloop()