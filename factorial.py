

# def fact(n):
#     x = 1
#     while(n>0):
#         x = x*n
#         n = n-1
#         # print(n,x)
#     print(x)




# def fact(n):
#     if(n == 0):
#         return 1
#     return n* fact(n-1)


# print(fact(5))

is_even = lambda x: x % 2 == 0
print(is_even(4))  # True

nums = [1, 2, 3, 4, 5]


# filter(function, iterable)

even = list(filter(lambda x: x%2 == 0,nums))
# print(even)


# map(function, iterable)

double = list(map(lambda x: x*2, nums))
# print(double)

# print(33*9/60)


from functools import reduce

nums = [1, 2, 3, 4]
sum = reduce(lambda a,b: a+b, nums)
print(sum)
