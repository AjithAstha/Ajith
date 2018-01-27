#program for snake and ladder
import random
count=0
while(count<=100):
    a=input("enter'r'to roll dice")
    if(a=='r'):
     r=random.randint(1,6)
     count=count+r
     print(r)
    if(count==8):
        count=37
        print("wow,you climbed the ladder",count)
    elif(count==11):
        count=2
        print("oops snake has bite you",count)
    if(count==13):
        count=34
        print("wow,you climbed the ladder",count)
    elif(count==25):
        count=4
        print("oops snake has bite you",count)
    if(count==38):
        count=9
        print("oops snake has bite you",count)
    elif(count==40):
        count=68
        print("wow u climbed the ladder",count)
    if(count==52):
        count=81
        print("wow u climbed the ladder",count)
    elif(count==65):
        count=46
        print("oops snake has bite you",count)
    if(count==76):
        count=97
        print("wow u climbed the ladder",count)
    elif(count==89):
        count=70
        print("oops snake has bite you",count)
    if(count==93):
        count=64
        print("oops snake has bite you",count)
    if(count==100):
        count=100
        print("you win")
    elif(count>100):
        print("try again")
        
