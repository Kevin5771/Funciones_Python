#Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. 
#Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.

def calcular_sueldo(nombre, pago_por_hora, horas_trabajadas):
  """Calcula el sueldo de un operario.

  Args:
    nombre: El nombre del operario.
    pago_por_hora: El pago por hora del operario.
    horas_trabajadas: El número de horas trabajadas por el operario.

  Returns:
    El sueldo del operario.
  """

  sueldo = pago_por_hora * horas_trabajadas
  return sueldo


if __name__ == "__main__":
  nombre = input("Nombre del operario: ")
  pago_por_hora = float(input("Pago por hora: "))
  horas_trabajadas = float(input("Horas trabajadas: "))

  sueldo = calcular_sueldo(nombre, pago_por_hora, horas_trabajadas)

  print(f"El sueldo de {nombre} es {sueldo}")