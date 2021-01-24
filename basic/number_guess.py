import random
import math

upperBound = int(input("Enter upper limit\t:"))
lowerBound = int(input("Enter lower limit\t:"))

x = random.randint(lowerBound , upperBound)
chance = round(math.log(upperBound - lowerBound + 1,2))
print("\nYou have ",str(chance)," chances to guess!\n")

count = 0

for i in range(chance):
    count = count + 1
    guess = int(input("Guess :"))

    if x == guess:
        print("Congrats you guessed it in",count)
        break
    elif x > guess:
        print("You need to guess higher next time")
    elif x < guess:
        print("You need to guess smaller next time")

if count >= chance:
    print("\nThe number was ",x)

