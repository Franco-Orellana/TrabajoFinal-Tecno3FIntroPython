
# Proyecto: Aplicaciones de Consola

## Descripción

Este proyecto contiene dos aplicaciones desarrolladas para ejecutarse desde consola:

1.  **Sistema de Gestión de Tickets**
    
2.  **Generador de Contraseñas**
     

----------

# Aplicación 1: Sistema de Gestión de Tickets

## Objetivo

Permitir a los usuarios crear y consultar tickets de soporte mediante una interfaz de consola simple e intuitiva.

## Menú Principal

Al iniciar la aplicación se mostrará el siguiente menú:

```text
			=========================================
						SISTEMA DE TICKETS
			=========================================

				Bienvenido/a, seleccione una opción:

				1. Generar ticket
				2. Leer ticket
				3. Salir

				Seleccione una opción:

```

----------

## Funcionalidades

### 1. Generar ticket

Permite registrar un nuevo ticket solicitando la siguiente información:

-   Nombre de quien reporta
    
-   Sector de trabajo
    
-   Asunto
    
-   Problema encontrado
    

#### Flujo

1.  El usuario ingresa los datos solicitados.
    
2.  Se genera automáticamente un número de ticket aleatorio entre **1000 y 9999**.
    
3.  Se muestra por pantalla toda la información registrada.
    

#### Ejemplo de ingreso de datos

```text
		===================================================
							NUEVO TICKET
		===================================================

				Ingrese los siguientes datos:

				1°. Nombre de quien reporta
				2°. Sector de trabajo
				3°. Asunto
				4°. Problema encontrado
				
				Solo se permiten ingresar letras y espacios.
						No ingrese números ni símbolos.

				- Nombre: Juan Pérez
				- Sector: Sistemas
				- Asunto: Impresora
				- Problema: No imprime documentos

```

#### Ejemplo de información registrada

```text
	================================================================
							TICKET GENERADO
	================================================================

		Nombre: Juan Pérez						N° Ticket: 5487
		Sector: Sistemas
		Asunto: Impresora
		Problema: No imprime documentos
		
	================================================================
					Recuerde guardar su número de ticket 
							para futuras consultas.
							
```


#### Crear otro ticket

Luego de mostrar el ticket se preguntará:

```text
¿Desea crear otro ticket? (s/n)
```

-   **S**: Regresa a la pantalla de "Nuevo ticket".
    
-   **N**: Regresa al menú principal.
    

----------

### 2. Leer ticket

Permite consultar un ticket previamente almacenado.

#### Flujo

1.  Se solicita el número de ticket.
    
2.  El sistema busca la información asociada.
    
3.  Si existe, se muestra por pantalla.
    

#### Ejemplo

```text
	================================================================
							LECTURA DE TICKET
	================================================================
			
				- Ingrese el número del ticket: 5487

	================================================================
							DATOS DE TICKET
	================================================================

		Nombre: Juan Pérez						N° Ticket: 5487
		Sector: Sistemas
		Asunto: Impresora
		Problema: No imprime documentos
	================================================================
	
```

#### Leer otro ticket

Al finalizar la consulta se preguntará:

```text
¿Desea consultar otro ticket? (s/n)
```

-   **S**: Regresa a la pantalla de "Leer ticket".
    
-   **N**: Regresa al menú principal.
    

----------

### 3. Salir

Permite finalizar la ejecución de la aplicación.

#### Confirmación

Antes de cerrar el programa se solicitará confirmación:

```text
¿Está seguro que desea salir? (s/n)
```

-   **S**: Finaliza la aplicación.
    
-   **N**: Regresa al menú principal.
    

----------

## Requisitos Funcionales

-   Generar números de ticket aleatorios entre 1000 y 9999.
    
-   Almacenar tickets durante la ejecución del programa.
    
-   Permitir la consulta mediante número de ticket.
    
-   Validar las opciones ingresadas por el usuario.
    
-   Solicitar confirmación antes de salir.
    

----------

# Aplicación 2: Generador de Contraseñas

## Objetivo

Permitir generar contraseñas seguras según diferentes criterios seleccionados por el usuario.

## Menú Principal

```text
	================================================================
						GENERADOR DE CONTRASEÑAS
	================================================================
			
			Elija el tipo de contraseña que desea generar:
			
			1. Solo letras
			2. Solo números
			3. Letras y números
			4. Letras, números y caracteres especiales
			0. Salir
			
			Seleccione una opción:

```

----------

## Funcionalidades

### 1. Contraseña "solo letras"

Genera una contraseña utilizando únicamente caracteres alfabéticos.

#### Ejemplo

```text
QwErTyUiOp
```

----------

### 2. Contraseña "solo números"

Genera una contraseña utilizando únicamente números.

#### Ejemplo

```text
8473629185
```

----------

### 3. Contraseña "letras y números"

Genera una contraseña combinando letras y números.

#### Ejemplo

```text
A7k9P2mQ4x
```

----------

### 4. Contraseña "letras, números y caracteres especiales"

Genera una contraseña incluyendo:

-   Letras mayúsculas
    
-   Letras minúsculas
    
-   Números
    
-   Caracteres especiales
    

#### Caracteres especiales empleados

```text
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

#### Ejemplo

```text
P@9k#T2!mQ
```

----------

### Longitud de la contraseña

La contraseña tendrá una longitud preestablecida de 12 caracteres. 

----------

### Generar otra contraseña

Después de mostrar la contraseña generada:

```text
 Presione cualquier tecla para volver al inicio...
```
    
----------

## Requisitos Funcionales

-   Generar contraseñas aleatorias.
    
-   Permitir seleccionar el tipo de contraseña.
    
-   Validar opciones ingresadas por el usuario.
    
-   Garantizar que la contraseña se genere según el criterio seleccionado.
    

----------

# Tecnología utilizada

-   Python 