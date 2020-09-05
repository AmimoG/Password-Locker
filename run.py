#!/usr/bin/env python3.6
from user import User
from credentials import Info

def create_account(first_name,middle_name,e_mail):
    new_user = User(first_name,middle_name,e_mail)
    return new_user
def create_credentials(linkedInp,e_mailp):
    new_cred = Info(linkedInp,e_mailp)
    return new_cred
def save_account(user):
    user.save_user()
def save_credentials(credentials):
    credentials.save_info()
def display_users():
    return User.display_users()
def display_creds():
    return Info.display_info()
def main():
    print(" ")
    print("Hi Welcom to Password Locker, Please follow the guidelines below.")
    print(" ")
    print(" ")
    while True:
        print("-" * 156)
        print("""Use the bellow short codes to execute what you want!!
1. CA - CREATE ACCOUNT
2. Ex - EXIT PASSWORD LOCKER
3. DA - DISPLAY ACCOUNTS
4. GP - GENERATE PASSWORDS""")


        print(" ")
        print("      Key in the short code you want to execute.")
        print(" ")
        short_code = input() .lower()
        if short_code =='CA':
            print(" ")
            print("-" * 156)
            print("      Create an Account!")
            print(" ")
            print(" ")
            print("what is your first name?..")
            print(" ")
            first_name =input()
            print("What is your middle name?..")
            print(" ")
            middle_name= input()
            print("what is your email address?..")
            print(" ")
            e_mail= input()
            print ("what is your linkedIn password?..")
            print(" ")
            linkedInp =input()
            print("what is your email password?..")
            print(" ")
            e_mailp= input()
            save_account(create_account(first_name,middle_name,e_mail))
            print('\n')
            save_credentials(create_credentials (linkedInp,e_mailp))
            print('\n')
            print("-" * 156)
            print(f"New Account  {first_name } { middle_name} { linkedInp } has been created")
            print('\n')
        elif short_code =='DA':
            if display_users():
                print(" ")
                print("The user name")
                print(" ")
                print('\n')
                for user in display_users():
                    print(f"{user.first_name}{user.middle_name}")
                for credentials in display_creds():
                    print (l"{linkedInp}")
                    print(" ")

            else:
                    print('\n')
                    print("-" * 156)
                    print(" ")
                    print("                         PLEASE CREATE AN ACCOUNT ")
                    print("                    You have not created an account yet :( ")
                    print(" ")
        elif  short_code == 'GP':
            print(" ")
            print(" ")
            print("To Generate a new Password please enter your Name!!")
            print(" ")
            list_of_inputs = [c for c in input()]

            # list_of_inputs= list(list_of_inputs)
            list_of_inputs.reverse()



            print (list_of_inputs)

        elif short_code == "Ex":
            print("-" * 156)
            print(" ")
            print("                        Thank you for creating an account with us!")
            print("                           Have a great time")
            print(" ")
            print("-" * 156)
            break
        else:
            print("-" * 156)
            print(" ")
            print("                              RETRY!!")
            print(" ")
            print("                Please Select One Of The Options Provided")
            print(" ")

if __name__ == '__main__':

    main()
