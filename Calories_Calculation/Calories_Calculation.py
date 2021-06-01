import tkinter as tk
from functools import partial




class basedesk():#基底視窗
  def __init__(self,master):
    self.root = master
    self.root.config()
    self.root.title("Calories Calculation")
    self.root.geometry("800x440+600+300")
    initface(self.root)

class initface():#初始畫面
  def __init__(self,master):
    self.master = master
    self.master.config(bg="#323232")#顏色
    self.master.attributes("-alpha",0.95)#透明度
    self.master.attributes("-topmost",1)#置頂
    #初始畫面
    self.initface = tk.Frame(self.master,width = 800,height = 440,bg="#323232")
    self.initface.pack()
    #開始按鈕
    Start_Button = tk.Button(self.initface , text = "START", font = "微軟正黑體 15", bg = "white", fg = "#323232", command = self.change)#定義按鈕功能
    Start_Button.place(x=355,y=175)

  def change(self):#頁面變化指令
    self.initface.destroy()
    face1(self.master)

class face1():#第1個視窗 
  
  def __init__(self,master):
    self.master = master
    self.master.config(bg="#323232")#顏色
    self.master.attributes("-alpha",0.95)#透明度
    self.master.attributes("-topmost",1)#置頂
    #第1個視窗
    self.face1 = tk.Frame(self.master,width = 800,height = 440,bg = "#323232")
    self.face1.pack()
    #Label區

    #請輸入個人資訊標籤
    title_text = tk.Label(self.face1,text="Enter your personal information",bg="#323232",fg="skyblue",font="微軟正黑體 15")
    title_text.pack()
    #姓名標籤
    name_text = tk.Label(self.face1,text="Name",bg="#323232",fg="white")
    name_text.pack()
    name_entry = tk.Entry(self.face1)
    name_entry.pack()
    #性別標籤
    sexual_text = tk.Label(self.face1,text="Sexual",bg="#323232",fg="white")
    sexual_text.pack()
    sexual_entry = tk.Entry(self.face1)
    sexual_entry.pack()
    #年齡標籤
    age_text = tk.Label(self.face1,text="Age",bg="#323232",fg="white")
    age_text.pack()
    age_entry = tk.Entry(self.face1)
    age_entry.pack()
    #體重標籤
    weight_text = tk.Label(self.face1,text="Weight(kg)",bg="#323232",fg="white")
    weight_text.pack()
    weight_entry = tk.Entry(self.face1)
    weight_entry.pack()

    height_text = tk.Label(self.face1,text="Height(cm)",bg="#323232",fg="white")
    height_text.pack()
    height_entry = tk.Entry(self.face1)
    height_entry.pack()
    #按鈕區

    #Next按鈕
    Next_Button = tk.Button(self.face1,text="Next",bg="white",fg="#323232",command=partial(self.next,name_entry,sexual_entry,age_entry,weight_entry,height_entry))
    Next_Button.pack(padx=20, pady=10)
    
   
  def cin(self,name_entry,sexual_entry,age_entry,weight_entry,height_entry):
    global personal_information
    name = name_entry.get()
    sexual = sexual_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    try:
      float_age = float(age)
      float_weight = float(weight)
      float_height = float(height)
      if name == "" or  float_age < 0  or float_weight < 0 or float_height<0 or (sexual != "Male" and sexual !="Female" ):
        if name == "":
           error_text_name = tk.Label(self.face1,text="Please enter your name",bg="#323232",fg="red")
           error_text_name.pack()
        if sexual != "Male" and sexual !="Female":
           error_text_sexual = tk.Label(self.face1,text="Please enter Male or Female",bg="#323232",fg="red")
           error_text_sexual.pack()
        if float_age < 0:
           error_text_age = tk.Label(self.face1,text="Please enter right age",bg="#323232",fg="red")
           error_text_age.pack()
        if float_weight < 0:
           error_text_weight = tk.Label(self.face1,text="Please enter right weight",bg="#323232",fg="red")
           error_text_weight.pack()
        if float_height < 0:
           error_text_height = tk.Label(self.face1,text="Please enter right height",bg="#323232",fg="red")
           error_text_height.pack()
      else:
        personal_information = [name,sexual,float_age,float_weight,float_height]
        IsInformatiomRight = True
        self.change2()
    except ValueError:
      error_text_ValueError = tk.Label(self.face1,text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.pack()
      # error_text_ValueError.destroy()
  def next(self,name_entry,sexual_entry,age_entry,weight_entry,height_entry):
    self.cin(name_entry,sexual_entry,age_entry,weight_entry,height_entry)
  def change2(self):
    self.face1.destroy()
    face2(self.master)


class face2():#第二個視窗
  def __init__(self,master):
    self.master = master
    self.master.config(bg="#323232")#顏色
    self.master.attributes("-alpha",0.95)#透明度
    self.face2 = tk.Frame(self.master,width = 800,height = 440,bg = "#323232")
    self.face2.pack()
    #標籤
    self.title_text3=tk.Label(self.face2,text="What you eat today?",bg="#323232",fg="skyblue")
    self.title_text3.config(font="微軟正黑體 15")
    self.title_text3.place(x=295,y=10)
    #按鈕

    #飯
    self.rice_btn=tk.Button(self.face2,text="Rice(bowl)",bg="white",fg="#323232",command = self.Rice_entry)
    self.rice_btn.place(x=50, y=60)
    self.rice_entry=tk.Entry(self.face2)
    #麵
    self.noodle_btn=tk.Button(self.face2,text="noodle(bowl)",bg="white",fg="#323232",command = self.Noodle_entry)
    self.noodle_btn.place(x=200, y=60)
    self.noodle_entry=tk.Entry(self.face2)
    #蔬菜
    self.vegetable_btn=tk.Button(self.face2,text="vegetable(plate)",bg="white",fg="#323232",command = self.Vegetable_entry)
    self.vegetable_btn.place(x=350, y=60)
    self.vegetable_entry=tk.Entry(self.face2)

    #豬肉
    self.pork_btn=tk.Button(self.face2,text="pork(100g)",bg="white",fg="#323232",command = self.Pork_entry)
    self.pork_btn.place(x=525, y=60)
    self.pork_entry=tk.Entry(self.face2)
    #牛肉
    self.beef_btn=tk.Button(self.face2,text="beef(100g)",bg="white",fg="#323232",command = self.Beef_entry)
    self.beef_btn.place(x=685, y=60)
    self.beef_entry=tk.Entry(self.face2)
    #魚
    self.fish_btn=tk.Button(self.face2,text="fish(100g)",bg="white",fg="#323232",command = self.Fish_entry)
    self.fish_btn.place(x=50, y=210)
    self.fish_entry=tk.Entry(self.face2)
    #家禽
    self.poultry_btn=tk.Button(self.face2,text="poultry(100g)",bg="white",fg="#323232",command = self.Poultry_entry)
    self.poultry_btn.place(x=200, y=210)
    self.poultry_entry=tk.Entry(self.face2)
    #羊肉
    self.lamb_btn=tk.Button(self.face2,text="lamb(100g)",bg="white",fg="#323232",command =self.Lamb_entry)
    self.lamb_btn.place(x=350, y=210)
    self.lamb_entry=tk.Entry(self.face2)
    #麵包
    self.bread_btn=tk.Button(self.face2,text="bread(slice)",bg="white",fg="#323232",command = self.Bread_entry)
    self.bread_btn.place(x=525, y=210)
    self.bread_entry=tk.Entry(self.face2)
    #手搖杯
    self.Hand_cup_btn=tk.Button(self.face2,text="hand_cup(slice)",bg="white",fg="#323232",command = self.Hand_cup_entry)
    self.Hand_cup_btn.place(x=685, y=210)
    self.hand_cup_entry=tk.Entry(self.face2)

    #next按鈕
    self.Next2_Button = tk.Button(self.face2,text="Next",bg="white",fg="#323232",command=self.cin2)
    self.Next2_Button.place(x=375,y=385) 


    #點按鈕後輸入

  def Rice_entry(self):
    self.rice_entry.place(width=70,height=20,x=50, y=100)
    self.rice_btn.configure(state=tk.DISABLED)


  def Noodle_entry(self):
    self.noodle_entry.place(width=87,height=20,x=200, y=100)
    self.noodle_btn.configure(state=tk.DISABLED)

  def Vegetable_entry(self):
    self.vegetable_entry.place(width=103,height=20,x=350, y=100)
    self.vegetable_btn.configure(state=tk.DISABLED)

  def Pork_entry(self):
    self.pork_entry.place(width=70,height=20,x=525, y=100)
    self.pork_btn.configure(state=tk.DISABLED)

  def Beef_entry(self):
    self.beef_entry.place(width=70,height=20,x=685, y=100)
    self.beef_btn.configure(state=tk.DISABLED)

  def Fish_entry(self):
    self.fish_entry.place(width=65,height=20,x=50, y=250)
    self.fish_btn.configure(state=tk.DISABLED)

  def Poultry_entry(self):
    self.poultry_entry.place(width=77,height=20,x=200, y=250)
    self.poultry_btn.configure(state=tk.DISABLED)

  def Lamb_entry(self): 
    self.lamb_entry.place(width=75,height=20,x=350, y=250)
    self.lamb_btn.configure(state=tk.DISABLED)

  def Bread_entry(self):
    self.bread_entry.place(width=70,height=20,x=525, y=250)
    self.bread_btn.configure(state=tk.DISABLED)

  def Hand_cup_entry(self):
    self.hand_cup_entry.place(width=98,height=20,x=685, y=250)
    self.Hand_cup_btn.configure(state=tk.DISABLED)

  #讀取輸入
  def cin2(self):
    global food_list
    rice = self.rice_entry.get()
    noodle = self.noodle_entry.get()
    vegetable = self.vegetable_entry.get()
    pork = self.pork_entry.get()
    beef = self.beef_entry.get()
    fish = self.fish_entry.get()
    poultry = self.poultry_entry.get()
    lamb = self.lamb_entry.get()
    bread = self.bread_entry.get()
    hand_cup= self.hand_cup_entry.get()
    food_list = [rice,noodle,vegetable,pork,beef,fish,poultry,lamb,bread,hand_cup]
    for i in range(len(food_list)):
        if food_list[i] == "":
          food_list[i] = 0
        else:
          try:
            food_list[i] = float(food_list[i])
            if food_list[i] < 0:
              error_text_ValueError = tk.Label(self.face2,text="Please enter right information",bg="#323232",fg="red")
              error_text_ValueError.place(x=320,y=360)
              food_list.clear()
              return
          except ValueError:
            error_text_ValueError = tk.Label(self.face2,text="Please enter right information",bg="#323232",fg="red")
            error_text_ValueError.place(x=320,y=360)
            food_list.clear()
            return
    self.change3()
  def change3(self):
    self.face2.destroy()
    face3(self.master)
 
class face3():
  def __init__(self,master):
    self.master = master
    self.master.config(bg="#323232")#顏色
    self.master.attributes("-alpha",0.95)#透明度
    self.master.attributes("-topmost",1)#置頂
    #視窗3
    self.face3 = tk.Frame(self.master,width = 800,height = 440,bg = "#323232")
    self.face3.pack()
    #標籤
    self.title_text4=tk.Label(self.face3,text="Enter your personal information",bg="#323232",fg="skyblue")
    self.title_text4.config(font="微軟正黑體 15")
    self.title_text4.place(x=250,y=10)

    #按鈕區

    #走路
    self.walking_btn=tk.Button(self.face3,text="walking(30mins)",bg="white",fg="#323232",command=self.walking_entry)
    self.walking_btn.place(x=30, y=60)
    self.walking_entry=tk.Entry(self.face3)
    #慢跑
    self.jogging_btn=tk.Button(self.face3,text="jogging(30mins)",bg="white",fg="#323232",command=self.jogging_entry)
    self.jogging_btn.place(x=180, y=60)
    self.jogging_entry=tk.Entry(self.face3)
    #跑步
    self.running_btn=tk.Button(self.face3,text="running(30mins)",bg="white",fg="#323232",command=self.running_entry)
    self.running_btn.place(x=350, y=60)
    self.running_entry=tk.Entry(self.face3)
    #游泳
    self.swimming_btn=tk.Button(self.face3,text="swimming(30mins)",bg="white",fg="#323232",command=self.swimming_entry)
    self.swimming_btn.place(x=505, y=60)
    self.swimming_entry=tk.Entry(self.face3)
    #騎腳踏車
    self.cycling_btn=tk.Button(self.face3,text="cycling(30mins)",bg="white",fg="#323232",command=self.cycling_entry)
    self.cycling_btn.place(x=665, y=60)
    self.cycling_entry=tk.Entry(self.face3)
    #籃球
    self.basketball_btn=tk.Button(self.face3,text="basketball(30mins)",bg="white",fg="#323232",command=self.basketball_entry)
    self.basketball_btn.place(x=30, y=210)
    self.basketball_entry=tk.Entry(self.face3)
    #跳繩
    self.rope_skipping_btn=tk.Button(self.face3,text="rope skipping(30mins)",bg="white",fg="#323232",command=self.rope_skipping_entry)
    self.rope_skipping_btn.place(x=180, y=210)
    self.rope_skipping_entry=tk.Entry(self.face3)
    #瑜珈
    self.Yoga_btn=tk.Button(self.face3,text="Yoga(30mins)",bg="white",fg="#323232",command=self.Yoga_entry)
    self.Yoga_btn.place(x=350, y=210)
    self.Yoga_entry=tk.Entry(self.face3)
    #羽毛球
    self.badminton_btn=tk.Button(self.face3,text="badminton(30mins)",bg="white",fg="#323232",command=self.badminton_entry)
    self.badminton_btn.place(x=505, y=210)
    self.badminton_entry=tk.Entry(self.face3)
    #乒乓球
    self.pingpong_btn=tk.Button(self.face3,text="pingpong(30mins)",bg="white",fg="#323232",command=self.pingpong_entry)
    self.pingpong_btn.place(x=665, y=210)
    self.pingpong_entry=tk.Entry(self.face3)

    #Next按鈕
    Next3_Button=tk.Button(self.face3,text="Next",bg="white",fg="#323232",command=self.cin3)
    Next3_Button.place(x=375,y=385)

  def walking_entry(self):
    self.walking_entry.place(width=100,height=20,x=30, y=100)
    self.walking_btn.configure(state=tk.DISABLED)
  def jogging_entry(self):
    self.jogging_entry.place(width=103,height=20,x=180, y=100)
    self.jogging_btn.configure(state=tk.DISABLED)
  def running_entry(self):
    self.running_entry.place(width=101,height=20,x=350, y=100)
    self.running_btn.configure(state=tk.DISABLED)
  def swimming_entry(self):
    self.swimming_entry.place(width=115,height=20,x=505, y=100)
    self.swimming_btn.configure(state=tk.DISABLED)
  def cycling_entry(self):
    self.cycling_entry.place(width=97,height=20,x=665, y=100)
    self.cycling_btn.configure(state=tk.DISABLED)
  def basketball_entry(self):
    self.basketball_entry.place(width=116,height=20,x=30, y=250)
    self.basketball_btn.configure(state=tk.DISABLED)
  def rope_skipping_entry(self):
    self.rope_skipping_entry.place(width=135,height=20,x=180, y=250)
    self.rope_skipping_btn.configure(state=tk.DISABLED)
  def Yoga_entry(self):
    self.Yoga_entry.place(width=88,height=20,x=350, y=250)
    self.Yoga_btn.configure(state=tk.DISABLED)
  def badminton_entry(self): 
    self.badminton_entry.place(width=121,height=20,x=505, y=250)
    self.badminton_btn.configure(state=tk.DISABLED)
  def pingpong_entry(self):
    self.pingpong_entry.place(width=115,height=20,x=665, y=250)
    self.pingpong_btn.configure(state=tk.DISABLED)
  def cin3(self):
      global exercise_list
      walking = self.walking_entry.get()
      jogging = self.jogging_entry.get()
      running = self.running_entry.get()
      swimming = self.swimming_entry.get()
      cycling = self.cycling_entry.get()
      basketball = self.basketball_entry.get()
      rope_skipping = self.rope_skipping_entry.get()
      Yoga = self.Yoga_entry.get()
      badminton = self.badminton_entry.get()
      pingpong = self.pingpong_entry.get()
      exercise_list = [walking,jogging,running,swimming,cycling,basketball,rope_skipping,Yoga,badminton,pingpong]
      for i in range(len(exercise_list)):
        if exercise_list[i] == "":
          exercise_list[i] = 0
        else:
          try:
            exercise_list[i] = float(exercise_list[i])
            if exercise_list[i] < 0:
              error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
              error_text_ValueError.place(x=320,y=360)
              exercise_list.clear()
              return
          except ValueError:
            error_text_ValueError = Label(text="Please enter right information",bg="#323232",fg="red")
            error_text_ValueError.place(x=320,y=360)
            exercise_list.clear()
      self.change4()
  def change4(self):
    self.face3.destroy()#第三個視窗
    face4(self.master)

class face4():
  def __init__(self,master):
    global food_list,exercise_list,personal_information
    self.master = master
    self.master.config(bg="#323232")#顏色
    self.master.attributes("-alpha",0.95)#透明度
    self.master.attributes("-topmost",1)#置頂
    #第4個視窗
    self.face4 = tk.Frame(self.master,width = 800,height = 440,bg = "#323232")
    self.face4.pack()
    #運算區


    #計算運動消耗量
    Sport_consuming=1.75*exercise_list[0]+4.1*exercise_list[1]+7.5*exercise_list[2]+4.1*exercise_list[3]+6.2*exercise_list[4]+3.65*exercise_list[5]+5.25*exercise_list[6]+1.5*exercise_list[7]+2.55*exercise_list[8]+2.1*exercise_list[9]
    #尋找PA值並計算基本消耗量
    if Sport_consuming <= 2.8 and personal_information[1] == "Female":
       Basic_consuming=354-6.91*personal_information[2]+1*(9.36*personal_information[3]+7.26*personal_information[4])
    if Sport_consuming <= 2.8 and personal_information[1] == "Male": 
       Basic_consuming=662-9.53*personal_information[2]+1*(15.91*personal_information[3]+5.396*personal_information[4])
    if 9.8 >= Sport_consuming > 2.8 and personal_information[1] == "Female" :
       Basic_consuming=354-6.91*personal_information[2]+1.12*(9.36*personal_information[3]+7.26*personal_information[4])
    if 9.8 >= Sport_consuming > 2.8 and personal_information[1] == "Male" :
       Basic_consuming=662-9.53*personal_information[2]+1.11*(15.91*personal_information[3]+5.396*personal_information[4])
    if 23.8 >= Sport_consuming > 9.8 and personal_information[1] == "Female" :
       Basic_consuming=354-6.91*personal_information[2]+1.27*(9.36*personal_information[3]+7.26*personal_information[4])
    if 23.8 >= Sport_consuming > 9.8 and personal_information[1] == "Male" :
       Basic_consuming=662-9.53*personal_information[2]+1.25*(15.91*personal_information[3]+5.396*personal_information[4])
    if Sport_consuming > 23.8 and personal_information[1] == "Female" :
       Basic_consuming=354-6.91*personal_information[2]+1.45*(9.36*personal_information[3]+7.26*personal_information[4])
    if Sport_consuming > 23.8 and personal_information[1] == "Male" :
       Basic_consuming=662-9.53*personal_information[2]+1.48*(15.91*personal_information[3]+5.396*personal_information[4])

    #一天消耗量
    Day_consuming = Basic_consuming 
    str_Day_consuming = str(int(Day_consuming))

    #計算一天攝取量
    Day_ingesting = 225*food_list[0]+138.1*food_list[1]+65.2*food_list[2]+242.1*food_list[3]+250.5*food_list[4]+150*food_list[5]+272*food_list[6]+294*food_list[7]+264.6*food_list[8]+600*food_list[9]
    str_Day_ingesting = str(int(Day_ingesting))
 

    #計算差值
    Difference = Day_ingesting-Day_consuming
    str_Difference = str(int(Difference))
    
    #宣告名字變成字串
    name=personal_information[0]
    name_str=str(name)

    Day_consuming_text=tk.Label(self.face4,text=name_str+",your day consuming is"+str_Day_consuming,bg="#323232",fg="white")
    Day_consuming_text.pack()

    Day_ingesting_text=tk.Label(self.face4,text=name_str+",your day ingesting is"+str_Day_ingesting,bg="#323232",fg="white")
    Day_ingesting_text.pack()

    Difference_text=tk.Label(self.face4,text=name_str+",your Difference is"+str_Difference,bg="#323232",fg="white")
    Difference_text.pack()


   

if __name__ == '__main__':    
  root = tk.Tk()
  basedesk(root)
  root.mainloop()