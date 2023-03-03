# Cual de 3 número es mayor

print("---------------------------------")
print("---------Mayor o menor-----------")
print("---------------------------------")

# input
a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
c = int(input("Digite el tercer número: "))

# processing and output

if a > b and a > c:
    print("El número "+str(a)+" es mayor que "+str(b)+" y que "+str(c))
elif b > a and b > c:
    print("El número "+str(b)+" es mayor que "+str(a)+" y que "+str(c))
else:
    print("El número "+str(c)+" es mayor que "+str(a)+" y que "+str(b))

print("---------------------------------")