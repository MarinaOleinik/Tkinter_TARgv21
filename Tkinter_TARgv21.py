from tkinter import *
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker2(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)
def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    val=str(var.get())+", " #value 1,2 või 3
    ent.insert(END,val)
aken=Tk() #Akna loomine
aken.title("Akna nimetus") #Akna pealkiri
aken.geometry("600x400") #Akna suurus
btn=Button(aken,text="Vajuta siia",font="Arial 20",fg="green",bg="lightblue", width=20, height=3,relief=SUNKEN)#GROOVE, RAISED Loome nupp
lbl=Label(aken,text="...") #Pealkiri
ent=Entry(aken,fg="blue",width=20,font="Arial 20",justify=CENTER) #Rida teksti sisestamiseks. tekxt on keskel
var=IntVar() #StringVar()
#var.set(3) valib kolmas button
r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik)

btn.bind("<Button-1>",klikker)#LKM 
btn.bind("<Button-3>",klikker2)#PKM
ent.bind("<Return>",text_to_lbl)#Enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()
