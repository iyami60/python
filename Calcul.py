from tkinter import *
from tkinter.messagebox import *


root = Tk()
root.title("Simple Calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0, columnspan=3)
current1 = 0
operateur = ""
result1 = 0
resultat = 0
def Inserr(number):
    global e,current1
    current1 = str(e.get())+str(number)
    e.delete(0,END)
    e.insert(0,current1)

def clear():
    global e,current1,operateur,resultat,result1
    e.delete(0,END)
    current1 = 0
    operateur = ""
    result1 = 0
    resultat = 0

def oper(symbole):
    global result1,operateur
    if symbole =="/":
        operateur = "/"
    if symbole =="+":
        operateur = "+"
    if symbole =="-":
        operateur = "-"
    if symbole =="*":
        operateur = "*"
    result1 = e.get()
    e.delete(0,END)

def alert():
    showinfo("alerte", "Error")
    
def callback():
    if askyesno('Validation', 'Êtes-vous sûr de fermer la fenétre ?'):
        root.destroy()

def equal():
    global current1,result1,resultat
    if operateur =="/":
        if int(e.get()) == 0:
            callback()
        resultat = int(result1)/int(e.get())

    if operateur =="+":
        resultat = int(result1)+int(e.get())
    if operateur =="-":
        resultat = int(result1)-int(e.get())
    if operateur =="*":
        resultat = int(result1)*int(e.get())
    e.delete(0,END)
    e.insert(0,resultat)
    
Button(text="Quitter", command=callback,bg="gray",fg="white",padx=15,relief=GROOVE).grid(row=0,column=3)
btn9 = Button(root,text = "9",padx=30,pady=20,bg="snow4",command=lambda: Inserr(9)).grid(row=2,column=0)
btn8 = Button(root,text = "8",padx=30,pady=20,bg="snow4",command=lambda: Inserr(8)).grid(row=2,column=1)
btn7 = Button(root,text = "7",padx=30,pady=20,bg="snow4",command=lambda: Inserr(7)).grid(row=2,column=2)

btnffff = Button(root,text = "+",padx=30,pady=20,bg="seashell3",command = lambda:oper("+")).grid(row=2,column=3)

btn6 = Button(root,text = "6",padx=30,pady=20,bg="snow4",command=lambda: Inserr(6)).grid(row=3,column=0)
btn5 = Button(root,text = "5",padx=30,pady=20,bg="snow4",command=lambda: Inserr(5)).grid(row=3,column=1)
btn4 = Button(root,text = "4",padx=30,pady=20,bg="snow4",command=lambda: Inserr(4)).grid(row=3,column=2)

btnfff = Button(root,text = "-",padx=30,pady=20,bg="seashell3",command = lambda:oper("-")).grid(row=3,column=3)

btn1 = Button(root,text = "1",padx=30,pady=20,bg="snow4",command=lambda: Inserr(1)).grid(row=4,column=0)
btn2 = Button(root,text = "2",padx=30,pady=20,bg="snow4",command=lambda: Inserr(2)).grid(row=4,column=1)
btn3 = Button(root,text = "3",padx=30,pady=20,bg="snow4",command=lambda: Inserr(3)).grid(row=4,column=2)
btnff= Button(root,text = "/",padx=30,pady=20,bg="seashell3",command = lambda:oper("/")).grid(row=4,column=3)

btn_clear = Button(root,text = "Clear",padx=20,pady=20,bg="seashell3",command=clear).grid(row=5,column=0)

btn0 = Button(root,text = "0",padx=30,pady=20,bg="snow4",command=lambda: Inserr(0)).grid(row=5,column=1)
btnf = Button(root,text = "=",padx=30,pady=20,bg="coral",command =equal).grid(row=5,column=2)
btnh = Button(root,text = "*",padx=30,pady=20,bg="seashell3",command = lambda:oper("*")).grid(row=5,column=3)

root.mainloop()
