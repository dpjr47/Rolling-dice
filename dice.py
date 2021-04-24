import random   

a=1
b=6




roll = 'r'

while roll in 'r':
    n = int(input("Enter the number of dices to roll : "))
    print("Rolling the dices...")
    print("The values are...")
    i = 1
    while (i < n):
        print("dice", i , ":" , random.randint(a,b))
        i= i + 1
    roll = input("Enter r to roll the dices again \n")

