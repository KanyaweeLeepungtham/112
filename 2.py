menu=[25,30,35]
mynum =3
num =[]
total =0
for i in range(mynum):
    cup = int(input())
    num.append(cup)
for i in range(mynum):
    total = sum(total + (menu[i] * num[i]))
if (total>=300):
    total= sum*(95/100)
elif(cup>=10):
    total= sum*(90/100)
else:print(total)