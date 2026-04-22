from tkinter import *
from PIL import ImageTk, Image, ImageSequence
from tkinter import messagebox

root = Tk()
root.title("First Login Window")
root.geometry("500x650")
root.configure(background="brown")

gif = Image.open(r"C:\codesss\spiderman-superhero.gif")
frames = [ImageTk.PhotoImage(frame.resize((300,200))) for frame in ImageSequence.Iterator(gif)]

label = Label(root)
label.pack(pady=(20,20))

def animate(i=0):
    label.config(image=frames[i])
    root.after(100, animate, (i+1) % len(frames))

animate()

text_label = Label(root, text="SPIDER-MAN🕷",fg="black",bg="brown" ,font=("Verdana", 26))
text_label.pack(pady=(10,10))

email_label=Label(root,text="Email",fg="white",bg="brown",font=("verdana",12))
email_label.pack(pady=(20,5))
email_label.config(font=(14))

email_input=Entry(root,width=30,justify="center",font=("verdana",14),fg="red",bg="black",bd=5, relief="groove",insertbackground="red", 
                  insertwidth=2 ,highlightcolor="orange", highlightthickness=4,insertofftime=300, insertontime=300)
email_input.pack(ipady=6,pady=(1,12))

pass_label=Label(root,text="Password",fg="white",bg="brown",font=("verdana",12))
pass_label.pack(pady=(20,5))
pass_label.config(font=(14))

pass_input=Entry(root,width=30,show="*",justify="center",font=("verdana",14),fg="red",bg="black",bd=5, relief="groove",insertbackground="red", 
                  insertwidth=2 ,highlightcolor="orange", highlightthickness=4,insertofftime=300, insertontime=300)
pass_input.pack(ipady=6,pady=(1,12))




root.mainloop() 