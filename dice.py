import random

user_number = int(input("Enter number between 2-12: "))

number_1 = random.randint(1, 6)
number_2 = random.randint(1,6)

number_3 = random.randint(1, 6)
number_4 = random.randint(1,6)

number_5 = random.randint(1, 6)
number_6 = random.randint(1,6)

roll_1 = number_1 +number_2
roll_2 = number_3 +number_4
roll_3 = number_5 +number_6

print ("First roll: ",'\t',number_1, number_2)
print ("Second roll: ",'\t',number_3, number_4)
print ("Third roll: ",'\t',number_5, number_6)

if roll_1 == user_number:
    print ("Winner")
    
elif roll_2 == user_number:
    print ("Winner")
    
elif roll_3 == user_number:
    print ("Winner")
    
else:
    print ("You loose. Play again?")
