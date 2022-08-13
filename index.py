def adicion(numero_1, numero_2):
    return numero_1 + numero_2

def sustraccion(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2

def division(numero_1, numero_2):
    return numero_1 / numero_2

def menu_opciones():
    print("BIENVENIDO A LA CALCULADORA")
    print("1. ADICION")
    print("2. SUSTRACCION")
    print("3. MULTIPLICACION")
    print("4. DIVISION")

numero_1 = float(input("Ingrese un primer numero: "))
numero_2 = float(input("Ingrese un segundo numero: "))

menu_opciones()
opcion = int(input("Ingrese el numero de la opcion requerida: "))

while opcion < 1 or opcion > 4:
    menu_opciones()
    opcion = int(input("Ingrese el numero de la opcion requerida: "))

if opcion == 1:
    print(f'La adicion de los numeros es: {adicion(numero_1, numero_2)}')
elif opcion == 2:
    print(f'La sustraccion de los numeros es: {sustraccion(numero_1, numero_2)}')
elif opcion == 3:
    print(f'La multiplicacion de los numeros es: {multiplicacion(numero_1, numero_2)}')
elif opcion == 4:
    print(f'La division de los numeros es: {division(numero_1, numero_2)}')

repeticion = int(input("¿Desea realizar otra operacion? 1 -> SI | 2 -> NO : "))

while(repeticion == 1):
    numero_1 = float(input("Ingrese un primer numero: "))
    numero_2 = float(input("Ingrese un segundo numero: "))

    menu_opciones()
    opcion = int(input("Ingrese el numero de la opcion requerida: "))

    while opcion < 1 or opcion > 4:
        menu_opciones()
        opcion = int(input("Ingrese el numero de la opcion requerida: "))

    if opcion == 1:
        print(f'La adicion de los numeros es: {adicion(numero_1, numero_2)}')
    elif opcion == 2:
        print(f'La sustraccion de los numeros es: {sustraccion(numero_1, numero_2)}')
    elif opcion == 3:
        print(f'La multiplicacion de los numeros es: {multiplicacion(numero_1, numero_2)}')
    elif opcion == 4:
        print(f'La division de los numeros es: {division(numero_1, numero_2)}')

    repeticion = int(input("¿Desea realizar otra operacion? 1 -> SI | 2 -> NO : "))
else:
    print("GRACIAS POR USAR LA CALCULADORA, ADIOS")

