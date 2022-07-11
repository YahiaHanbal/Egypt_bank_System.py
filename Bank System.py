#if you wanted to quit the bank_system write quit-exit-close.

class Bank_System:

    #create the account:
    def __init__(self, name, age, city, amount=0):
        self.__name = name
        self.__age = age
        self.__city = city
        self.__amount = amount

    #Show the account:
    def Show_Account(self):
        print('_'*40)
        print(' '*40)
        print(f'Name is: {self.__name}')
        print(f'Age is: {self.__age}')
        print(f'City is: {self.__city}')
        print(f'Amount is: {self.__amount}')
        print('_'*40)
        print(' '*40)
        
    #Cash deposit:
    def Deposit_Money(self, New_amount=0):
        print('_'*40)
        print(' '*40)
        New_amount = input('What is the new amount?')
        try:
            self.__amount = int(New_amount)
            print('Done')
            print('_'*40)
        except:
            print('Please try again and enter the number correct!')
            intro()


    #Cash withdrawal:
    def Withdraw_Money(self, New_amount=0):
        print('_'*40)
        print(' '*40)
        New_amount = input('What is the amount you want?')

        if int(New_amount) >= int(self.__amount):
            print(f"There isn't enough money! You have just in your account :{self.__amount}")
            print('_'*40)
            intro()
        else:
            try:
                self.__amount -= int(New_amount)
                print('Done')
                print('_'*40)
            except:
                print('Please try again and enter the number correct!')
                intro()

# The clients 
Person1 = Bank_System('Yahia M. Hanbal', 15, 'Alexandria')
# The persons or clients need to be added with a function!

def welcome():
    print(' '*40)
    print('^'*40)
    print('Egypt International Bank.')
    print('Welcome to our system!')

    
def intro():
    print('_'*40)
    print('_'*40)
    print(' '*40)
    print('1. Create account!')
    print('2. Show account!')
    print('3. Deposit Money.')
    print('4. Withdraw Money.')
    print('_'*40)
    print('_'*40)
    print(' '*40)
    i = input('What is your choice ?')

    if i in ('1', '1.', 'first'):
        print('Sorry, this featcher is not availiable now!')
    # This need a function to make a new account with new client!

    elif i in ('2', '2.', 'Second'):
        Person1.Show_Account()
        intro()

    elif i in ('3', '3.', 'third'):
        Person1.Deposit_Money()
        intro()

    elif i in ('4', '4.', 'fourth'):
        Person1.Withdraw_Money()
        intro()

    elif i in ('exit', 'quit', 'close'):
        exit()
        
    
    else:
        print(' '*40)
        print("Sorry we didn't understand your choice, please try again!")
        intro()

welcome()
intro()