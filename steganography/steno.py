#python3 -m venv myenv ; source myenv/bin/activate ;pip install stegano


from tkinter import *
from tkinter import filedialog
import tkinter as tkr
from PIL import Image, ImageTk
import os
from stegano import lsb # type: ignore



cmnBg='#54DCF7'

root=Tk()
root.title("Hider - Hide Secrets in Images")
root.geometry("700x500")
root.resizable(False, False)
root.configure(background=cmnBg)

#functions

def hide():
    global secret
    message=text1.get(1.0, END)
    secret = lsb.hide(str(filename),message)
def show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)
def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Image File",
                                        filetypes=(("PNG File","*.png"),
                                                  ("JPG File","*.jpg"),("All file","*.txt")))
    if filename:
        try:
            img = Image.open(filename)
            img = ImageTk.PhotoImage(img)
            lbl.configure(image=img, width=250, height=250)
            lbl.image = img  # Keep a reference to prevent garbage collection
        except Exception as e:
            print("Error:", e)
def save():
    secret.save("hidden.png")


#icon
image_icon = PhotoImage(file="./assets/hidden.png")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="./assets/eye.png")
resized_logo= logo.subsample(3)
Label(root,image=resized_logo,bg=cmnBg).place(x=10,y=0)
Label(root,text="Steganography", bg=cmnBg,fg="#3B52AF",font='arial 25 bold').place(x=200,y=12)

#frame_1
f=Frame(root,bd=3,bg='#364BA1',width=340, height=280, )
f.place(x=10,y=80)

lbl=Label(f,bg='black')
lbl.place(x=40,y=10)

#frame_2
f2=Frame(root,bd=3,width=340, height=280 , bg='#204E5C')
f2.place(x=350,y=80)

text1=Text(f2,font='Robote 15', bg='#204E5C',fg='#13A913',wrap=WORD)
text1.place(x=0,y= 0,width=320,height=295)

scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#frame_3
f3=Frame(root,bd=3,width=330, height=80 , bg='#204E5C')
f3.place(x=10,y=370)

Button(f3,text="Open Image", width=10, height=1, font='arial 8 bold',command=showimage).place(x=20,y=35)
Button(f3,text="Save Image", width=10, height=1, font='arial 8 bold',command=save).place(x=180,y=35)
Label(f3,text="Image file", bg='#204E5C', fg='yellow').place(x=110,y=5)

#frame_4
f4=Frame(root,bd=3,width=330, height=80 , bg='#204E5C')
f4.place(x=360,y=370)

Button(f4,text="Hide Text", width=10, height=1, font='arial 8 bold',command=hide).place(x=20,y=35)
Button(f4,text="Show Text", width=10, height=1, font='arial 8 bold',command=show).place(x=180,y=35)
Label(f4,text="Image file", bg='#204E5C', fg='yellow').place(x=110,y=5)
root.mainloop()

root.mainloop()
