
# i =0
# while i<20:
#     print("hello", i)
#     j = 0
#     while j < 2:
#         print(j)
#         j = j+1
#     i = i+ 1

# i = 0

# for i in range(9):

    # print(i)




# # odd Number print without condition

# for i in range(0,100,2):
#     print(i, end=" ")



# 4 cube

# for i in range(0,4):
#     for j in range(0,4):
#         print("#", end=" ")
    
#     print("")


##### create triAngle



# for i in range(0,10):
#     for j in range(0,i):
#         print("#", end=" ")
#     print("")


# output

# 
# #
# # #
# # # #
# # # # #
# # # # # #
# # # # # # #
# # # # # # # #
# # # # # # # # #


# for i in range(0,10):
#     for j in range(i,10):
#         print(end=" ")
#     for j in range(i):
#         print("#",end=" ")
#     print("")


# output

         # 
        # #
       # # #
      # # # #
     # # # # #
    # # # # # #
   # # # # # # #
  # # # # # # # #
 # # # # # # # # #





# ##### filter even nummer
# nums = [10,130,4,5,55,89,90,100,2,103,10]

# for i,value in enumerate(nums):
#     if value% 3 == 0:
#         print(i, value)




# then he

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print(alpha[0])

str = "NAZRUL"
newStr = ""

for i in range(len(str)):
    for j in range(len(alpha)):
        if(str[i] == alpha[j]):
            # print(j)
            newStr = newStr + alpha[(j+3)%26]
            break


print(newStr)