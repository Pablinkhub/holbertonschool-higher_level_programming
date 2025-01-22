#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ultimo_Digito = number % 10 if number >= 0 else number % -10

if Ultimo_Digito > 5:
    mensaje = "and is greater than 5"
elif Ultimo_Digito == 0:
    mensaje = "and is 0"
else:
    mensaje = "and is less than 6 and not 0"

print (f"Last digit of {number} is {Ultimo_Digito} {mensaje}")