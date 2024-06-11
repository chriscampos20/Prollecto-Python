package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func showMainMenu() {
	fmt.Println("-----Menu Principal-----")
	fmt.Println("1. Administrar alumnos\n2. Crear registro de asistencias")
	fmt.Println("3. Ver registro de asistencias\n4. Salir")
	fmt.Println("Selecciona una opción: ")
}

func administrarAlumnos() {
	for {
		// ...Imprimir el menú de administrar alumnos
		fmt.Println("---- Administrar alumnos ----")
		fmt.Println("1. Matricular alumnos\n2. Eliminar alumnos")
		fmt.Println("3. Volver al menu principal\n4. Salir")
		fmt.Println()

		// Leer la opción seleccionada por el usuario
		var opcion int
		fmt.Print("Selecciona una opción: ")
		fmt.Scanln(&opcion)

		// opciones del menu administrar alumnos
		if opcion == 1 {
			fmt.Println("-----Matricular alumnos-----")
			/////matricula() // Llamada a la función matricula() desde el archivo matricula.go
			matricula()
		} else if opcion == 2 {
			fmt.Println("-----Eliminar alumnos-----")
			/////eliminate() // Llamada a la función eliminate() desde el archivo eliminate.go
			eliminate()
		} else if opcion == 3 {
			fmt.Println("-----Volver al menu principal-----")
			// Salir del bucle y volver al menú principal
			break
		} else if opcion == 4 {
			fmt.Println("Saliendo del programa...")
			// Salir del bucle y del programa
			return
		} else {
			fmt.Println("Opción no válida. Por favor, selecciona una opción válida.")
		}
	}
}

func crearRegistroAsistencia() {
	// ...menu de crear registro de asistencia
	fmt.Println("---- Crear registro de asistencias ----")
	crearRegistros()
}

func verRegistroAsistencia() {
	fmt.Println("----Ver registros de asistencias----")
	verRegistros()

}
func asistencias() {
	// Crear un mapa para almacenar el registro de asistencia
	registro := make(map[string]*Alumno)

	// Solicitar el nombre para el registro
	fmt.Println("Ingrese el nombre del registro de asistencia:")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	nombreRegistro := scanner.Text()

	// Crear un bucle para que el usuario pueda agregar alumnos al registro
	fmt.Println("Ingrese el nombre de los alumnos a matricular (escriba 'salir' para terminar):")
	for scanner.Scan() {
		entrada := scanner.Text()

		// Si el usuario escribe "salir", termina el bucle
		if strings.ToLower(entrada) == "salir" {
			break
		}

		// Crear un nuevo alumno con nombre y asistencia inicial "No"
		alumno := &Alumno{
			Nombre:     entrada,
			Asistencia: "No",
		}

		// Agregar al alumno al registro
		registro[entrada] = alumno
	}

	// Verificar si hubo algún error al escanear la entrada del usuario
	if err := scanner.Err(); err != nil {
		fmt.Println("Error al leer la entrada:", err)
		return
	}

	// Imprimir el nombre del registro
	fmt.Println("Registro de asistencia:", nombreRegistro)

	// Solicitar la asistencia de cada alumno en el registro
	for _, alumno := range registro {
		fmt.Printf("¿Estuvo presente %s? (Ingrese 'Si' o 'No'):", alumno.Nombre)
		scanner.Scan()
		asistencia := scanner.Text()

		// Verificar si la respuesta es válida (Sí o No)
		if strings.EqualFold(asistencia, "Si") || strings.EqualFold(asistencia, "No") {
			alumno.Asistencia = asistencia
		} else {
			fmt.Println("Respuesta inválida. Ingrese 'Si' o 'No'.")
		}
	}

	// Verificar si hubo algún error al escanear la entrada del usuario
	if err := scanner.Err(); err != nil {
		fmt.Println("Error al leer la entrada:", err)
		return
	}

	// Imprimir el registro de asistencia
	fmt.Println("Registro de asistencia:")
	for _, alumno := range registro {
		fmt.Printf("%s: %s\n", alumno.Nombre, alumno.Asistencia)
	}
}

func eliminate() {
	// Crear una lista vacía para almacenar los nombres
	var lista []string

	// Crear un bucle para que el usuario pueda agregar nombres a la lista
	fmt.Println("Ingrese nombres para agregar a la lista (escriba 'salir' para terminar):")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		entrada := scanner.Text()

		// Si el usuario escribe "salir", termina el bucle
		if strings.ToLower(entrada) == "salir" {
			break
		}

		// Agregar el nombre ingresado a la lista
		lista = append(lista, entrada)
	}

	// Verificar si hubo algún error al escanear la entrada del usuario
	if err := scanner.Err(); err != nil {
		fmt.Println("Error al leer la entrada:", err)
		return
	}

	// Imprimir la lista de nombres ingresados por el usuario con su número de índice
	fmt.Println("Nombres en la lista:")
	for i, nombre := range lista {
		fmt.Printf("%d: %s\n", i+1, nombre)
	}

	// Solicitar al usuario el número de lista del nombre que desea eliminar
	fmt.Println("Ingrese el número de lista del nombre que desea eliminar:")
	scanner = bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		numeroListaStr := scanner.Text()
		numeroLista, err := strconv.Atoi(numeroListaStr)
		if err != nil {
			fmt.Println("Error al convertir el número de lista:", err)
			return
		}

		// Verificar si el número de lista es válido
		if numeroLista < 1 || numeroLista > len(lista) {
			fmt.Println("Número de lista inválido.")
			return
		}

		// Eliminar el nombre correspondiente al número de lista ingresado
		lista = append(lista[:numeroLista-1], lista[numeroLista:]...)

		// Imprimir la lista actualizada
		fmt.Println("Nombres en la lista después de eliminar:")
		for i, nombre := range lista {
			fmt.Printf("%d: %s\n", i+1, nombre)
		}
	}
}

func matricula() {
	// Crear una lista vacía para almacenar los nombres
	var lista []string

	// Crear un bucle para que el usuario pueda agregar nombres a la lista
	fmt.Println("Ingrese los nombres de los alumnos a matricular (escriba 'salir' para terminar):")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		entrada := scanner.Text()

		// Si el usuario escribe "salir", termina el bucle
		if strings.ToLower(entrada) == "salir" {
			break
		}

		// Agregar el nombre ingresado a la lista
		lista = append(lista, entrada)
	}

	// Verificar si hubo algún error al escanear la entrada del usuario
	if err := scanner.Err(); err != nil {
		fmt.Println("Error al leer la entrada:", err)
		return
	}

	// Imprimir la lista de nombres ingresados por el usuario con su número de índice
	fmt.Println("Alumnos matriculados:")
	for i, nombre := range lista {
		numero := i + 1
		fmt.Printf("%d: %s\n", numero, nombre)
	}
}

// Estructura para representar a un alumno
type Alumno struct {
	Nombre     string
	Asistencia string // Puede ser "Sí" o "No"
}

func crearRegistros() {
	// Crear un mapa para almacenar el registro de asistencia
	registro := make(map[string]*Alumno)

	// Solicitar el nombre para el registro
	fmt.Println("Ingrese el nombre del registro de asistencia:")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	nombreRegistro := scanner.Text()

	// Crear un bucle para que el usuario pueda agregar alumnos al registro
	fmt.Println("Ingrese el nombre de los alumnos a matricular (escriba 'salir' para terminar):")
	for scanner.Scan() {
		entrada := scanner.Text()

		// Si el usuario escribe "salir", termina el bucle
		if strings.ToLower(entrada) == "salir" {
			break
		}

		// Crear un nuevo alumno con nombre y asistencia inicial "No"
		alumno := &Alumno{
			Nombre:     entrada,
			Asistencia: "No",
		}

		// Agregar al alumno al registro
		registro[entrada] = alumno
	}

	// Verificar si hubo algún error al escanear la entrada del usuario
	if err := scanner.Err(); err != nil {
		fmt.Println("Error al leer la entrada:", err)
		return
	}

	// Imprimir el nombre del registro
	fmt.Println("Registro de asistencia:", nombreRegistro)

	// Solicitar la asistencia de cada alumno en el registro
	for _, alumno := range registro {
		fmt.Printf("¿Estuvo presente %s? (Ingrese 'Si' o 'No'):", alumno.Nombre)
		scanner.Scan()
		asistencia := scanner.Text()

		// Verificar si la respuesta es válida (Sí o No)
		if strings.EqualFold(asistencia, "Si") || strings.EqualFold(asistencia, "No") {
			alumno.Asistencia = asistencia
		} else {
			fmt.Println("Respuesta inválida. Ingrese 'Si' o 'No'.")
		}
	}

	// Verificar si hubo algún error al escanear la entrada del usuario
	if err := scanner.Err(); err != nil {
		fmt.Println("Error al leer la entrada:", err)
		return
	}

	// Imprimir el registro de asistencia
	fmt.Println("Registro de asistencia:")
	for _, alumno := range registro {
		fmt.Printf("%s: %s\n", alumno.Nombre, alumno.Asistencia)
	}
}

type student struct {
	Nombre     string
	Asistencia string // Puede ser "Sí" o "No"
}

func verRegistros() {
	// Crear un slice para almacenar los registros de asistencia
	var registros []map[string]*Alumno

	// Solicitar el nombre para el registro
	fmt.Println("Ingrese el nombre del registro de asistencia:")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	nombreRegistro := scanner.Text()

	// Bucle para crear múltiples registros de asistencia
	for {
		// Crear un nuevo mapa para el registro de asistencia actual
		registro := make(map[string]*Alumno)

		// Solicitar el nombre de los alumnos a matricular
		fmt.Println("Ingrese el nombre de los alumnos a matricular (escriba 'salir' para terminar):")
		for scanner.Scan() {
			entrada := scanner.Text()

			// Si el usuario escribe "salir", termina el bucle de matriculación
			if strings.ToLower(entrada) == "salir" {
				break
			}

			// Crear un nuevo alumno con nombre y asistencia inicial "No"
			alumno := &Alumno{
				Nombre:     entrada,
				Asistencia: "no",
			}

			// Agregar al alumno al registro
			registro[entrada] = alumno
		}

		// Agregar el registro al slice de registros
		registros = append(registros, registro)

		// Verificar si hubo algún error al escanear la entrada del usuario
		if err := scanner.Err(); err != nil {
			fmt.Println("Error al leer la entrada:", err)
			return
		}

		// Preguntar si se desea crear otro registro
		fmt.Println("¿Desea crear otro registro de asistencia? (Ingrese 'si' o 'no'):")
		scanner.Scan()
		respuesta := scanner.Text()

		// Si la respuesta es diferente de "Si", terminar el bucle de creación de registros
		if !strings.EqualFold(respuesta, "si") {
			break
		}
	}

	// Imprimir el nombre del registro
	fmt.Printf("Registro de asistencia: %s\n", nombreRegistro)

	// Mostrar la lista numerada de los registros de asistencia existentes
	fmt.Println("Registros de asistencia realizados:")
	for i := range registros {
		fmt.Printf("%d: Registro %d\n", i+1, i+1)
	}

	// Solicitar al usuario el número del registro deseado
	fmt.Println("Ingrese el número del registro deseado:")
	scanner.Scan()
	numeroRegistroStr := scanner.Text()
	numeroRegistro, err := strconv.Atoi(numeroRegistroStr)
	if err != nil || numeroRegistro < 1 || numeroRegistro > len(registros) {
		fmt.Println("Número de registro inválido.")
		return
	}
	registroSeleccionado := registros[numeroRegistro-1]

	// Imprimir el informe del registro seleccionado
	fmt.Printf("Informe de asistencia para Registro %d:\n", numeroRegistro)
	for _, alumno := range registroSeleccionado {
		fmt.Printf("Nombre: %s\n", alumno.Nombre)
		fmt.Printf("Asistencia: %s\n", alumno.Asistencia)
	}
}

func password() {
	// Get the username from the user.
	fmt.Println("Ingrese su usuario de acceso: ")
	reader := bufio.NewReader(os.Stdin)
	Chris, _, err := reader.ReadLine()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// Get the password from the user.
	fmt.Println("Enter your password: ")
	edwin007, _, err := reader.ReadLine()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// Store the username and password in a file.
	file, err := os.OpenFile("./users.txt", os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer file.Close()

	fmt.Fprintf(file, "%s %s\n", Chris, edwin007)

	fmt.Println("User and password created successfully.")
}

func main() {
	for {
		password()

		for {
			showMainMenu()

			var mainOption int
			fmt.Scanln(&mainOption)

			switch mainOption {
			case 1:
				administrarAlumnos()
			case 2:
				crearRegistroAsistencia()
			case 3:
				verRegistroAsistencia()
			case 4:
				fmt.Println("Saliendo del programa...")
				return // Salir del programa
			default:
				fmt.Println("Opción inválida. Inténtalo de nuevo.")
			}
		}
	}
}
