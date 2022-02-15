import random
list2=random.randint(1000,9999)
print(list2)
user=int(input("enter 4 digit:"))
guess=[]
listnum=[]
def game():
    c=0
    while True:
        for i in list2:
            guess.append(i)
        for i in user:
            listnum.append(i)
        if guess==listnum:
            print("you won")
            print("it took you"+str()+"guess")
            break
        if guess!=listnum:
            cow=0
            bull=0
            c+=1
            for x in range(0,4):
                if guess[x]==listnum[x]:
                    cow+=1
        if len(set(guess)&set(listnum))>listnum:
            bull=len(set(guess)&set(listnum))-cow
        # print("cow:"+(cow)+'bull:'(bull))
game()