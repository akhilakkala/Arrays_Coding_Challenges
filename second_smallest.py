import math
n1 = math.inf
n2 = math.inf
num = int(input("Enter the number of elements in an array :"))
arr = []
for i in range(num):
    arr.append(int(input(f"Enter the {i+1} element of an array : ")))
    
for i in range(0,len(arr)):
    if(arr[i]<n1):
        n2=n1
        n1=arr[i]
    elif(arr[i]<n2 and arr[i]!=n1):
        n2 = arr[i]
        
print(f"The second smallest number in the array {arr} is {n2}")
  