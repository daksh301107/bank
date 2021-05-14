class Atm:
    def __init__(my,accountnumber,pincode):
        my.accountnumber = accountnumber
        my .pincode = pincode

    def checkBalance(my):
        print("Your balance is 310000")

    def withdrawl(self,amount):
        newAmount = 310000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(newAmount))


def main():
    accountNumber = input("insert your account number:- ")
    pincodeNumber  = input("enter your pincode number:- ")

    newUser =  Atm(accountNumber ,pincodeNumber)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        newUser.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        newUser.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
