import random 
def digit(num):
    return [int(i) for i in str(num)]   
def duplicate(num):
    num= digit(num)
    if len(num) == len(set(num)):
        return True
    else:
        return False    
def generatenum():
    while True:
        num = random.randint(1000,9999)
        if duplicate(num):
            return num
def cowbull(num,guess):
    bull_cow = [0,0]
    num1= digit(num)
    guess1= digit(guess)
    for i,j in zip(num1,guess1):
        if j in num1:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow
num = generatenum()
tries=int(input('Enter number of tries: '))
while tries > 0:
    guess = int(input("Enter your guess: "))
      
    if not duplicate(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
      
    bull_cow = cowbull(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries-=1
      
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")