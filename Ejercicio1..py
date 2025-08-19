import math

num1=int(input("Dame un número entero: "))
num2=float(input("Dame un número decimal: "))

#Hipotenusa de un triángulo rectángulo con catetos
h = math.hypot(num1, num2)
print("Hipotenusa" ,h)

#Constantes
print("Número pi: ",math.pi)
print("Número e: ",math.e)

#Potencias y raíces
print("Raíz cuadrade de num1" ,math.sqrt(num1))
print("Raíz cuadrada de num1" ,num1**(0.5))

print("Cubo de num2" ,math.pow(num2, 3))
print("Cubo de num2" ,num2**3)

if(num1>num2):
    diferencia=num1-num2
    print("Num1 es mayor que Num2")
elif(num1<num2):
    print("Num2 es mayor que Num1")
else:
    print("Num1 igual que Num2")