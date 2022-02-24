# Sistema Operativo Bash de Primera Generación
# Presentado por: Alejandro Bermudez y Miguel Salazar

# imports

import time

def procesamiento(instruccion):
    for i in linea:
        time.sleep(0.3)
        if i=='#':   ###@
            time.sleep(10)
        print(i)
    print(linea)
    return 0

instrucciones = open("instrucciones.txt")

linea = instrucciones.readline()
print("Primer set de instrucciones (disquete)")
while linea !='':
  linea=instrucciones.readline()
  procesamiento(linea)

print("Segundo set de instrucciones (disquete)")
instrucciones2 = open("instrucciones2.txt")

linea = instrucciones2.readline()

while linea !='':
  linea=instrucciones2.readline()
  procesamiento(linea)

print("Tercer set de instrucciones (disquete)")
instrucciones3 = open("instrucciones3.txt")

linea = instrucciones3.readline()

while linea !='':
  linea=instrucciones3.readline()
  procesamiento(linea)
  

