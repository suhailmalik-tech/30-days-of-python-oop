class Atm:

    def __init__(self):

        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:

            user_input = input(""" 
                    Hello, How would you like to proceed?
                    1.Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
                      
Choose an Option: """)

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid choice, please try again")
    


    def create_pin(self):
        self.pin = input("Enter your pin")
        print("PIN set successfully")


    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            try:

                amount = float(input("Enter the amount: "))
                if amount <= 0:
                    print("Please enter an amount greater than Zero.")
                else:
                    self.balance += amount
                    print("Deposit successful")
            except ValueError:
                print("Invalid input! Please enter a valid numerical amount.")
        else:
            print("Invalid pin")

     

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            try:
                amount = float(input("Enter the amount: "))
                if amount <= 0:
                    print("Please enter an amount greater than Zero.")
                elif amount > self.balance:
                    print("Insufficient balance")
                else:
                    self.balance -= amount
                    print("amount withdrawal successful")
            except ValueError:
                print("Invalid input! Please enter a valid numerical amount.")

        else:
            print("invalid pin")


        


    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your current balance is ${self.balance:.2f}")

        else:
            print("Invalid pin")

        
if __name__ == "__main__":
    Atm()



    



        

