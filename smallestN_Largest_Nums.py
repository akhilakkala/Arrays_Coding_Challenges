num = int(input("Enter the number of elements in an array :"))
print("Enter elements of an array")
arr = []
for i in range(num):
    arr.append(int(input(f"Enter the {i+1} element of an array : ")))
min_num = arr[0]
max_num = arr[0]
for i in range(1,num):
    if(arr[i]<min_num):
        min_num = arr[i]
    if(arr[i]>max_num):
        max_num = arr[i]

print(f"The smallest and largest numbers in the array {arr} are {min_num} and {max_num} respectively")

