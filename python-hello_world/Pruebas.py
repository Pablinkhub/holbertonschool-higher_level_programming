#!/usr/bin/env python3
import sys
import inspect

# Definición de las funciones de prueba
def prueba1():
    print("Esta prueba es un simple print, string de texto")
    print("Holberton school")

def prueba2():
    mensaje = (
        f"(Esta prueba es un print en el que se utiliza un f-string)\n"
        f"Una f-string, en Python, es una forma de formatear cadenas de texto que te permite incrustar\n"
        f"expresiones directamente dentro de la cadena. El prefijo f antes de las comillas indica que la\n"
        f"cadena es una formatted string (cadena formateada). Las expresiones, como variables o cálculos\n"
        f"se colocan dentro de llaves {{}} y se evalúan y convierten a texto automáticamente cuando se ejecuta\n"
        f"el código. Esto hace que sea muy fácil y eficiente combinar texto estático con datos dinámicos)\n"
        f"Por ejemplo:\n"
        f"{98} Battery street\n"
        f"En la prueba numero 3 se da un ejemplo practico de esto" 
    )
    print(mensaje)
def prueba3():
    productos = [29.99, 15.99, 49.95, 5.99]
    subtotal = sum(productos)
    impuesto = subtotal * 0.08
    total = subtotal + impuesto
    print(f"El total de tu compra, incluyendo impuestos, es ${total:.2f}")

def prueba4():
    print("Esta prueba tan solo es un ejemplo de un numero común (98) en un string de texto dentro de un print sin utilizar un f-sting:")
    print("98 Battery Street")
    print("Como verás, es aparentemente igual a lo visto en la prueba 2, sin embargo es un string estatico (No puede variar su resultado)")

def prueba5():
    print("Tan solo otro ejemplo de como se utilizan los f-string")
    print(f"{98} Battery street, {'San Francisco'}")

def prueba6():
    a = "Python is cool"
    print(a[4])
    print("En este caso estamos aplicando una función de python que nos permite imprimir un caracter especifico de un string de texto archivado en una variable")
    print("Es importante recordar que python cuenta el primer caracter como la posición 0, no 1")

def prueba7():
    a = "Python is cool"
    print (a[0:6])
    print ("En este caso aprendemos que se puede utilizar el mismo metodo para imprimir sectores marcados de una cadena de texto")
    print ("Tambíen note que las variables de diferentes 'funciónes' son independientes entre sí, es decír si marcaste una variable a en la 'función' 'prueba6'")
    print ("deberás volver a marcarla en la 'función' 'prueba7' ya que dentro de esta, no existirá")

def prueba8():
    a = "Python is cool"
    print(a[:6])
    print("Mas de lo mismo, aparentemente dejar vacio un de los dos lados de los ':' es como decirle al programa que imprima todo lo que pueda hacía el lado vacio")
    
def prueba9():
    a = "Python is cool"
    print(a[7:-5])
    print("Es rotundo que esta es tan solo una forma de marcar parametros, es mas facil imaginarlo ocmo una rueda marcada")

def prueba10():
    a = "Python is cool"
    print(a[-2])
    print("Tan solo una reafirmación de lo dicho en la prueba 9")
    
    
    
    
    
    
# Función para obtener automáticamente todas las funciones de prueba
def obtener_pruebas():
    pruebas = {} #Iniicalizo diccionario
    funciones = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    for nombre, funcion in funciones:
        if nombre.startswith("prueba"):  # Todo nombre de prueba debe comenzar con prueba4
            pruebas[nombre] = funcion
    return pruebas

if __name__ == '__main__':
    pruebas = obtener_pruebas()
    if len(sys.argv) < 2:
        print("Por favor, indica el número de prueba a ejecutar.")
        print("Pruebas disponibles:")
        for key in pruebas.keys():
            print(key)
    else:
        prueba_nombre = f"prueba{sys.argv[1]}"
        if prueba_nombre in pruebas:
            pruebas[prueba_nombre]()
        else:
            print("Número de prueba no válido. Pruebas disponibles:")
            for key in pruebas.keys():
                print(key)