import secrets, string, sys, os, subprocess, msvcrt


def dicDatosIniciales():

    """
    Función encargada de devolver un diccionario con los elementos necesarios para la creación de una contraseña.
    """

    diccionario = {
        'letras': string.ascii_letters,
        'numeros': string.digits,
        'caracteres': string.punctuation
        }
    
    return diccionario


def limpiarPantalla():
    
    """
    Función utilizada para limpiar la consola, eliminando los elementos visibles en pantalla antes de continuar con la ejecución del programa. El comando utilizado dependerá del sistema operativo en el que se ejecute.
    """ 

    comando = "cls" if os.name == "nt" else "clear"

    subprocess.run([comando], shell=True) 


def pantallaMenu():

    """
    Función utilizada para mostrar el menú con las diferentes opciones disponibles para crear una contraseña y retorna la opción ingresada por el usuario.
    """

    print(f"\n\t\t{'=' * 70}")
    print("\t\t\t\t\tGENERADOR DE CONTRASEÑAS")
    print(f"\t\t{'=' * 70}")
    print("\n\t\t\tElija el tipo de contraseña que desea generar:\n")  
    print("\t\t\t1. Solo letras")
    print("\t\t\t2. Solo números")
    print("\t\t\t3. Letras y números")
    print("\t\t\t4. Letras, números y caracteres especiales")
    print("\t\t\t0. Salir") 

    return input("\n\t\t\tSeleccione una opción: ")


def generarPassword(opcion):

    """ 
    Función encargada de generar una contraseña en base a la opción ingresada por el usuario, utilizando los elementos contenidos en el diccionario retornado por la función 'dicDatosIniciales()'. La función devolverá la contraseña resultante, la cual tendrá una longitud de 12 caracteres.
    """ 

    largoPassword = 12
    password = ""
    charsPermitidos = ""
    diccionario = dicDatosIniciales()

    match opcion:
        case 1:
            charsPermitidos = diccionario['letras']
        case 2:
            charsPermitidos = diccionario['numeros']
        case 3:
            charsPermitidos = diccionario['letras'] + diccionario['numeros']
        case 4:
            charsPermitidos = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']

    for _ in range(largoPassword):
        password += secrets.choice(charsPermitidos)

    return password


def imprimirDatos(opcion, texto):

    """
    Función encargada de mostrar información sobre la contraseña generada, como su longitud, composición y valor final. Además, invoca a la función 'generarPassword()' para llevar a cabo su creación.
    """
 
    print(texto)
    print(f"\t\t{'=' * 70}") 
    print(f"\n\t\t\t- Se ha generado una contraseña con una longitud de \n\t\t\t  12 caracteres compuesta ", end="")

    match opcion:
        case 1: 
            print("solo por letras.") 
        case 2: 
            print("solo por números.") 
        case 3: 
            print("por una combinación de letras \n\t\t\t  y números.") 
        case 4:   
            print("por una combinación de letras, \n\t\t\t  números y caracteres especiales.") 

    print(f"\n\t\t\t- Contraseña generada: {generarPassword(opcion)}") 


def inicio():

    """
    Función encargada de administrar el flujo principal del programa. En primer lugar, llamará a la función 'pantallaPrincipal()' para capturar la opción elegida por el usuario. En caso de un ingreso incorrecto, mostrará una advertencia; caso contrario, enviará dicha opción como parámetro a la función 'imprimirDatos()', que a su vez se encargará de reenviarla a 'generarPassword()' para la creación de la contraseña.
    Por último, aparecerá una leyenda indicándole al usuario que debe presionar una tecla para volver a comenzar el proceso de creación de una contraseña. Esto sucederá tanto luego de mostrar la información generada como cuando se ingrese una opción incorrecta.
    """
    
    flag = True 

    while flag:
        
        opcion = pantallaMenu()

        print("\n\n\t\t" + "=" * 70)
        
        if opcion.isdigit():

            opcion = int(opcion)

            match opcion:
                case 0:    
                    limpiarPantalla()
                    sys.exit()
                case 1: 
                    imprimirDatos(opcion, "\t\t\t\t\t   SOLO LETRAS") 
                case 2: 
                    imprimirDatos(opcion, "\t\t\t\t\t   SOLO NÚMEROS")  
                case 3: 
                    imprimirDatos(opcion, "\t\t\t\t\t   LETRAS Y NÚMEROS") 
                case 4:  
                    imprimirDatos(opcion, "\t\t\t\t    LETRAS, NÚMEROS Y CARACTERES ESP.") 
                case _:  
                    print("\n\t\t\t\t\tERROR. Opción no válida.") 
        else:  
            print("\n\t\t\t\tERROR. Debe ingresar un número.")
 
        
        print(f"\n\t\t{'=' * 70}") 
        print("\n\t\t\tPresione cualquier tecla para volver al inicio...")
        msvcrt.getch()
        limpiarPantalla()

#Inicio del programa
limpiarPantalla()
inicio()

 