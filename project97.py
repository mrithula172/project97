import random
print ("NUMBER GUESSING GAME")
n=random.randint(1,9)

chance=0
print("guess a number between 1 and 9")

while chance<5:
    guess=int(input("enter your guess"))
    if guess==n:
        print("Congratulations you won")
        break
    elif guess<n:
        print("your guess was too low")
    else:
        print("your guess was too high")
    chance=chance+1

if chance==5:
    print("YOU LOSE,The Number Is",n)
        
