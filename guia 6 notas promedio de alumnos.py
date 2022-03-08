# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:38:04 2020
 print(nombres)
    print(apellidos)
    print(notas)
    print(suma)
    print(mayor)
    print(menor)
    print(prom)
@author: Rmiglio
"""


def main():
    archivo=open("C:\\Users\\Rmiglio\Downloads\\Python\\Archivos\\lista.csv","r")
    archivo2=open("C:\\Users\\Rmiglio\Downloads\\Python\\Archivos\\resumen.txt","w")
    nombres=[]
    apellidos=[]
    notas=[]
    for linea in archivo:
      valores=linea.split(",")
      nombres.append(valores[0])
      apellidos.append(valores[1])
      corregido=int(valores[2].strip("\n"))
      if corregido<0 or corregido>20:             
              notas.append(0)
      else:
              notas.append(corregido)
     
    suma=0
    aprobados=0
    mayor=notas[0]
    menor=notas[0]
    for i in notas:
        suma=suma+i
        if i>mayor:
            mayor=i
        if i<menor:
            menor=i
        if i>10:
            aprobados=aprobados+1
    
    
    prom=suma/len(notas)
    promaprobados=aprobados/len(notas)
    cad="promedio: "+str(prom)+"\n"
    archivo2.write(cad)
    cad="promedio de aprobados: " + str(promaprobados)+"\n"
    archivo2.write(cad)
   
    indicemayor=0
    indicemenor=0
    for i in range(0,len(notas)):
        if notas[i]==mayor:
            indicemayor=i
        if notas[i]==menor:
            indicemenor=i
    cad="Alumno con Mayor nota: "+ apellidos[indicemayor]+"\n"
    archivo2.write(cad)
    cad="Alumno con Menor nota: "+ apellidos[indicemenor]+"\n"
    archivo2.write(cad) 
    archivo.close()
    archivo2.close()
    
main()