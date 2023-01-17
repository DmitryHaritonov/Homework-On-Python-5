#def sum(a, b):
#    if a == 0 or b == 0:
#        return a and b
#    else:
#        if a > 0 and b > 0:
#            return sum((a + 1)+(b - 1))
#a = int(input("Введите число a: "))
#b = int(input("Введите число b: "))
#print(sum(a, b))

#def summa(a, b):
#    a += 1
#    b -= 1
#    if b > 0:
#        return summa(a, b)
#    else:
#        return a
# 
# 
#print (summa(3, 5))

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
 
 
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
 
 
print(sum(a, b))