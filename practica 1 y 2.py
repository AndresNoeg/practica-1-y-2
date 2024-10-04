print(" ")
print("Gomez Garcia Andres Noe")
print(" ")
#Declaramos una lista
x=[43, 57, 92, 20, 37, 5, 9]
#Imprime un objeto de la lista segun el valor dado en los corchetes
print ("El menor es: ", x[5])
print("El mayor es: ", x[2])
#Deja un espacio entre lineas
print(" ")

#Declara una lista
y=["Programacion", "Leoye", "Metodologia", "Ingles", "Ecosistemas"]
#imprime lista
print(y)
#Deja un espacio
print(" ")
#Imprime la materia segun el valor dado entre corchetes
print("Estoy curando la materia de: ", y[0])
print("Estoy curando la materia de: ", y[1])
print("Estoy curando la materia de: ", y[2])
print("Estoy curando la materia de: ", y[3])
print("Estoy curando la materia de: ", y[4])



#Le pide a el usuario sus calificaciones
cal=list(input("ingrese sus calificciones en las materias anteriormente vistas: "))
print (y[0],"la calificacion es: ", cal[0])
print (y[1],"la calificacion es: ",cal[1])
print (y[2],"la calificacion es: ",cal[2])
print (y[3],"la calificacion es: ",cal[3])



# Inicializar la lista para los números ganadores
numerosg = []

# Solicitar al usuario que ingrese 5 números ganadores
num1 = int(input("Ingresa el primer número ganador: "))
num2 = int(input("Ingresa el segundo número ganador: "))
num3 = int(input("Ingresa el tercer número ganador: "))
num4 = int(input("Ingresa el cuarto número ganador: "))
num5 = int(input("Ingresa el quinto número ganador: "))

# Agregar los números a la lista
numerosg.extend([num1, num2, num3, num4, num5])

# Ordenar la lista de números ganadores
numerosg.sort()

# Mostrar los números ganadores ordenados
print("Números ganadores de la lotería (ordenados):", numerosg)