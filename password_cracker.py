from pikepdf import Pdf
import sys

def cracking_password(password):
    i=0
    try:
        pdf=Pdf.open('PDF.pdf',password)
        print("Password is "+(password))
        i=1
    except:
        print("[+]-CHECKING-",password)

    if i==1:
        sys.exit()

def cracking():
    file = open('passwords.txt','r')
    for line in file.readlines():
        password = line.split('\n')
        cracking_password(password[0])

cracking()
