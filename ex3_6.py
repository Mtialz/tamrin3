def gcd(x, y):
    if x>y:
        mini=y
    else:
        mini=x
    for i in range(1,mini+1):
        if(x%i==0) and (y%i==0):
            gccd=i
    return gccd

def lcm(a, b): 
    result=a*b // gcd(a, b)
    return result

num1=(input("please enter first number:"))
num2=(input("please enter second number:"))
kmm=lcm(num1, num2)
print("the lcm is :", kmm)