num = int(input("Enter the number of elements in an array :"))
print("Enter elements of an array")
arr = []
for i in range(num):
    arr.append(int(input(f"Enter the {i+1} element of an array : ")))

maxi = 0
for i in range(num):
    maxi = max(arr[i],maxi)
print(f"The largest number in the array {arr} is " , maxi)
    