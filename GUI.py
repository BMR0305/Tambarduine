from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from Testing_files import *
import Arduino_code
#tambourine = Arduino_code.momvementController()

file_path = ''
class GUI:
    def __init__(self, frame):
        self.myFrame = frame

        self.menu_bar = Menu(self.myFrame)
        self.set_menu_bar()

        self.run_bar = Menu(self.menu_bar, tearoff=0)
        self.set_run_bar()

        self.myFrame.config(menu=self.menu_bar)

        self.textScrollbar = Scrollbar(self.myFrame)
        self.textScrollbar.pack(side=RIGHT,fill=Y)

        self.linenumber = Text(frame,height=25,width=4,padx=0,state="disabled",takefocus=0, background="grey", wrap="none", yscrollcommand=self.textScrollbar.set)
        self.linenumber.place(x=10,y=10)
        self.editor = Text(frame,wrap="word", undo=True,height=25,width=90,yscrollcommand=self.textScrollbar.set)

        self.editor.bind('<Any-KeyPress>',self.updateLineNumbers)
        self.editor.bind('<Control-a>',self.selectAll)
        self.editor.place(x=50,y=10)

        self.textScrollbar.config(command=self.multipleYView)

        self.code_output = Text(height=10,width=95)
        self.code_output.configure(state="disabled")
        self.code_output.place(x=10,y=420)

    def set_file_path(self, path):
        global file_path
        file_path = path

    def multipleYView(self,*args):
        self.editor.yview(*args)
        self.linenumber.yview(*args)


    def getLineNumbers(self):
        self.output = ""
        self.row, self.col = self.editor.index("end").split(".")
        for i in range(1,int(self.row)):
            self.output += str(i) + '\n'

        return self.output

    def updateLineNumbers(self, event=None):
        self.lineNumber_Bar = self.getLineNumbers()
        self.linenumber.config(state="normal")
        self.linenumber.delete(1.0,END)
        self.linenumber.insert(1.0,self.lineNumber_Bar)
        self.linenumber.config(state="disabled")

    def selectAll(self, event=None):
        self.editor.tag_add(SEL,1.0,END)
        return "break"

    def open_file(self):
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            self.editor.delete('1.0', END)
            self.editor.insert('1.0', code)
            self.updateLineNumbers()
            self.set_file_path(path)


    def save_as(self):
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = self.editor.get('1.0', END)
            file.write(code)
            self.set_file_path(path)

    def run(self):
        self.code_output.configure(state="normal")
        if file_path == '':
            save_prompt = Toplevel()
            text = Label(save_prompt, text='Please save your code')
            text.pack()
            return
        '''command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.code_output.insert('1.0', output)
        self.code_output.insert('1.0', error)'''
        lex_test(file_path)
        if True:  #Cambiar por un if que revise si hay errores
            myprintLog = print_log()
            self.code_output.insert('1.0', myprintLog.value())
            #myTamb = TambInstructions()
            #tambourine.movement_analisis(myTamb.value())
        else:
            print("errores")
            # self.code_output.insert('1.0', ) Pasar los errores

        self.code_output.configure(state="disabled")

    def set_menu_bar(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_command(label='Save', command=self.save_as)
        self.file_menu.add_command(label='Save As', command=self.save_as)
        self.file_menu.add_command(label='Exit', command=exit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

    def set_run_bar(self):
        self.run_bar.add_command(label='Run', command=self.run)
        self.run_bar.add_command(label='Compile', command=self.run)
        #self.menu_bar.add_cascade(label='Run', menu=self.run_bar)



