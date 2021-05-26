
import tkinter as tk
from functools import partial

personal_information = []
IsInformatiomRight = False



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
    self.initface = tk.Frame(self.master,width = 800,height = 440)
    self.initface.pack()
    #開始按鈕
    Start_Button = tk.Button(self.initface , text = "START", font = "微軟正黑體 15", bg = "white", fg = "#323232", command = self.change)#定義按鈕功能
    Start_Button.pack()

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
    
    #按鈕區

    #Next按鈕
    Next_Button = tk.Button(self.face1,text="Next",bg="white",fg="#323232",command=partial(self.next,name_entry,sexual_entry,age_entry,weight_entry))
    Next_Button.pack()
    
   
  def cin(self,name_entry,sexual_entry,age_entry,weight_entry):
    name = name_entry.get()
    sexual = sexual_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    try:
      float_age = float(age)
      float_weight = float(weight)
      if name == "" or  float_age < 0  or float_weight < 0 or (sexual != "Male" and sexual !="Female" ):
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
      else:
        personal_information = [name,sexual,age,weight]
        IsInformatiomRight = True
        self.face1.destroy()
    except ValueError:
      error_text_ValueError = tk.Label(self.face1,text="Please enter right information",bg="#323232",fg="red")
      error_text_ValueError.pack()
      # error_text_ValueError.destroy()
  def next(self,name_entry,sexual_entry,age_entry,weight_entry):
    self.cin(name_entry,sexual_entry,age_entry,weight_entry)
      

if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()








