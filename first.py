from tkinter import *
root = Tk()
e = Entry(root)

e.pack()

def myClick(number):
    global e
    e.insert(0,number)

#state = DISABLED MEANS not working //  #fg="color text"  // #bg="backgroundColor"
btn = Button(root,text = "Click Me", command=lambda: myClick(5))
btn.pack()

root.mainloop()
