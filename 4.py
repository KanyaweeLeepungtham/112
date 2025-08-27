mynum = int(input())
num = input()
lista = list(map(int, num.split()))
def median(x):
    n = len(x)
    mid = n // 2
    if n % 2 != 0:
        return x[mid]
    else:
        return (x[mid - 1] + x[mid]) / 2
print("%.2f" %median(lista))