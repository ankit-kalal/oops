class ATM:

    # static/class variable
    __counter = 1

    def __init__(self):
        # instance variables
        self.__pin = ''
        self.__balance = 0
        self.sno = ATM.__counter

        ATM.__counter = ATM.__counter+1

        self.__menu()

    def __menu(self):

        user_input = input(''' 
Hello , How would you like to proceed ?
1. Enter 1 to create a pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check the balance
5. Enter 5 to exit

''')

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            print("exit")
        else:
            print("Bye")

    @staticmethod
    def get_counter(self):
        return f'{ATM.__counter}'

    @staticmethod
    def set_counter(value):
        ATM.__counter = value
        print("counter changed")

    def get_pin(self):
        return f'{self.__pin}'

    def set_pin(self, value):
        self.__pin = value
        print("Pin changed")

    def create_pin(self):
        self.__pin = input("Enter Your Pin : ")
        print(f'pin created successfully {self.__pin}')

    def deposit(self):
        temp = input("Enter your pin : ")
        if self.__pin == temp:
            amount = int(input("enter amount"))
            self.__balance = self.__balance + amount
        else:
            print("invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin : ")
        if self.__pin == temp:
            amount = int(input("enter amount"))

            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation Successful")
            else:
                print("insufficient fund")

    def check_balance(self):
        temp = input("Enter your pin : ")
        if self.__pin == temp:
            print(self.__balance)
        else:
            print("invalid pin")
