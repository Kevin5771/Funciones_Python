#Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.

def cargar():
    lista=[]
    for x in range(10):
        valor= int (input("Ingresa un valor: "))
        lista.append(valor)
    return(lista)

def imprimir_lista(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


#Bloque Principa
lista=cargar()
imprimir_lista(lista)