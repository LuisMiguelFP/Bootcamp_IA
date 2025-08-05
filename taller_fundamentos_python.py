"""
                                 taller_fundamentos_python.py

         Nombre : Luis Miguel Franco Perez

         codigo : 56068

         Docente : Julian buitrago 

"""

"""
    1. Solicite al usuario su nombre y edad. Luego imprima un saludo personalizado
       indicando cuántos años tendrá en su próximo cumpleaños.
"""


""" nombre = input("ingrese su nombre completo : ")
edad = int(input ("ingrese su edad : "))
print (f"hola {nombre},el proximo año tendras {edad +1} años de edad")
 """






"""
2. Pida dos números enteros y muestre la suma, resta, multiplicación, división y
módulo de esos números.
"""


""" num1 = int(input ("ingrese un numero entero : "))
num2 = int(input ("ingrese el otro numero entero : "))

ops = input ("con estos dos numeros que operacion desea realizar (+,-,*,/,%) : ")
if ops == "+":
    print (f"el total de la suma es : {num1+num2}")

elif ops == "-":
    print (f"el total de la resta es {num1-num2}")
elif ops == "+":
    print (f"el total de la multiplicacion es {num1*num2}")
elif ops == "/":
    print (f"el total de la division es {num1/num2}")
elif ops == "%":
    print (f"el residuo de la division es {num1%num2}")
 """

"""
3. Calcule el área de un triángulo pidiendo la base y la altura al usuario.
"""



""" base = float(input("ingrese la base del triangulo : "))
altura = float(input("ingrese la altura del triangulo : "))

area = (base * altura) / 2
print (f"el area del triangulo es : {area}")
 """


"""
4. Reciba un número entero e imprima su tabla de multiplicar del 1 al 10.
"""
""" num = int(input("infrese un numero para generar su tabla de multiplicar : "))
for i in range (1,10):
    print (f"{num} x {i} = {num*i}")
 """


"""
5. Solicite un texto y muestre cuántos caracteres contiene sin contar los espacios.
"""""" 
texto = input("ingrese un texto : ")
texto_sin_espacios = texto.replace(" ","")
print (f"el texto ingresado tiene {len(texto_sin_espacios)} caracteres sin contar los espacios") """
"""


6. Pida al usuario su peso en kilogramos y su estatura en metros; calcule e imprima su
índice de masa corporal (IMC).
"""


""" peso = float(input("ingrese su peso en kilogramos : "))
estatura = float(input("ingrese su estatura en metros : "))
imc = peso / (estatura ** 2)
 
print(f"su indice de masa corporal es : {imc:.2f}")
 """
"""
7. Convierta una cantidad de grados Celsius ingresada por el usuario a Fahrenheit.
"""
""" grados = float(input("ingrese la temperatura en grads celsius : "))

total = (grados *9)/5 +32

print(f"{grados} grados celsius son {total} grados fahrenheit")
 """

"""
8. Inicialice tres variables con distintos tipos de datos (str, int, float) y muestre el tipo
de cada una usando la función type().
"""
""" var1 = "hola profe julian buitrago"
var2 = 2025
var3 = 3.14

print(type(var1))
print(type(var2))
print(type(var3))   
 """

"""
9. Pida al usuario un número entero y muestre el resultado de elevarlo al cubo.
"""
""" num = int(input("ingrese un numero entero : "))
print(f"el resultado de elevar {num} al cubo es : {num**3}") """
"""
10. Convierta una cantidad de segundos ingresada por el usuario a horas, minutos y
segundos
"""
segundos = int(input("ingrese la cantidad de segundos : "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")