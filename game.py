from random import choice, randrange
from datetime import datetime
operators = ["+", "-", "*", "/"]
times = 5
aciertos = 0
fallos =0 
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  if(operator=='+'):
    num3=number_1 + number_2
  elif(operator=='-'):
      num3=number_1 - number_2
  elif(operator=='/'):
    num3=number_1 / number_2
  else:
    num3=number_1*number_2
  result = input("resultado: ")
  print(result)
  if(int(result)==num3):
    print("El resultado introducido es correcto! :D")
    aciertos=aciertos+1
  else:
    print("El resultado introducido es incorrecto D:")
    fallos=fallos+1
  end_time = datetime.now()
  total_time = end_time - init_time
  print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"Cantidad de aciertos:{aciertos}")
print(f"Cantidad de fallos:{fallos}")