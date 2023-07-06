import random
t = 0
targetNum = random.randrange(1,100)
print("Welcome to guess a number game. There will be 3 chance to guess the number.")
while(t<3):
    storedNum = str(input("Hey! guess two digit number: "))
    if(storedNum == targetNum):
        print("Congratulations! your guess is right.")
    else:
        print("Oops! you have failed.")
    
    t += 1

print("The Number is: "+str(targetNum))
