num = int(input("Enter the number of elements in an array :"))
arr = []
for i in range(num):
    arr.append(int(input(f"Enter the {i+1} element of an array : ")))
    
min_num = arr[0]
for i in range(1,num):
    if arr[i]<min_num :
        min_num = arr[i]

print(f"The smallest number in the array {arr} is " , min_num)