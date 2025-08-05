"""                    Tarea de investigación adicional

Investigue y prepare una nota breve sobre los siguientes temas:
• Operadores lógicos en Python: and, or, not.
• La estructura condicional if, elif y else.
Por favor realice tres ejemplos en Python """


# operdores logicos en python
# and, or, not

# and: devuelve True si ambos operandos son verdaderos


edad = 20
es_mayor = edad > 18 and edad < 65  # True


# or: devuelve True si al menos uno de los operandos es verdadero

tiene_licencia = True
tiene_permiso = False
puede_conducir = tiene_licencia or tiene_permiso  # True



# not: invierte el valor de verdad del operando

es_menor = not(edad > 18)  # False


# Estructura condicional if, elif y else
# if: se ejecuta si la condición es verdadera
if edad >= 18:
    print("Eres mayor de edad")
# elif: se ejecuta si la condición del if es falsa y la condición del elif es verdadera
elif edad >= 13:
    print("Eres un adolescente")
# else: se ejecuta si todas las condiciones anteriores son falsas
else:
    print("Eres un niño")
