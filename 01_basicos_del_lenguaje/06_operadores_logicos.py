x = 2
y = 3

print(x == y)

y = 2

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 2
y = 3
a = 5
b = 7

print((x < y) and (a < b)) 
print((x < y) and (a > b))
print((x < y) or (a < b)) 

if x < y :
    print(f"El valor {x} es menor que {y}")
else:
    print(f"El valor {x} no es menor que {y}")