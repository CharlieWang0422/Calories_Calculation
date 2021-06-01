personal_information=["Chen","Male",22,50,175]
exercise_list=[0,0,0,0,0,1,1,1,1,1]
food_list=[0,0,0,0,0,1,2,1,1,1]







#計算運動消耗量
Sport_consuming=1.75*exercise_list[0]+4.1*exercise_list[1]+7.5*exercise_list[2]+4.1*exercise_list[3]+6.2*exercise_list[4]+3.65*exercise_list[5]+5.25*exercise_list[6]+1.5*exercise_list[7]+2.55*exercise_list[8]+2.1*exercise_list[9]
#尋找PA值並計算基本消耗量
if Sport_consuming <= 2.8 and personal_information[1] == "Female":
   Basic_consuming=354-(6.91*personal_information[2]+1*(9.36*personal_information[3]+7.26*personal_information[4]))
if Sport_consuming <= 2.8 and personal_information[1] == "Male": 
   Basic_consuming=662-(9.53*personal_information[2]+1*(15.91*personal_information[3]+5.396*personal_information[4]))
if 9.8 >= Sport_consuming > 2.8 and personal_information[1] == "Female" :
   Basic_consuming=354-(6.91*personal_information[2]+1.12*(9.36*personal_information[3]+7.26*personal_information[4]))
if 9.8 >= Sport_consuming > 2.8 and personal_information[1] == "Male" :
   Basic_consuming=662-(9.53*personal_information[2]+1.11*(15.91*personal_information[3]+5.396*personal_information[4]))
if 23.8 >= Sport_consuming > 9.8 and personal_information[1] == "Female" :
   Basic_consuming=354-(6.91*personal_information[2]+1.27*(9.36*personal_information[3]+7.26*personal_information[4]))
if 23.8 >= Sport_consuming > 9.8 and personal_information[1] == "Male" :
   Basic_consuming=662-(9.53*personal_information[2]+1.25*(15.91*personal_information[3]+5.396*personal_information[4]))
if Sport_consuming > 23.8 and personal_information[1] == "Female" :
   Basic_consuming=354-(6.91*personal_information[2]+1.45*(9.36*personal_information[3]+7.26*personal_information[4]))
if Sport_consuming > 23.8 and personal_information[1] == "Male" :
   Basic_consuming=662-(9.53*personal_information[2]+1.48*(15.91*personal_information[3]+5.396*personal_information[4]))
#一天消耗量
Day_consuming = Basic_consuming + Sport_consuming*personal_information[3]
str_Day_consuming=str(Day_consuming)

#計算一天攝取量
Day_ingesting = 225*food_list[0]+138.1*food_list[1]+65.2*food_list[2]+242.1*food_list[3]+250.5*food_list[4]+150*food_list[5]+272*food_list[6]+294*food_list[7]+264.6*food_list[8]+600*food_list[9]
str_Day_ingesting = str(Day_ingesting)

#計算差值
Difference = Day_ingesting-Day_consuming
str_Difference = str(Difference)

#宣告名字變成字串
name=personal_information[0]
name_str=str(name)

Day_consuming_text=tk.Label(text=name_str+",your day consuming is"+str_Day_consuming,bg="#323232",fg="white")
Day_consuming_text.pack(padx=20, pady=30)

Day_ingesting_text=tk.Label(text=name_str+",your day ingesting is"+str_Day_ingesting,bg="#323232",fg="white")
Day_ingesting_text.pack(padx=20, pady=30)

Difference_text=tk.Label(text=name_str+",your Difference is"+str_Difference,bg="#323232",fg="white")
Difference_text.pack(padx=20, pady=30)
