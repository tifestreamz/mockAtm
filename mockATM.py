#Store arrays of names
database = ["Debo", "Jide", "Odun", "Jane"]
transc_type = ["1-Withdrawal", "2-Deposit","3-Complaint"]
current_acct_balance = 0

#bank operations
def bank_Operations():
    print(transc_type)
    selected_transc_type= int(input("What would you like to do today? \n"))
    if selected_transc_type == 1:
        withdraw()
    elif selected_transc_type == 2:
       deposit()
    elif selected_transc_type == 3:
        complain()
    else:
        print("Invalid option selected")
#Register function
def Register():
    reg_Name = input("Enter a prefered username \n")
    #check if username is already taken
    if reg_Name in database:
        print("Username already taken")
        exit()
    else:
        print("Welcome onboard %s" %reg_Name)
        database.append(reg_Name)
        print(database)
        return True


#login
def Login():
    if username in database:
        print("Welcome back " + username)
        return True
    else:
        print("Username not in our database")
        print("Kindly register for an account")
        Register()

#Withdraw
def withdraw():
    amount= int(input("Enter amount \n"))
    acct_balance = current_acct_balance + amount
    print ("Account balance : %d" %acct_balance)

#deposit
def deposit():
    amount= int(input("Enter amount \n"))
    acct_balance = current_acct_balance - amount
    print ("Account balance : %d" %acct_balance)

#complaint
def complain():
    complaint = input("Enter your complaint \n")
    if not complaint:
        print("You've not entered any complaint")
    else:
        print("Your complain is %s" %complaint)
        print("Complaint received, our customer service agent would be in touch with you")

#Take username input from user then login
username = input("Enter your username to log in \n")
Login()
# if Login() == False:
#     Register()
#     if Register() == True:
#         bank_Operations()

bank_Operations()

    