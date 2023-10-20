A= input("please enter number and participate them with cama (,)")
array=[int(x) for x in A.split(",")]
x=True
for i in range(len(array)-1):
    if array[i] <= array[i+1]:
        continue
    else:
        x=False
        break


if x:
     print ("the array is sorted ") 
else:
     print("the array is not sorted")

        








