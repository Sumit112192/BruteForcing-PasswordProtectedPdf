from pikepdf import Pdf
import sys

def cracking_password(password):
    try:
        pdf=Pdf.open('PDF.pdf',password)
        print("Password is "+(password))
        sys.exit()
    except:
        print("[+]-CHECKING-",password)
        

def cracking():
    file = open('passwords.txt','r')
    for line in file.readlines():
        password = line.split('\n')
        cracking_password(password[0])

cracking()
