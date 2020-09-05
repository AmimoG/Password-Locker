from user import *
from credentials import *

def create_account(f_name,m_name,e_mail):
    new_user = User(f_name,m_name,e_mail)
    return new_user
def create_credentials(face_bookp,e_mailp):
    new_cred = Info(face_bookp,e_mailp)
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
    print("")
    print("Hi, WELCOME TO PASSWORD LOCKER!!")
    print(" ")
    print(" ")
    while True:
        print("-" * 156)
        print("""USE THE FOLLOWING SHORT CODES!!
1. cc - CREATE NEW ACCOUNT
2. ex - EXIT PASSWORD LOCKER
3. dac - DISPLAY ACCOUNTS
4. gs - GENERATE PASSWORDS""")