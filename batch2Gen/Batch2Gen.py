# Sistema Operativo Batch Segunda Generacion
# Presentado por: Diago Bermudez y Miguel Salazar

# imports
from _csv import reader
from abc import ABC, abstractmethod


# Esta clase emula el buffer de un sistema operativo Batch de segunda generacion.
# Se cargan los jobs al buffer, se priorizan, y se ejecutan segun su priorizacion.
class Buffer:
    def __init__(self):
        self.sumas = []
        self.restas = []
        self.multiplicaciones = []
        self.divisiones = []


class Job(ABC):
    def __init__(self, jobno, num1, num2):
        self.jobno = int(jobno)
        self.num1 = float(num1)
        self.num2 = float(num2)

    @abstractmethod
    def resultado(self):
        pass


class Suma(Job):

    def __init__(self, jobno, num1, num2):
        super().__init__(jobno, num1, num2)

    def resultado(self):
        resultado = self.num1 + self.num2
        print("Job No. " + str(self.jobno) + ": " + str(self.num1) + " + " + str(self.num2) + "= " + str(resultado))


class Resta(Job):
    def __init__(self, jobno, num1, num2):
        super().__init__(jobno, num1, num2)

    def resultado(self):
        resultado = self.num1 - self.num2
        print("Job No. " + str(self.jobno) + ": " + str(self.num1) + " - " + str(self.num2) + "= " + str(resultado))


class Multiplicacion(Job):
    def __init__(self, jobno, num1, num2):
        super().__init__(jobno, num1, num2)

    def resultado(self):
        resultado = self.num1 * self.num2
        print("Job No. " + str(self.jobno) + ": " + str(self.num1) + " * " + str(self.num2) + "= " + str(resultado))


class Division(Job):
    def __init__(self, jobno, num1, num2):
        super().__init__(jobno, num1, num2)

    def resultado(self):
        resultado = self.num1 / self.num2
        print("Job No. " + str(self.jobno) + ": " + str(self.num1) + " / " + str(self.num2) + "= " + str(resultado))


# Se crea una instancia de Buffer en la que se almacenaran los jobs y
buffer = Buffer()


# Metodo leerTarjeta toma un archivo de texto csv y lo inserta en el Buffer
def leerTarjeta(path):
    with open(path, "r") as file:
        csv_reader = reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            if row[1] == 'suma':
                buffer.sumas.append(Suma(row[0], row[2], row[3]))

            elif row[1] == 'rest':
                buffer.restas.append(Resta(row[0], row[2], row[3]))

            elif row[1] == 'mult':
                buffer.multiplicaciones.append(Multiplicacion(row[0], row[2], row[3]))

            elif row[1] == 'divi':
                buffer.divisiones.append(Division(row[0], row[2], row[3]))


# En este metodo se procesan los jobs por prioridad y se imprimen en consola los resultados
def procesarDatos():
    for suma in buffer.sumas:
        suma.resultado()
    for resta in buffer.restas:
        resta.resultado()
    for multiplicacion in buffer.multiplicaciones:
        multiplicacion.resultado()
    for division in buffer.divisiones:
        division.resultado()

# Se efectuan los procesos y se imprime el resultado
print("**** Resultado de los Trabajos ****\n")
leerTarjeta("batch2Gen/batch2Gen.csv") # Revisar el Path del archivo. En algunos equipos cambia.
procesarDatos()

