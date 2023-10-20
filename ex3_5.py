def gcd(x, y):
    if x>y:
        mini=y
    else:
        mini=x
    for i in range(1,mini+1):
        if(x%i==0) and (y%i==0):
            gccd=i
    return gccd

number1=int(input("please enter first number:"))
number2=int(input("please enter second number:"))
bmm=gcd(number1,number2)
print("the gcd is:", bmm )

