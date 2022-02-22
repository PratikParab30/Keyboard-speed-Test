import random as rd
import string
import keyboard as kb
import os
import time
import pickle


st=string.ascii_letters
st=list(st)

while True:
    name=input("\nEnter your name:")
    if name !=("" or " " or "\n"):
        break
    else:
        print("Re_Enter The name:")

while True:
    print("Select Difficulty Level: ")
    print("1.Easy")
    print("2.Medium")
    print("3.Advance")
    print("4.Master")
    ch=input("Enter a choice:")
    if ch=="1":
        dfc=3
        break
    if ch=="2":
        dfc=5
        break
    if ch=="3":
        dfc=7
        break
    if ch=="4":
        dfc=9
        break
    else:
        print("\nWrong choice,Try again!\n")

arr_word_time=[]       #used to store Word with respect time taken in Sec 
       
while True:     
    txt1=rd.choices(st,k=dfc)
    txt2=""
    for i in txt1:
        txt2=txt2+i
        
    print(f"the word is*****: {txt2}  :******")
    inp=""
    while True:
        print("\n1. for Exit from game Long press 'End+ESC' + Press_and_Release'Enter' buttons ")
        print("2.skip this word,and try new word, long press 'End' + Press_and_Release'Enter' buttons")
        t1=time.time()    #Time Counter start
        inp=input("Please Enter given Text: ")
        t2=time.time()    #Time Counter end
        t3=t2-t1          #total time Taken in Sec
        if kb.is_pressed("End"):
            break
        if(txt2==inp):
            arr1=[]        #temporary array
            arr1.append(txt2)
            arr1.append(t3)
            arr_word_time.append(arr1)
            print("\n"*2) 
            break
        else:
            print("\n"*2)
            print("******************************")
            print(f"\n!!Wrong Word!!, please reEnter {txt2}\n")
    
    if kb.is_pressed("Esc"):
        break 
    

    
print("Time Taken for Enter a words is ")  

tt=0  #for count Total time

for i in arr_word_time:
    print(f"{i[0]} :: {i[1]} Sec")
    tt=tt+i[1]

round_Diffculty=["Easy","Medium","Advance","Master"]
    
print(f"Total Time taken for {round_Diffculty[int(ch)-1]} Game is {tt}Sec")
print(f"And Average time taken is {tt/len(arr_word_time)}")

if os.path.exists("mygame.pkl"): 
    jlobj=open("mygame.pkl","rb")
    rf=pickle.Unpickler(jlobj).load()
    jlobj.close()
    
    jlobj=open("mygame.pkl","wb")
    arr2=[]
    
    arr2.append(name)
    arr2.append(round_Diffculty[int(ch)-1])
    arr2.append(len(arr_word_time))
    arr2.append(tt)
    arr2.append(tt/len(arr_word_time))
    rf.append(arr2)
    
    pickle.dump(rf,jlobj)
    
    jlobj.close()
    
    print("\nOld Player and Your Recard are:\n")
    for i in rf:
        stm=f" Name is:{i[0]} \n Level of dificulty is:{i[1]} \n total word cover is:{i[2]} \n total time taken is:{i[3]}Sec \n avarage time is:{i[4]}Sec\n"
        print(stm)
        
else:
    jlobj=open("mygame.pkl","wb")
    arr1=[]
    arr2=[]
    arr2.append(name)
    arr2.append(round_Diffculty[int(ch)-1])
    arr2.append(len(arr_word_time))
    arr2.append(tt)
    arr2.append(tt/len(arr_word_time))
    arr1.append(arr2)
    
    pickle.dump(arr1,jlobj)
    jlobj.close()
    print("\nYou are first player whose data stored:\n")
    for i in arr1:
        stm=f" Name is:{i[0]} \n Level of dificulty is:{i[1]} \n total word cover is:{i[2]} \n total time taken is:{i[3]}Sec \n avarage time is:{i[4]}Sec"
        print(stm,end="\n")
    