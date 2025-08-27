# # num = int(input())
# # a = 0
# # while num > 0:
# #     num=num / 10  
# #     a = a+ 1
# # print(a)

# num=[]
# mynum= int(input())
# if (mynum >= 10):
#     break
# else:
#     for i in range(mynum):
#         a = int(input())
#         num.append(a)
#     odd = (mynum % 2 != 0)
#     prime = True
#     for i in range(mynum):
#         if a < 2:
#             prime = False
#         else:
#             for j in range(2, mynum):
#                 if mynum % j == 0:
#                     prime = False
#                     break
#         if odd and prime:
#             print('T')
#         else:
#             print('F')

a= int(input())
b=int(input())
c= int(input())
cup = a+b+c
menu =[25*a, 30*b,35*c]
total = sum(menu)
if (total>=300):
    total= total * 95//100
elif(cup>=10):
    total= total * 90//100
else:print(total)