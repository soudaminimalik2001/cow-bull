import random
list=[0,1,2,3,4,5,6,7,8,9]
list2=random.sample(list,5)
print(list2)
for i in range(10):
    n=int(input("enter number"))
    index=int(input("enter index"))
    bull=[]
    cow=[]
    for j in range(len(list2)):
        if n in list2:
            if index==list2[i]:
                bull.insert(n)
                print(bull)
        elif n not in list2:
            cow.append(n)
            if index==i:
                cow.append(index)
if list2==bull:
    print("congratulation you are the winner")
else:
    print("opps you are the looser")
    
    
    # random.sample
    
    
    
    
