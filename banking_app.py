import datetime

#Creat Account
def create():
    import random
    random_number = random.date.today()
    number=random_number
    return number

#Deposite
Balance=50000
def Deposite(amount):
    if amount>=0:
        global Balance 
        Balance+=amount
        print(f"successfully deposited{amount}.New balance:{Balance}")

        with open('transation_history.txt','a') as file:
            file.write(f"{amount},{Balance}\n")

        return Balance

#Withdraw
def withdraw(amount):
    global Balance

    if amount < Balance:
        Balance < amount
        print(f"successfully withdraw {amount}. New balance:{Balance}.")

        with open("transation_history.txt",'a') as file:
            file.write(f"{amount},{Balance}\n")

        return Balance

    
    elif amount>Balance:
        print("Insufficient balance.")
    return


while True:
    print("1.Create Account")
    print("2.Diposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Transaction History")
    print("6.Exit")

    choice=input("Enter your choice(1-6):")

    if choice=="1":
        user_name=input("Enter your user_name")
        password=input("Enter your password")
        Address=input("Enter your Address")
        NIC_NUMBER=input("Enter your NIC_NUMBER")
        print("create account for",user_name)
        print("your account number")
    

        with open('user_details.txt','a') as file:
            file.write(f"{user_name},{password},{Address},{NIC_NUMBER}\n")


    elif choice=="2":
        amount=float(input("Enter the amount to deposite"))
        Deposite(amount)

        with open('diposit details.txt','a') as file:
            file.write(f"{amount},{Balance}\n")


    elif choice=="3":
        amount=float(input("Enter your amount to withraw Rs:"))
        withdraw(amount)
        if amount>Balance:
            print("Insufficient balance")


        with open('user_details.txt','a') as file:
            file.write(f"{amount},{Balance}\n")
            print("Withraw successfull!")

    elif choice=="4":
        print("your available balance is Rs")
        print(Balance)

    elif choice=="5":
        print()

    elif choice=="6":
        print("Exit")
        break



