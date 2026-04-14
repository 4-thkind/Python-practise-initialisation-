class Atm:
    __counter=0#creating a serial number for each
    def __init__(self):
        self.__pin=""
        self.__balance=100000
        #process to get serial number for each object from this class
        self.serial=Atm.__counter
        Atm.__counter+=1
        self.menu()


    def menu(self):
        val=int(input(''' options:
                1->for create pin
                2->for depositing money
                3->for withdrawing money
                4->checking balance
                5->create new pin
                6->exit
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
        else:
            print("NOT AND OPTION-->>EXIT")

    def check_pin(self):
        temp = input("enter pin:")
        if self.__pin=="":
            self.create_pin()
        elif temp != self.__pin:
            print("wrong pin-->>moving to MENU")
            self.menu()
    
    def create_pin(self):
        self.__pin=input("enter the pin:")
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

    def get(self):
        return self.__pin
    
    def set(self):
        self.check_pin()
        new_pin=input("enter new pin:")
        self.__pin=new_pin
        print("new pin setted")
        self.menu()

sbi=Atm()#intialisation/to run

