# import random
# # alpha=[]
# list1 = [1, 2, 3, 4, 5, 6]
# # print(random.choice(list1)
# print(random.choice(list))

# # import random
 
# # # prints a random value from the list
# # list1 = [1, 2, 3, 4, 5, 6]
# # print(random.choice(list1))
 
# prints a random item from the string
# string = "striver"
# print(random.choice(string))

import random
string = "striver"
print(random.choice(string))

rand=[random.randint(0,9) for n in range(3)]


user_guess=[input("Please guess 4-digit number: ")]

def game():
    count=0
    while True:
        guess=[i for i in rand]
        listnum=[i for i in user_guess]

        if guess == listnum:
            print("You won.")
            print("It took you "+str(count)+" guess.")
            break

        if guess != listnum:
            cow=0
            bull=0
            count+=1
            for x in range(0,5):
                if guess[x]==listnum[x]:
                    cow+=1

        if len(set(guess)&set(listnum))>listnum:
            bull=len(set(guess)&set(listnum)) - cow

        print("Cows: "+str(cow)+' Bulls: '+str(bull))

game()



# a=["a","b","c","d"]
# for i in range(len(a)):
#     print(a[i])
