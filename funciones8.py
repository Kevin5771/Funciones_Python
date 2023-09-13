#Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. 
#En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. 
#Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def contar_caracteres(cadena):
  """Cuenta la cantidad de caracteres en una cadena."""
  return len(cadena)


def main():
  """Solicita la carga de dos nombres por teclado y llama a la función dos veces. 
  Imprime en el bloque principal cual de las dos palabras tiene más caracteres."""

  nombre1 = input("Ingrese el primer nombre: ")
  nombre2 = input("Ingrese el segundo nombre: ")

  caracteres1 = contar_caracteres(nombre1)
  caracteres2 = contar_caracteres(nombre2)

  if caracteres1 > caracteres2:
    print(f"{nombre1} tiene más caracteres que {nombre2}.")
  elif caracteres1 < caracteres2:
    print(f"{nombre2} tiene más caracteres que {nombre1}.")
  else:
    print(f"{nombre1} y {nombre2} tienen la misma cantidad de caracteres.")


if __name__ == "__main__":
  main()