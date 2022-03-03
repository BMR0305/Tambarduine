from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
file_path = ''
class GUI:
    def __init__(self, frame):
        self.myFrame = frame

        self.menu_bar = Menu(self.myFrame)
        self.set_menu_bar()

        self.run_bar = Menu(self.menu_bar, tearoff=0)
        self.set_run_bar()

        self.myFrame.config(menu=self.menu_bar)

        self.editor = Text()
        self.editor.pack()

        self.code_output = Text(height=10)
        self.code_output.configure(state="disabled")
        self.code_output.pack()

    def set_file_path(self, path):
        global file_path
        file_path = path

    def open_file(self):
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            self.editor.delete('1.0', END)
            self.editor.insert('1.0', code)
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
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.code_output.insert('1.0', output)
        self.code_output.insert('1.0', error)
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
        self.menu_bar.add_cascade(label='Run', menu=self.run_bar)



