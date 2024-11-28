
#la forma para ingresar valores a python es con la instruccion input
num = int(input("Ingresa un valor: "))
edad = 0


#en las siguientes lienas realizan una comparacion con un if anidado
if num>500:
    print("Es mayor que 500")
elif num>100:
    print("Es menor que 500 y mayor que 100")
else:
    print("Es menor que 100")


if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")


num = 42

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")