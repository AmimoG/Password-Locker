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
    return Info.display_info()s