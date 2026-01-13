# arr = [1,2,3,4,5]

# # Length
# # print(len(arr))  # 5

# # # Append
# # arr.append(6)

# # # Remove
# # arr.remove(3)

# # Iterate
# for i in arr:
#     print(i)


# arr = [10,20,30,40,50]

# print(arr[0])    # 10
# print(arr[-1])   # 50
# print(arr[1:4])  # [20,30,40]


n = int(input('enter the length of array: '))

array = []

for i in range(0,n):
    x = int(input('enter array element: '))
    array.append(x)

print(array)
