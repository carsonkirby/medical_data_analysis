import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")



def getHeart():
    
    df_h = df.loc[(df.attack == 1)]
    heart_attacks = len(df_h)
    
    df_n = df.loc[(df.attack == 0)]
    no_attacks = len(df_n)
    
    t_attack_history = heart_attacks + no_attacks
   
    no_ha_percent_notation = "{:,.2f}%".format(no_attacks/t_attack_history*100)
    ha_percent_notation = "{:,.2f}%".format(heart_attacks/t_attack_history*100)
    
    print("\nThe percent of no heart attacks in the data: " + no_ha_percent_notation)  
    print("The percent of heart attacks in the data:  " + ha_percent_notation)
    
    labels = 'Heart Attack', 'No Heart Attack'
    sizes = [heart_attacks, no_attacks]
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    ax1.axis('equal')
    ax1.set_title('Heart Attack Ratio in Data')
    
    # fig1 = plt.figure()
    plt.show()
    fig1.savefig('HeartAttack.png')
     
    
def getGender():
    df_m = df.loc[(df.sex == 0) & (df.attack == 1)]
    m_heart_attacks = len(df_m)
    
    df_f = df.loc[(df.sex == 1) & (df.attack == 1)]
    f_heart_attacks = len(df_f)
     
    t_heart_attacks = m_heart_attacks + f_heart_attacks
    

    male_percent_noation = "{:,.2f}%".format(m_heart_attacks/t_heart_attacks*100)
    female_percent_notaion = "{:,.2f}%".format(f_heart_attacks/t_heart_attacks*100)
    
    print("\nMale heart atttacks: " + male_percent_noation)
    print("Female heart atttacks: " + female_percent_notaion)
    
    
    labels = 'Male', 'Female'
    sizes = [m_heart_attacks, f_heart_attacks]
    
    fig1, ax1 = plt.subplots()
    
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    
    ax1.axis('equal')
    ax1.set_title('Heart Attack Ratio between Male & Female')
    
    # fig1 = plt.figure()
    plt.show()
    fig1.savefig('Gender.png')
    
    
def getEKG():
    #EKG = 0
    df_0 = df.loc[(df.restecg == 0) & (df.attack == 1)]
    df_00 = df.loc[(df.restecg == 0) & (df.attack == 0)]
    zero_attack = len(df_0)
    zero_no_attack = len(df_00)
    zero_total = zero_attack + zero_no_attack 
    
    #EKG = 1
    df_1 = df.loc[(df.restecg == 1) & (df.attack == 1)]
    df_11 = df.loc[(df.restecg == 1) & (df.attack == 0)]
    one_attack = len(df_1)
    one_no_attack = len(df_11)
    one_total = one_attack + one_no_attack
    
    #EKG = 2
    df_2 = df.loc[(df.restecg == 2) & (df.attack == 1)]
    df_22 = df.loc[(df.restecg == 2) & (df.attack == 0)]
    two_attack = len(df_2)
    two_no_attack = len(df_22)
    two_total = two_attack + two_no_attack
   
    zero_percent_notaion = "{:,.2f}%".format(zero_attack/zero_total*100)
    one_percent_notation = "{:,.2f}%".format(one_attack/one_total*100)
    two_percent_notation = "{:,.2f}%".format(two_attack/two_total*100)
    
    print("\nEKG type:")
    print("\t0 - EKG was normal")
    print("\t1 - EKG had an abnormality with ST-T Wave")
    print("\t2 - EKG had an abnormality in the Left ventricular")
    print("Resting EKG Type 0 had this percent of heart attack: " + zero_percent_notaion)
    print("Resting EKG Type 1 had this percent of heart attack: " + one_percent_notation)
    print("Resting EKG Type 2 had this percent of heart attack: " + two_percent_notation)
    
    data = {'Normal':zero_attack/zero_total*100, 'Abnormal ST-T Wave':one_attack/one_total*100, 'Abnormal Left Ventricular': two_attack/two_total*100}
    courses = list(data.keys())
    values = list(data.values())
    
    fig1 = plt.figure(figsize = (10, 5))
    plt.bar(courses, values, color ='brown', width = 0.5)
    plt.xlabel("EKG Type")
    plt.ylabel("Percent")
    plt.title("Percent Heart Attack by Resting EKG")
    
    
    plt.show()
    fig1.savefig('EKG.png')
    
    
def getExercise():
    exang_val_counts = df.groupby("exng")["attack"].value_counts()
    
    exang_heart_attack = (exang_val_counts[1][1] / (exang_val_counts[1] [1] + exang_val_counts[1][0]))
    no_exang_heart_attack = (exang_val_counts[0][1] / (exang_val_counts[0][1] + exang_val_counts[0][0]))
    
    #Percentage for Positive                         
    e_percent_notation = "{:,.2f}%" .format(exang_heart_attack*100)
    ne_percent_notation = "{:,.2f}%" .format(no_exang_heart_attack*100)
    
    print("\nPercent who Exercised and had heart attack: " + e_percent_notation)
    print("Percent with No Exercise and had a heart attack: " + ne_percent_notation)  
    
    #bar chart
    data = {'Yes':exang_heart_attack*100, 'No':no_exang_heart_attack*100}
    
    #graph inputs
    courses = list(data.keys())
    values = list(data.values())
    
    fig1= plt.figure(figsize = (10, 5))
    plt.bar(courses, values, color ='purple', width = 0.7)
    plt.xlabel("Exercise")
    plt.ylabel("Percent Heartattack")
    plt.title("Percent Heart Attack if Exercising")
   

    #draw
    plt.show()
    fig1.savefig('Exercise.png')
    
    
               
