# Sistema Operativo Bash de Primera GeneraciÃ³n
# Presentado por: Alejandro Bermudez y Miguel Salazar

# imports

import time
import numpy as np

#Archivos (disquetes) de instrucciones
instrucciones1 = open("instrucciones1.txt")
instrucciones2 = open("instrucciones2.txt")
instrucciones3 = open("instrucciones3.txt")

#Archivos para el manejo de las instrucciones
memoriaSecundaria = open("memoriaSecundaria.txt","r+") #Memoria no volatil

#Memoria volatil y quien se entiende con el procesado
memoriaPrimaria = open("memoriaPrimaria.txt","r+") 

#Se recibe y procesa el lote correspondiente segun la prioridad del Sheduling
def procesamiento(lote):
    bandera="Instruccion ejecutada: "
    for instruccion in lote:
        for i in instruccion:
            time.sleep(0)
            if i=='#':   ###@
                time.sleep(0)
                memoriaSecundaria.write(instruccion)
                bandera="Instruccion perdida (cuelgo)"
                break
            #print(i)
            else:
                bandera="Instruccion ejecutada: "
        print(bandera,instruccion)
    return 0

#Se almacenan todas las instrucciones y luego se ordenan
def memoriaSecundariaF(instr):
    #Los bloques de instrucciones quedan de manera permanete en la memoria Secundaria
    #memoriaSecundaria.writelines(instr)
    print(len(memoriaSecundaria.readlines()))
    ingreso=memoriaSecundaria.readlines()
    #print("\n Carga de instrucciones de la memoria secundaria \n")
    print(ingreso)
   
    #print("\n Ordenamiento de las instrucciones en la memoria secundaria \n")#Abecedario
    pp=sorted(instr,key=len)
    insOrdenadas=sorted(pp)
    memoriaSecundaria.truncate(0)
    memoriaSecundaria.writelines(insOrdenadas)
    memoriaPrimaria.writelines(insOrdenadas)#ingreso)
    memoriaPrimariaF()
    
    return 0

#Recibe las instrucciones segun su prioridad y hace el envio al procesamiento por lotes
def memoriaPrimariaF():
    cargaP=memoriaPrimaria.readlines()
    lote=[]
    ins= np.array(cargaP)
    for i in range(0,int(len(ins)/10)):
        lote=ins[i*10:(i+1)*10]
        print("Lote del Sheduling numero:",i," cantidad de instrucciones: ",len(lote))
        print("Instrucciones procesadas")
        print(lote)
        procesamiento(lote)
    return 0
        

instr=instrucciones2.readlines()+instrucciones3.readlines()+instrucciones1.readlines()
print("Cantidad de instrucciones insertadas",len(instr))
print(instr)
i=1
if i==0:
    memoriaPrimaria.truncate(0)
    memoriaSecundaria.truncate(0)
else:
    memoriaSecundariaF(instr)




    

