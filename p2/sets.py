"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print ("\033c")
set1={"python", "SQL", "Estructurado", "SQL"}

for i in set1:
  print (i)

set2={"Hola", True, 33, 3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={""}
print(set3)

set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add("33")
print(set3)

lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=list(conjunto)
print (lista)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
lista_alum= []
set_alum={""}
set_alum.clear()
resp="si"
while resp == "si":
  lista_alum.append (input("Ingrese los correos de los alumnos: "))
  set_alum.add (input("Ingrese los correos de los alumnos: "))
  resp=input ("Desea ingresar otro: (si/no)").lower().strip()
print (lista_alum)
print(set_alum)

list_emails=[]
opc="s"
while opc=="s":
  list_emails.append(input("Ingresa el email: ")).lower().strip()
  opc=input("Desea repetir el ciclo (si/no)").lower().strip()
    
set_emails=set(list_emails)

#Solucion 2
list_emails=[]
set_alumn={}
opc=True
while opc==True:
  list_emails.insert(0,input("ingrese los emails de los estudiantes"))
  opc=input("Desea volver a intentarlo? (si/no)").lower().strip()
  if opc == "no":
    opc= False
  else:
    opc=True

list_emails.set(set_alumn) 
set_alumn.list(list_emails)
print (list_emails)



  



