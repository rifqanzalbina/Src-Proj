from tkinter import filedialog

def saveDoc(textarea):
    text = textarea.get("1.0", "end-1c")
    location = filedialog.asksaveasfilename()
    with open(location, "w+") as file:
        file.write(text)

def boldDoc(textarea):
    textarea.config(font=('arial', 14, 'bold'))

def Algerian(textarea):
    textarea.config(font="Algerian")  

def Arial(textarea):
    textarea.config(font="Arial")  

def Courier(textarea):
    textarea.config(font="Courier")  

def Cambria(textarea):
    textarea.config(font="Cambria")
