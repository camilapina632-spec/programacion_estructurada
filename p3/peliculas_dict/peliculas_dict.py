import funciones_dict

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR  CARACTERISTICAS DE UNA PELICULA :::... \n")
    caracteristica=input("Escribe el nombre de lacaracteristica: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones_dict.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR LA CARACTERISTICAS DE LA PELICULA :::... \n")
    if len(pelis)>0:
       for i in pelis:
        print(f"{i}={pelis[i]}")
    else:
        print("... ¡No hay caracteristicas de peliculas que Mostrar, verifique! ... ")
    funciones_dict.esperarTecla()
    
def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS CARACTERISTICAS  DE LA PELICULA :::... \n")
    opc=input("¿Estas seguro que deseas borrar TODAS las caracteristicas de la pelicula (Si/No)? ").lower().strip()
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las caracteristicas de la pelicula (Si/No)? ").lower().strip()
    if opc=="si":
        pelis=pelis.clear()
        funciones_dict.accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR UNA CARACTERISTICA DE LA PELICULA :::... \n")
    peli=input("Escribe la pelicula a buscar: ").lower().strip()
    noEncontre=True
    for i in pelis:
        if i == peli:
         print (f"La caracteristica es: {peli} y su valor es: {pelis[peli]}")
         funciones_dict.esperarTecla()
         noEncontre=False
    if noEncontre:
        input("\n\t... ¡No existe la caracteristica de la pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR CARACTERISTICA DE LA PELICULA :::... \n")
    peli=input("Escribe la caracteristica de la pelicula: ").lower().strip()
    noEncontre=True
    for i in pelis:
        if peli ==i:
         noEncontre=False
         opc=""
         while opc!="si" and opc!="no":
            opc=input("¡Estas seguro que deseas borrar esta caracteristicas de la pelicla (si/no)? ").lower().strip()
         if opc=="si":
            caracteristica=peli
    if noEncontre: 
       input("\n\t... !No existe la caracteristica de la pelicula a bscar, verifique! ...")
    else:
       pelis.pop(caracteristica)
       funciones_dict.accionExitosa()

        
def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR EL VALOR DE LA CARACTERISTICA DE LA PELICULA :::... \n")
    peli=input("Escribe el valor de la caracteristica a modificar: ").upper().strip()
    noEncontre=True
    for i in pelis:
        if peli ==i:
         noEncontre=False
         print(f"La caracteristica a buscar es: {pelis} y su valor es: {peli}")
         opc=""
         while opc!="si" and opc!="no":
            opc=input("¡Estas seguro que deseas modificar esta caracteristica de la pelicla (si/no)? ").lower().strip()
         if opc=="si":
           pelis[peli]=input("Escribe el nuevo valor de esta caracteristica: ").upper().strip()
           funciones_dict.accionExitosa()
    if noEncontre: 
       input("\n\t... !No existe la caracteristica de la pelicula a modificarr, verifique! ...")
