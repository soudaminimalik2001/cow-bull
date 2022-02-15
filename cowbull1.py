import random
list=[0,1,2,3,4,5,6,7,8,9]
list2=random.sample(list,5)
print(list2)
for i in range(len(list2)):
    # print(i)
    # print(list2[i])
    n=int(input("enter number"))
    # 
    # position=int(input("enter index"))
    bull=[]
    cow=[]
    if n in list2:
        bull.append(n)
        print(bull)
    else:
        cow.append(n)
        print("these are correct number you can reuse",cow)
if list2==bull:
    print("congratulation you are the winner")
else:
    print("opps you are the looser")
        
