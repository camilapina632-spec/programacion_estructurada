
print ("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
varios=[1,2,33,65,23,23]
print(varios)


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["hola","NBA","ganador","perdedor"]
palabra=input("Dame la palabra a buscar: ")

encontre=False
for i in palabra:
    if i==palabra:
        encontre=True
        if encontre==True:
          print(f"La palabra: {palabra}, si esta en la lista.")
        else:
            print(f"La palabra {palabra}, no esta en la lista")

#2DA FORMA
 

#3er FORMA
palabras=["hola","NBA","ganador","perdedor"]
palabra=input("Dame la palabra a buscar: ")

encontre=False
while i < len(palabras):
     if palabras [i]==palabras:
         encontre=True
         i+=1

if encontre == True:
     print (f"La palabra: {palabra}, si se encuentra dentro de la lista.") 
else:   
     print (f"La palabra: {palabra}, no se encuentra dentro de la lista.")    

#Ejemplo 3 Añadir elementos a la lista
lista= []
true="s"
while true=="s":
     valor=input("Dame un valor de la lista").lower().strip()
     lista.append(valor)
     true=input("Desea añadir otro elemento a la lista (si/no)? ").lower().strip()

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ["Carlo", "6181234567"],
        ["Juan","6182334567"],
        ["Tony", "6182342323"]
]
print(agenda)

for i in agenda:
     print (i)

for r in range (0,3):
    for c in range (0,2):
     print(agenda[r][c])

lista=""
for r in range (0,3):
    for c in range (0,2):
      lista+=(f"{agenda[r][c]}, ")
    lista+="\n"
print (f"["+lista+"]")