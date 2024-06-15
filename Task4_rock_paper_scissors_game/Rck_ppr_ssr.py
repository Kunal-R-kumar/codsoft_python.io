from tkinter import Tk,Frame,IntVar,Button,Label,NORMAL,DISABLED
from PIL import Image,ImageTk
from random import randint
# Basic window setup
base = Tk()
base.title("Rock Paper Scissor")
base.attributes("-fullscreen", True)
sw = base.winfo_screenwidth()
sh = base.winfo_screenheight()
# Basic variables
dt = IntVar(value=0)
#pic corrector
def piccorrector(name,w,h):
    piccor = Image.open(f"{name}.png").resize((sw//w, sh//h))
    return ImageTk.PhotoImage(piccor)
photoci = piccorrector("ci",2,1)
photoui = piccorrector("ui",2,1)
pic1 = piccorrector("1",2,1)
pic2 = piccorrector("2",2,1)
pic3 = piccorrector("3",2,1)
cfr = Frame(base, width=sw//2, height=sh)
cfr.pack(side="left", fill="y", expand=True)
ufr = Frame(base, width=sw//2, height=sh)
ufr.pack(side="right", fill="y", expand=True)
clbl = Label(cfr, image=photoci)
clbl.pack()
ulbl = Label(ufr, image=photoui)
ulbl.pack()
pic=0
def binder():
    base.bind("<r>",lambda event:stopp(1))
    base.bind("<p>",lambda event:stopp(2))
    base.bind("<s>",lambda event:stopp(3))
def playy():
    if dt.get() == 0:
        for btn in [stb,pab,scb]:
            btn.configure(state=NORMAL)
        binder()        
        global pic
        pic = randint(0,2)
        piclist=[pic1,pic2,pic3]
        clbl.config(image=piclist[pic])
        clbl.image = piclist[pic]
        cfr.after(40, playy)
        play.configure(text="Play again🔄",font=22,command=lambda:[dt.set(0),playy()] ,state=DISABLED)
        base.unbind("<Return>")
        play.place(relx=0.45,rely=0.87)
        rslt.configure(text="choose One",fg="white",bg="#1f1e3e")
    cmpcnt.place(relx=0.33)
    usrcnt.place(relx=0.45)
    photouu = piccorrector("u",2,1)
    ulbl.config(image=photouu)
    ulbl.image = photouu
    stb.place(relx=0.53, rely=0.08)
    scb.place(relx=0.78,rely=0.08)
    pab.place(relx=0.655,rely=0.47)
def stopp(a):
    dt.set(1)
    for btn in [stb,pab,scb]:
        btn.configure(state=DISABLED)
    for bindd in ["r","p","s"]:
        base.unbind(f"<{bindd}>")
    result(a)
def result(slctn):
    cmp=pic+1
    if slctn==cmp:
        rslt.configure(text="Match Draw",fg="White",bg="#1f1e3e")
    elif (slctn==3 and cmp==2) or (slctn==2 and cmp==1) or (slctn==1 and cmp==3):
        rslt.configure(text="You Win",fg="Green",bg="White")
        usrscr.set(usrscr.get()+1)
        usrcnt.configure(text=f"User: {usrscr.get()}")
    else:
        rslt.configure(text="You Loss",fg="Red",bg="white")
        cmpcnt.configure(text=f"Computer: {cmpscr.get()+1}")
        cmpscr.set(cmpscr.get()+1)
    play.configure(state=NORMAL)
    base.bind("<Return>",lambda event : [dt.set(0),playy()])
# Button to start the game
play = Button(base, text="Play Now!!", font=("Algerian", 22), command=playy)
play.place(relx=0.44, rely=0.87)
# Button to stop the game
stpic=piccorrector("1",5,3)
papic=piccorrector("2",5,3)
scpic=piccorrector("3",5,3)
stb = Button(base, image=stpic, font=("Algerian", 22), command=lambda: stopp(1))
pab = Button(base, image=papic, font=("Algerian", 22), command=lambda: stopp(2))
scb = Button(base, image=scpic, font=("Algerian", 22), command=lambda: stopp(3))
rslt=Label(base,text="Let's start",font=("Algerian", 22),fg="white",bg="#1f1e3e")
rslt.place(relx=0.45,rely=0.50)
cmpscr=IntVar(value=0)
usrscr=IntVar(value=0)
cmpcnt=Label(cfr,text=f"Computer: {cmpscr.get()}",font=("Times Italics", 24),fg="#f76461",bg="#1f1e3e")
usrcnt=Label(ufr,text=f"User: {usrscr.get()}",font=("Times Italics", 24),fg="#4B7FBB",bg="#1f1e3e")
base.bind("<Return>",lambda event : playy())
base.mainloop()