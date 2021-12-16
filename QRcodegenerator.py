import tkinter


from tkinter import *
import qrcode
import image
from PIL import ImageTk,Image

root=Tk()
root.geometry("500x500")
root.title("QRcode Generator")

def generate():
    global codeimg
    qr=qrcode.QRCode(version=15,box_size=10,border=5)

    data=DataEntry.get()

    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img=img.resize((250,250))
    codeimg=ImageTk.PhotoImage(img)
    lab=Label(root,image=codeimg)
    lab.place(x=130,y=40)
    


text=Label(root,text="Enter Link")
text.place(x=50,y=300)

DataEntry=Entry(root,borderwidth=2,width=50)
DataEntry.place(x=110,y=300)

gen=Button(root,text="Generate",borderwidth=2,command=generate)
gen.place(x=230,y=350)


root.mainloop()


