from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
aciertos = 0
errores = 0
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    result = input("resultado: ")
    match operator:
        case "+":
            correcto = str(number_1 + number_2)
        case "-":
            correcto = str(number_1 - number_2)
        case "*":
            correcto = str(number_1 * number_2)
        case "/":
            correcto = str(number_1 / number_2)
    if result ==  correcto:
        print("Bien")
        aciertos += 1
    else:
        errores += 1
        print ("La correcta era: ", correcto)

end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(" Acertaste: ", aciertos, " Te equivocaste: ",errores)