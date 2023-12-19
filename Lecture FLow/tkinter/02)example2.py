import tkinter

sc = tkinter.Tk()
sc.geometry("500x500")
sc.title("My Application")

lbl = tkinter.Label(sc, text="welcome to my application", foreground="blue",font=("arial", 20,"bold"))
lbl.pack(side="top")

def myfun():
    print("Welcome to tkinter")

btn=tkinter.Button(sc, text="click me",font=("arial", 20,"bold"),command=myfun)
btn.place(x=100, y=100)
sc.mainloop()