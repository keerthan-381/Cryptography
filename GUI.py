from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("CRYPTOGRAPHY")
root.geometry("500x300")
def home():
    f1=Frame(background='yellow')
    f1.place(x=0,y=0,width=500,height=300)
    u=Label(f1,text="WELCOME",font=("Helvetica",20))
    u.config(background='yellow',foreground="red")
    u.place(x=175,y=50)
    u1=Label(f1,text="!!Encrypting & Decrypting!!",font=("Helvetica",20))
    u1.config(background='yellow',foreground="red")
    u1.place(x=100,y=125)
    b1=Button(f1,text="Encryption",command=encrypting, fg="red", activebackground = "grey")
    b1.place(x=120,y=200,width=100,height=40)
    b2=Button(f1,text="Decryption",command=decrypting, fg="red", activebackground = "grey")
    b2.place(x=280,y=200,width=100,height=40)
def encrypting():
    def Encryption():
        plaintext = r1.get()
        key = int(r2.get())
        ciphertext = ""
        for i in range(0,len(plaintext)):
            if plaintext[i].isalpha():
                ciphertext += chr((ord(plaintext[i]) + key - 65) % 26 + 65)
            else:
                ciphertext += plaintext[i]
        #messagebox.showinfo(title="", message="The Ciphertext generated is:" '\n' '%s \n ' %(ciphertext))
        r3.insert(0, ciphertext)
    f2=Frame(background='orange')
    f2.place(x=0,y=0,width=500,height=300)
    u=Label(f2,text="!!ENCRYPTION!!",font=("Helvetica",20))
    u.config(background='orange',foreground="black")
    u.place(x=110,y=20)
    u1=Label(f2, text="Plaintext", font=("Helvetica",14))
    u1.place(x=100,y=80)
    r1=Entry(f2, width=50, font=("Quintessential",14))
    r1.place(x=225,y=80,width=120)
    u2=Label(f2, text="Key", font=("Helvetica",14))
    u2.place(x=100,y=130)
    r2=Entry(f2, width=50, font=("Quintessential",14))
    r2.place(x=225,y=130,width=120)
    u3=Label(f2, text="Ciphertext", font=("Helvetica",14))
    u3.config(background='yellow',foreground="black")
    u3.place(x=100,y=180)
    r3=Entry(f2, width=50, font=("Quintessential",14))
    r3.config(background='yellow',foreground="black")
    r3.place(x=225,y=180,width=120)
    b2=Button(f2,text="<-",command=home)
    b2.place(x=0,y=0,width=20,height=20)
    b3=Button(f2,text="Encrypt",command=Encryption)
    b3.place(x=200,y=230,width=100,height=40)
def decrypting():
    def Decryption():
        ciphertext = r1.get()
        key = int(r2.get())
        plaintext = ""
        for i in range(0,len(ciphertext)):
            if ciphertext[i].isalpha():
                plaintext += chr((ord(ciphertext[i]) - key - 65) % 26 + 65)
            else:
                plaintext += ciphertext[i]
        #messagebox.showinfo(title="", message="The Plaintext generated is:" '\n' '%s \n ' %(ciphertext))
        r3.insert(0, plaintext)
    f3=Frame(background='aqua')
    f3.place(x=0,y=0,width=500,height=300)
    u=Label(f3,text="!!DECRYPTION!!",font=("Helvetica",20))
    u.config(background='aqua',foreground="black")
    u.place(x=110,y=20)
    u1=Label(f3, text="Ciphertext", font=("Helvetica",14))
    u1.place(x=100,y=80)
    r1=Entry(f3, width=50, font=("Quintessential",14))
    r1.place(x=225,y=80,width=120)
    u2=Label(f3, text="Key", font=("Helvetica",14))
    u2.place(x=100,y=130)
    r2=Entry(f3, width=50, font=("Quintessential",14))
    r2.place(x=225,y=130,width=120)
    u3=Label(f3, text="Plaintext", font=("Helvetica",14))
    u3.config(background='pink',foreground="black")
    u3.place(x=100,y=180)
    r3=Entry(f3, width=50, font=("Quintessential",14))
    r3.config(background='pink',foreground="black")
    r3.place(x=225,y=180,width=120)
    b2=Button(f3,text="<-",command=home)
    b2.place(x=0,y=0,width=20,height=20)
    b3=Button(f3,text="Decrypt",command=Decryption)
    b3.place(x=200,y=230,width=100,height=40)
home()
root.mainloop()