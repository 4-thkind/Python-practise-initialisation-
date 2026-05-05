from tkinter import *


root=Tk()
root.title("Calculator")
root.geometry("280x380")
root.configure(bg="black")
root.resizable(0,0)

result_lable=Label(root,text="",bg="black",fg="white")
result_lable.grid(column=0,row=0,pady=(50,25),sticky="w",columnspan=7)
result_lable.configure(font=("verdana",30,"bold"))
