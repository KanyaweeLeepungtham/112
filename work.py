num = []
mynum = int(input())
for i in range(mynum):
    a = int(input())
    num.append(a)
def prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
for number in num:
    if number%2 != 0 or prime(number)==True:
        print('T')
    else: print('F')