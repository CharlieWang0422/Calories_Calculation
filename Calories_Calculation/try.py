from tkinter import*

win=Tk()
win.title("Calories Calculation")
win.geometry("800x440+600+300") #大小
win.resizable(0,0)
win.config(bg="#323232")#顏色
win.attributes("-alpha",0.95)#透明度
win.attributes("-topmost",1)#置頂

def cin():
    rice = rice_entry.get()
    noodle = noodle_entry.get()
    vegetable = vegetable_entry.get()
    pork = pork_entry.get()
    beef=beef_entry.get()
    fish=fish_entry.get()
    poultry=poultry_entry.get()
    lamb=lamb_entry.get()
    hand_cup= hand_cup_entry.get()
    bread=bread_entry.get()
    try:
     if rice == "":
      float_rice=0
     else :
      float_rice=float(rice)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if noodle == "":
      float_noodle=0
     else :
      float_noodle=float(noodle)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if vegetable == "":
      float_vegetable=0
     else :
      float_vegetable=float(vegetable)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if pork == "":
      float_pork=0
     else :
      float_pork=float(pork)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if lamb == "":
      float_lamb=0
     else :
      float_lamb=float(lamb)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if beef == "":
      float_beef=0
     else :
      float_beef=float(beef)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if fish == "":
      float_fish=0
     else :
      float_fish=float(fish)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if poultry == "":
      float_poultry=0
     else :
      float_poultry=float(poultry)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if bread == "":
      float_bread=0
     else :
      float_bread=float(bread)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
     if hand_cup == "":
       float_hand_cup=0
     else :
        float_hand_cup=float(hand_cup)
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)
    try:
      if float_rice < 0  or float_noodle < 0 or float_vegetable<0 or float_pork<0 or float_lamb<0 or float_beef or float_fish or float_poultry or float_bread or float_hand_cup :
       error_text_age = Label(text="Please enter right information",bg="#323232",fg="red")
       error_text_age.place(x=320,y=360)
      else:
       personal_eating = [float_rice,float_noodle,float_vegetable,float_pork,float_lamb,float_beef,float_fish,float_poultry,float_bread,float_hand_cup]
    except ValueError:
      error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.place(x=320,y=360)


title_text3=Label(text="Enter your personal information",bg="#323232",fg="skyblue")
title_text3.config(font="微軟正黑體 15")
title_text3.pack()

def Rice_entry():
  rice_entry.place(width=70,height=20,x=50, y=100)
  rice_btn.configure(state=DISABLED)
rice_btn=Button(text="Rice(bowl)",bg="white",fg="#323232",command=Rice_entry)
rice_btn.place(x=50, y=60)
rice_entry=Entry()


def Noodle_entry():
  noodle_entry.place(width=87,height=20,x=200, y=100)
  noodle_btn.configure(state=DISABLED)
noodle_btn=Button(text="noodle(bowl)",bg="white",fg="#323232",command=Noodle_entry)
noodle_btn.place(x=200, y=60)
noodle_entry=Entry()



def Vegetable_entry():
  vegetable_entry.place(width=103,height=20,x=350, y=100)
  vegetable_btn.configure(state=DISABLED)
vegetable_btn=Button(text="vegetable(plate)",bg="white",fg="#323232",command=Vegetable_entry)
vegetable_btn.place(x=350, y=60)
vegetable_entry=Entry()


def Pork_entry():
  pork_entry.place(width=70,height=20,x=525, y=100)
  pork_btn.configure(state=DISABLED)
pork_btn=Button(text="pork(100g)",bg="white",fg="#323232",command=Pork_entry)
pork_btn.place(x=525, y=60)
pork_entry=Entry()

def Beef_entry():
  beef_entry.place(width=70,height=20,x=685, y=100)
  beef_btn.configure(state=DISABLED)
beef_btn=Button(text="beef(100g)",bg="white",fg="#323232",command=Beef_entry)
beef_btn.place(x=685, y=60)
beef_entry=Entry()

def Fish_entry():
  fish_entry.place(width=65,height=20,x=50, y=250)
  fish_btn.configure(state=DISABLED)
fish_btn=Button(text="fish(100g)",bg="white",fg="#323232",command=Fish_entry)
fish_btn.place(x=50, y=210)
fish_entry=Entry()

def Poultry_entry():
  poultry_entry.place(width=87,height=20,x=200, y=250)
  poultry_btn.configure(state=DISABLED)
poultry_btn=Button(text="poultry(100g)",bg="white",fg="#323232",command=Poultry_entry)
poultry_btn.place(x=200, y=210)
poultry_entry=Entry()

def Bread_entry(): 
  bread_entry.place(width=75,height=20,x=525, y=250)
  bread_btn.configure(state=DISABLED)
bread_btn=Button(text="bread(slice)",bg="white",fg="#323232",command=Bread_entry)
bread_btn.place(x=525, y=210)
bread_entry=Entry()


def Lamb_entry():
  lamb_entry.place(width=75,height=20,x=350, y=250)
  lamb_btn.configure(state=DISABLED)
lamb_btn=Button(text="lamb(100g)",bg="white",fg="#323232",command=Lamb_entry)
lamb_btn.place(x=350, y=210)
lamb_entry=Entry()

def Hand_cup_entry():
  hand_cup_entry.place(width=65,height=20,x=685, y=250)
  Hand_cup_btn.configure(state=DISABLED)
Hand_cup_btn=Button(text="hand_cup",bg="white",fg="#323232",command=Hand_cup_entry)
Hand_cup_btn.place(x=685, y=210)
hand_cup_entry=Entry()



btn=Button(text="Next",bg="white",fg="#323232",command=cin)
btn.pack(side=BOTTOM,padx=10,pady=10)





win.mainloop()