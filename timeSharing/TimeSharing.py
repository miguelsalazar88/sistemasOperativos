# Sistema Operativo de Tiempo Compartido
# Presentado por: Alejandro Bermudez y Miguel Salazar

# imports

from itertools import cycle


# La clase usuario le permite al sistema operativo saber cuantos usuarios van a compartir los
# recursos
class Usuario:
    def __init__(self, nombre, porcentaje):
        self.nombre = nombre
        self.porcentaje = porcentaje


# Ejecucion en consola
print("**** Bienvenido al Sistema Operativo de Tiempo Compartido ****\n")

# Se le pide al primer usuario indicar la cantidad de personas que utilizaran el sistema en la sesion
numUsuarios = int(input("Digite el numero de usuarios para esta sesion: "))

# Se crea una lista de usuarios que iterara ciclicamente durante el transcurso del programa
listaUsuarios = []
porcentajeTotal = 100

# Se le pide a los usuarios ingresar el mombre y el porcentaje de recursos a usar
for i in range(numUsuarios):
    nombre = str(input("Digite el nombre del usuario " + str(i + 1) + ": "))
    porcentajeUsuario = int(input("Ingrese el porcentaje de los recursos a usar ("
                                  + str(porcentajeTotal) + "% disponible): "))
    listaUsuarios.append(Usuario(nombre, porcentajeUsuario))
    porcentajeTotal = porcentajeTotal - porcentajeUsuario

# Se itera ciclicamente en la lista de usuarios para que cada uno ejecute las operaciones que desee
for usuario in cycle(listaUsuarios):
    termino = False;
    print("*********************************************************\n")
    while not termino:
        print("Turno del usuario " + usuario.nombre + "(" + str(usuario.porcentaje) + "% de los recursos)")
        print("********************************")
        opcion = int(input("Digite que tipo de operacion desea hacer:\n"
                           "1. Suma\n"
                           "2. Resta\n"
                           "3. Multiplicacion\n"
                           "4. Division\n"
                           "********************************\n"))
        num1 = float(input("Digite el primer numero:"))
        num2 = float(input("Digite el segundo numero:"))

        if opcion == 1:
            resultado = num1 + num2;
            op = "+"

        if opcion == 2:
            resultado = num1 - num2
            op = "-"

        if opcion == 3:
            resultado = num1 * num2
            op = "*"

        if opcion == 4:
            resultado = resultado = num1/num2
            op = "/"

        print("El resultado de " + str(num1) + " " + op + " " + str(num2) + " es: " + str(resultado))
        desea = str(input("Desea realizar otra operacion? (S/N)"))

        if desea == "N" or desea == "n":
            termino = True
        else:
            termino = False
