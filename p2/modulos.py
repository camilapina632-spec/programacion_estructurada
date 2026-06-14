# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
def borrarPantalla():
    print ("\033c")

def funcion1():
    
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("Apellido: ").strip().upper()
    print(f"El nombre de el alumno es: {nombre} {apellidos}")

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
    
    nombre=nom
    apellidos=ape
    print(f"El nombre de el alumno es: {nombre} {apellidos}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   numero=int(8+5)
   return numero

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom, ape):
    
    nombre=nom
    apellidos=ape
   
    return nombre, apellidos

#Invocar las funciones
funcion1()

funcion3("Michael", "Jackson")

resultado=funcion2()
print(f"El resultado es: {resultado}")

nom,ape=funcion4("Juan", "Lopez")
print(f"El nombre del alumno es: {nom} {ape}")
