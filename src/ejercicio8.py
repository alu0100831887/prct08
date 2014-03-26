#!/usr/bin/python
import modulo
def error(numero_intervalo, numero_test, umbral):
  errores=0.0
  for i in range (numero_test):
    
    aprox1= modulo.aproximacion(numero_intervalo)
    aprox2= modulo.aproximacion(numero_test)
    resultado= aprox1 - aprox2
    if abs(resultado)>= umbral:
       errores+=1
  return (errores/numero_test)*100
  
  
if (__name__=="__main__"):
  import sys
  if((len(sys.argv) ==1) or (len(sys.argv) == 2) or (len(sys.argv) ==3)):
    print("No se han introducido todos los argumentos")
    numero_intervalo = 10
    numero_test = 10
    umbral=0.000000001
  else:
    numero_intervalo= int(sys.argv[1])
    numero_test= int(sys.argv[2])
    umbral=float(sys.argv[3])
  
  print error(numero_intervalo,numero_test,umbral)
  
  
  
  
  
  
  

