from tkinter import *
from functions import *

root=Tk()
root.title("ProjectGurukul Text Editor Python")

savebtn = Button(root, command=lambda: saveDoc(textarea), text="Save")
savebtn.grid(row=1,column=0)
savebtn.config(font=('arial',20,'bold'),bg="DodgerBlue2",fg="white")

fontbtn=Menubutton(root,text="Font")
fontbtn.config(font=('arial',20,'bold'),bg="DodgerBlue2",fg="white")
fontbtn.grid(row=1,column=1)
fontbtn.menu=Menu(fontbtn,tearoff=0)
fontbtn["menu"]=fontbtn.menu

fontbtn.menu.add_checkbutton(label="Arial", command=lambda: Arial(textarea))
fontbtn.menu.add_checkbutton(label="Algerian", command=lambda: Algerian(textarea))
fontbtn.menu.add_checkbutton(label="Cambria", command=lambda: Cambria(textarea))
fontbtn.menu.add_checkbutton(label="Courier", command=lambda: Courier(textarea))

boldbtn=Button(root,command=lambda: boldDoc(textarea), text="Bold")
boldbtn.grid(row=1,column=2)
boldbtn.config(font=('arial',20,'bold'),bg="DodgerBlue2",fg="white")

textarea=Text(root)
textarea.grid(row=2,columnspan=5)

mainloop()
