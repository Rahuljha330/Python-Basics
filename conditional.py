import sys
import math
import random
import threading
import time
from functools import reduce





'''age = input("Enter your age man:")
print("so your age is " , age)
if age is 20:
    print("Bro you can drive")

else:
    print("YOu can't drive")
'''
# guys jus fucking frickin can't understand the above code
# lets try the below and maybe i guess that will be hell easy.lets do this

age = 18.5
if age < 5:
    print("Go to home")
elif (age >= 5)and  (age <=6):
    print("hell go to KG")
elif (age > 6) and (age <= 17):
    print("Grade",(age - 5))
elif (age > 20):
    print("you have possibly completed school")
else:
    print("College")

# now this is jus the same

canVote = True if age >= 18 else False
print(canVote)

