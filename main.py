from  tkinter import *
from  time import strftime

def time():
    str=strftime("%H : %M : %S %p")
    label.config(text=str)
    label.after(1000,time)

myWindow=Tk()
myWindow.title("Digital Clock")
label=Label(myWindow,font=("ds-digital",80),background="black",foreground="cyan")
label.pack()

time()
mainloop()