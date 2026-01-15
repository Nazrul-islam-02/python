

# def fact(n):
#     x = 1
#     while(n>0):
#         x = x*n
#         n = n-1
#         # print(n,x)
#     print(x)




def fact(n):
    if(n == 0):
        return 1
    return n* fact(n-1)


print(fact(5))