import re
import Task
import JSONHandler
from pprint import pprint


tareaActual = None
def main():
  JSONHandler.loadJSON()
  data = JSONHandler.file_data
  for x in data["open tasks"]:
    pprint(x)
  while True:
    printInitialMenu()
    inp = input()
    if inp == "3":
      print("Saliendo del programa\n")
      break
    elif inp == "2":
      loadTask("CARGAR")
    elif inp == "1":
      newTask()
    

def printInitialMenu():
  print("    **SEGUIMIENTO MINUTAS**")
  if(tareaActual != ""):
    print("\n ID Tarea cargada: {}".format(tareaActual))
  else:
    print("\n No hay ninguna tarea cargada")
    
  print("\n\t 1- Nueva tarea.")
  print("\n\t 2- Cargar tarea.")
  print("\n\t 3- Cerrar.")


def newTask():
  global tareaActual
  print("\n NUEVA TAREA")
  while True:
    while True:
      print("Escriba ID de la tarea: ")
      expediente = input()
      s = re.search("\d{12}", expediente)
      if (len(expediente) == 12) and (s.string == expediente):
        break
      else:
        print("Formato incorrecto.")
    print("¿Desea crear la tarea {t}?".format(t=expediente))
    r = input()
    if r == "SI":
      tareaActual = Task(expediente)
      break


def loadTask():
  global tareaActual
  print("\n CARGAR TAREA")
  while True:
    while True:
      print("Escriba ID de la tarea: ")
      expediente = input()
      s = re.search("\d{12}", expediente)
      if (len(expediente) == 12) and (s.string == expediente):
        break
      else:
        print("Formato incorrecto.")
    print("¿Desea cargar la tarea {t}?".format(t=expediente))
    r = input()
    if r == "SI":
      tareaActual = Task(expediente)
      tareaActual.load_from_file()
      break
  

if __name__ == "__main__":
  main()