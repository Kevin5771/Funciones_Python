# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad 
# (mayores o iguales a 18 años)
# Imprimir la edad promedio de las personas.
# Crear una función para cargar los nombres y edades
def cargar_dato():
    nombres = [] 
    edades = []  
    for x in range(5):
        v1 = input("Ingrese el nombre de la persona: ")
        nombres.append(v1)
        v2 = int(input("Ingrese la Edad: ")) 
        edades.append(v2)

    return (nombres, edades)


def mayores_edad(nombres, edades):
    print("Nombres de personas mayores de edad:")
    for x in range(len(nombres)):
        if edades[x] >= 18:
            print(nombres[x])

# Crear una función para calcular y imprimir la edad promedio de las personas
def promedio_edades(edades):
    suma = sum(edades)         
    promedio = suma / len(edades)  
    print("Edad promedio de las personas:", promedio)

# Bloque principal

nombres, edades = cargar_dato()
mayores_edad(nombres, edades)
promedio_edades(edades)