import random

n=int(input("enter size of array"))
random_numbers=[]

for x in range(n):
    random_numbers.append(random.randint(1,1000))


print("the array is: ", "[", random_numbers,"]")

