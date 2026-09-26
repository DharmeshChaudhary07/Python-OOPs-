

####################################################### Creating ATM ########################################################


class atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0

    def function(self):
        while True:
            user_input  = input(''' Enter your choice:
                                1. Create Pin
                                2. Check Balance
                                3. Deposit
                                4. Withdraw
                                5. Exit          
                            ''')
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.check_balance()
            elif user_input == '3':
                self.deposit()
            elif user_input == '4':
                self.withdraw()
            elif user_input == '5':
                print("Thank you for banking with us")
                break

    def create_pin(self):
        self.pin = input("Enter you pin:")
        print(f"Pin generated successfully, pin is: {self.pin}")

    def check_balance(self):
        your_pin = input("Enter you pin:")
        if self.pin == your_pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Incorrect pin")

    def deposit(self):
        your_pin = input("Enter you pin:")
        if self.pin == your_pin:
            amount = int(input("Enter amount:"))
            self.balance += amount
            print("Amount deposited successfully")
            print(f"Your updated balance is: {self.balance}")
        else: 
            print("Incorrect pin")

    def withdraw(self):
        your_pin = input("Enter you pin:")
        if self.pin == your_pin:
            amount = int(input("Enter amount to withdraw:"))
            if self.balance >= amount:
                self.balance = self.balance - amount
                print("Amount withdrawn successfully")
                print(f"Updated balance is: {self.balance}")
            else:
                print("Insuffcient balance")
        else: 
            print("Incorrect pin")



atm1 = atm()
atm1.function()


################################################################################################################
'''
1. class atm:  ->  atm is the class — the blueprint.

2. atm1 = atm() -> This creates an object (also called an instance) of the class. atm1 is that object.

3. pin and balance are attributes. Each object gets its own copy. 
     So atm1.pin and atm1.balance hold that specific object's data — if you made atm2 = atm(), it would have its own separate pin and balance, unrelated to atm1's.

4. __init__, function, create_pin, check_balance, deposit, withdraw -> All are method as defined inside a class

5. __init__ ->  It's a special method that runs automatically the moment an object is created
                The instant atm1 = atm() runs, this fires and gives atm1 a blank pin and zero balance to start with

6. self: is reference to the specific object the method is currently running on. 
    It's how deposit() knows to change atm1.balance specifically, not some other atm object's balance.
    You never pass self in yourself — Python does it automatically, based on which object called the method.

'''