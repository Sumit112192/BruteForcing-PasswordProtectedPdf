from pikepdf import Pdf
import sys

def cracking_password(password):
    i=0
    try:
        pdf=Pdf.open('Document-protected.pdf',password)
        sys.stdout.write("\033[K")
        print("[+]-CHECKING-",password)
        print("Password is", password)
        i=1
    except:
        sys.stdout.write("\033[K")
        print("[+]-CHECKING-",password, end="\r")
    if i==1:
        sys.exit(1)

def cracking():
    with open('passwords.txt', 'r') as f:
        for line in f:
            password = line.split('\n')
            cracking_password(password[0])
        

cracking()
