import sys, os, random, subprocess 


def getRutaArchivo():

    """
    Función que se encargará de retornar la ruta del archivo de texto.    
    """

    rutaArchivo = "./tickets.txt"
    
    return rutaArchivo
 

def limpiarPantalla():

    """
    Función encargada de limpiar la consola, eliminando los elementos visibles en pantalla antes de continuar con la ejecución del programa. El comando utilizado dependerá del sistema operativo en el que se ejecute.
    """
     
    comando = "cls" if os.name == "nt" else "clear"  

    subprocess.run([comando], shell=True)


def crearArchDatos():

    """
    Función encargada de crear un archivo de texto necesario para almacenar los datos ingresados por el usuario.  
    """

    rutaArchivo = getRutaArchivo()

    with open(rutaArchivo, "w", encoding="UTF-8") as f:

        pass


def actArchDatos(dictDatosNuevos):

    """
    Función encargada de actualizar el archivo de texto agregando nuevos registros al programa.
    """

    rutaArchivo = getRutaArchivo()

    with open(rutaArchivo, "a", encoding="UTF-8") as f:
        
        for clave, lista in dictDatosNuevos.items(): 

            f.write(f"{clave}: {', '.join(lista)}\n") 


def leerArchDatos(): 

    """  
    Función encargada de obtener los datos almacenados en el archivo de texto, los guarda en un diccionario y lo retorna.
    """

    rutaArchivo = getRutaArchivo()
    dictDatos = {}

    with open(rutaArchivo, "r", encoding="UTF-8") as f:

        for linea in f:

            clave, valores = linea.strip().split(": ", 1)

            dictDatos[clave] = valores.split(", ")

    return dictDatos


def pantallaMenu():

    """
    Función encargada de mostrar en pantalla el menú con las diferentes opciones disponibles, retorna la opción ingresada por el usuario.
    """
      
    print(f"\n\t{'=' * 70}")
    print("\t\t\t\tSISTEMA DE TICKETS")
    print(f"\t{'=' * 70}") 
    print("\n\t\t\tBienvenido/a, seleccione una opción: \n") 
    print("\t\t\t1. Generar ticket")
    print("\t\t\t2. Leer ticket")
    print("\t\t\t3. Salir\n") 
    
    return input("\n\t\t\tSeleccione: ")

 
def pantallaLecturaTicket(dictDatosTickets, idTicket, flag):

    """
    Función encargada de mostrar en pantalla los datos del ticket, ya sea cuando es generado o cuando se busca a partir de su número.
    """
      
    print(f"\n\t{'=' * 70}")
    print("\t\t\t\t  TICKET GENERADO") if flag == 1 else print("\t\t\t\t  DATOS DEL TICKET")
    print("\t" + "=" * 70)  
    print(f"\n\t\tNombre: {dictDatosTickets[idTicket][0]}", end=""),
    print(f"\t\t\tN° Ticket: {idTicket}"),
    print(f"\t\tSector: {dictDatosTickets[idTicket][1]}"),
    print(f"\t\tAsunto: {dictDatosTickets[idTicket][2]}"),
    print(f"\t\tProblema: {dictDatosTickets[idTicket][3]}")    
    print(f"\n\t{'=' * 70}")   

    if flag == 1:
        print("\n\t\t\tRecuerde guardar su número de ticket\n\t\t\t\tpara futuras consultas.")


def verificarDato(dato): 

    """
    Función encargada de verificar que el dato ingresado por el usuario contenga únicamente letras y espacios. Retorna un valor booleano indicando si la validación fue correcta.
    """

    return dato.replace(" ", "").isalpha()


def pantallaNuevoTicket():

    """
    Función encargada de solicitar al usuario los datos necesarios para generar un nuevo ticket. Valida que cada dato ingresado sea correcto antes de almacenarlo y retorna una lista con la información recopilada.
    """
  
    print(f"\n\t{'=' * 70}")
    print("\t\t\t\t  NUEVO TICKET")
    print(f"\t{'=' * 70}") 
    print("\n\t\t\tIngrese los siguientes datos: \n")  
    print("\t\t\t1°. Nombre de quien reporta")
    print("\t\t\t2°. Sector de trabajo")
    print("\t\t\t3°. Asunto") 
    print("\t\t\t4°. Problema encontrado\n")   
    print("\t\t\tSolo se permiten ingresar letras y espacios.")
    print("\t\t\t\tNo ingrese números ni símbolos.\n")

    cont = 0
    datosTicket = []

    while cont < 4:

        match cont:
            case 0:
                texto = "\n\t\t\t- Nombre: "
            case 1:
                texto = "\n\t\t\t- Sector: "
            case 2:
                texto = "\n\t\t\t- Asunto: "
            case 3:
                texto = "\n\t\t\t- Problema: "

        dato = input(texto)

        if verificarDato(dato):

            datosTicket.append(dato)
            cont += 1
        else:
            print("\n\t\t\tDato inválido, intente nuevamente.")

    return datosTicket


def opcionFinal(opBase):

    """    
    Función encargada de mostrar una opción de confirmación al usuario según la operación actual del programa. Recibe una opción base que determina el mensaje a mostrar, permitiendo reutilizar la función para confirmar acciones como generar un nuevo ticket, consultar otro ticket o cerrar el programa. Retorna una tupla compuesta por la operación seleccionada y el estado de la respuesta ingresada por el usuario:
    
        -  1: respuesta afirmativa ('s').
        - -1: respuesta negativa ('n').
        -  0: opción inválida.
    """

    respuesta = ()

    match opBase:

        case 1: 
            opcionIngresada = input("\n\t\t\t¿Desea generar un nuevo ticket? (s/n): ")

        case 2: 
            opcionIngresada = input("\n\t\t\t¿Desea consultar otro ticket? (s/n): ")

        case 3: 
            opcionIngresada = input("\n\t\t\t¿Está seguro que desea salir? (s/n): ")

    opcionIngresada = opcionIngresada.strip().lower()

    if len(opcionIngresada) == 1 and opcionIngresada in ('s','n'):

        if opcionIngresada == 'n':  
            respuesta = (opBase, -1)
        else:
            respuesta = (opBase, 1)  
    else: 
        respuesta = (opBase, 0)
    
    return respuesta


def nuevoTicket(dictDatosTickets):

    """
    Función encargada de capturar los datos ingresados por el usuario mediante la función 'pantallaNuevoTicket()'. Genera un número para el nuevo ticket y, tras comprobar su unicidad, almacena tanto el número generado como los datos ingresados por el usuario en un diccionario utilizado para la consulta de tickets durante el tiempo de ejecución. Asimismo, llama a la función 'actArchDatos()' para actualizar el archivo de texto del programa.
    Además, muestra en pantalla los datos del ticket generado mediante la función 'pantallaLecturaTicket()' y, por último, solicita al usuario que indique si desea generar un nuevo ticket o retornar al menú inicial.
    """

    listDatosTicket = () 
    respuesta = (1,1)
    flag = True
    
    while flag:
  
        if respuesta[1] == 0:
            respuesta = gestionarError("\n\t\t\t\tERROR. Opción inexistente.\n", 1) 

        elif respuesta[1] == -1:
            flag = False  

        else:
            limpiarPantalla() 
            listDatosTicket = pantallaNuevoTicket() 

            idTicket = random.randrange(1000, 9999)

            if idTicket not in dictDatosTickets: 

                dictDatosTickets[str(idTicket)] = listDatosTicket 
                actArchDatos({str(idTicket):listDatosTicket})
                limpiarPantalla()
                pantallaLecturaTicket(dictDatosTickets, str(idTicket), 1) 

                respuesta = opcionFinal(1) 

    return respuesta


def lecturaTicket(dictDatosTickets):

    """ 
    Función encargada de mostrar en pantalla los datos de un ticket a partir de su número.
    Si el ticket no existe, se informa al usuario mediante un mensaje. En caso contrario,
    se muestran sus datos llamando a la función 'pantallaLecturaTicket()'. También gestiona
    errores como el ingreso de opciones inválidas o números de ticket incorrectos.
    """
  
    flag = True
    respuesta = (2, 1)

    while flag: 
 
        if respuesta[0] == 2: 

            if respuesta[1] == 0:
               respuesta = gestionarError("\n\t\t\t\tERROR. Opción inexistente.\n", 2)

            elif respuesta[1] == -1:
                flag = False  

            else:
                limpiarPantalla() 
                print(f"\n\t{'=' * 70}")
                print("\t\t\t\t  LECTURA DE TICKET")
                print(f"\t{'=' * 70}") 

                idTicket = input("\n\t\t\t- Ingrese el número del ticket: ") 

                if not (idTicket.isnumeric() and len(idTicket) == 4): 
                    respuesta = gestionarError("\n\t\t\tERROR. Debe ingresar un número de cuatro dígitos.\n", 2)
    
                else:
                    if idTicket not in dictDatosTickets: 
                        respuesta = gestionarError("\n\t\t\tALERTA. No existe ticket asociado al número ingresado.\n", 2)
                    else: 
                        pantallaLecturaTicket(dictDatosTickets, idTicket, 0)
                        respuesta = opcionFinal(2) 

    return respuesta


def cerrarPrograma():
    
    """
    Función encargada de gestionar el cierre del programa. Solicita al usuario la confirmación para finalizar la ejecución. Si la opción ingresada es válida, retorna una tupla con la respuesta seleccionada. En caso de una opción inválida, muestra un mensaje de error y vuelve a solicitar la confirmación.
    """ 

    flag = True
    respuesta = (3, 2)

    while flag:

        if respuesta[0] == 3: 

            if respuesta[1] == 0: 
                respuesta = gestionarError("\n\t\t\t\tERROR. Opción inexistente.\n", 3)

            elif respuesta[1] in (1, -1):
                break
            else:
                respuesta = opcionFinal(3)
                
    return respuesta


def gestionarError(texto, opBase):

    """ 
    Función encargada de mostrar un mensaje de error en pantalla. Luego ejecuta la función 'opcionFinal()' y retorna el resultado obtenido según la opción seleccionada por el usuario.
    """

    print(texto)
    print(f"\t{'-' * 70}") 
    return opcionFinal(opBase)


def validarOpcion(datos=None):

    """ 
    Función encargada de capturar la opción ingresada por el usuario y validar que sea un valor numérico. Si la opción es válida, la envía a la función 'opciones()', encargada de gestionar las operaciones disponibles. Retorna el resultado de la acción seleccionada o una respuesta indicando una entrada inválida.
    """

    opcion = pantallaMenu()

    if opcion.isdigit():

        if int(opcion) in (1,2):

            return opciones(int(opcion), datos)

        else:
            return opciones(int(opcion))
    else:  
        return False, -1 
 

def opciones(opcion, datos=None):

    """
    Función encargada de gestionar la opción seleccionada por el usuario. Ejecuta la acción correspondiente según la opción ingresada, como crear un nuevo ticket, consultar uno existente o finalizar el programa. Retorna el resultado de la operación realizada.
    """

    respuesta = () 

    match opcion: 
        case 1: 
            respuesta = nuevoTicket(datos) 
        case 2: 
            respuesta = lecturaTicket(datos)
        case 3: 
            respuesta = cerrarPrograma()
        case _: 
            respuesta = False, -1
 
    return respuesta



def inicio(datos=None): 
    
    """
    Función encargada de administrar el flujo principal del programa. Controla las opciones seleccionadas por el usuario y mantiene la ejecución del sistema mediante un ciclo, permitiendo crear tickets, consultar información o volver al menú según la acción elegida. 
    """

    flag = True
    inicio = True 
    resultado = ()  
    
    while flag:      

        limpiarPantalla()  

        if inicio:
            resultado = validarOpcion(datos)  
            inicio = False  

        else:     
            if resultado[1] == -1: 
               resultado = validarOpcion(datos)  

            elif resultado[0] == 1: 
                resultado = opciones(1, datos) 

            elif resultado[0] == 2:  
                resultado = opciones(2, datos)  

            elif resultado[0] == 3 and resultado[1] == 1:
                sys.exit() 
  

#Comprueba si existe el archivo de almacenamiento. En caso contrario, crea uno nuevo.
if not os.path.isfile(getRutaArchivo()): 

    crearArchDatos()

#Carga en el diccionario los datos almacenados en el archivo de texto.
dictTickets = leerArchDatos() 

#Inicio del programa
inicio(dictTickets)