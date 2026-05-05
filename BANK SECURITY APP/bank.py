from tkinter import *
from PIL import ImageTk, Image, ImageSequence
from tkinter import messagebox

class Atm:
    __counter=0
    def __init__(self):
        self.__pin=""
        self.__balance=100000
        self.CARD_NO=Atm.__counter
        Atm.__counter+=1
        self.menu()

    def menu(self):
        val=int(input(''' options:
                1->for create pin
                2->for depositing money
                3->for withdrawing money
                4->checking balance
                5->create new pin
                6->see card number   
                enter your option:'''))
        if val==1:
            self.create_pin()
        elif val==2:
            self.deposit()
        elif val==3:
            self.withdraw()
        elif val==4:
            self.check_balance()
        elif val==5:
            self.set()
        elif val==6:
            self.showPin()
        else:
            print("NOT AND OPTION-->>EXIT")
            
    def check_pin(self):
        if self.__pin=="":
            self.create_pin()
        
        else:
            temp=input("enter the pin:")

            if temp != self.__pin:
                print("wrong pin-->>moving to MENU")
                self.menu()
    
    def create_pin(self):
        self.__pin=input("first time here?????????enter the pin:")
        print("pin setted")
        self.menu()

    def deposit(self):
        self.check_pin()
        amount = int(input("Enter money:"))
        self.__balance +=amount
        print("amount credited")
        self.menu()

    def withdraw(self):
        self.check_pin()
        amount=int(input("Enter money:"))
        if amount<=self.__balance:
            self.__balance-=amount
            print(amount,"debited")
            self.menu()
        else:
            print("SHORT ON MONEY")
            self.menu()

    def check_balance(self):
        self.check_pin()
        print(self.__balance,"is the total amount")
        self.menu()

    def showPin(self):
        self.check_pin()
        print("card number is:",self.CARD_NO)
        self.menu()

#creating GUI
root = Tk()
root.title("First Login Window")
root.geometry("500x750")
root.configure(background="brown")

gif = Image.open(r"/workspaces/Python-practise-initialisation-/BANK SECURITY APP/BANK INTERFACE.gif")
frames = [ImageTk.PhotoImage(frame.resize((250,300))) for frame in ImageSequence.Iterator(gif)]

label = Label(root)
label.pack(pady=(20,20))

def animate(i=0):
    label.config(image=frames[i])
    root.after(50, animate, (i+1) % len(frames))

animate()

text_label = Label(root, text="BANK LOGIN",fg="black",bg="brown" ,font=("Verdana", 26))
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

login_button=Button(root,text="Login",fg="red",bg="black",highlightcolor="orange",highlightthickness=4, command=function)
login_button.pack(ipady=6,ipadx=6,pady=(10,10))
login_button.config(font=('verdana',12))

def function():
    email=email_input.get()
    password=pass_input.get()

    if email=="utkarsh" and password=="123":
        messagebox.showinfo("correct",''' login successful
                                        WELCOME TO THE BANK
                                       PLEASE MOVE TOWARDS TERMINAL''')
        root.withdraw()
        sbi=Atm()
        
    else:
        messagebox.showerror("Wrong","wrong passoword or email")

root.mainloop()