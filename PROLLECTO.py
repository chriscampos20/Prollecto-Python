import sys

def show_main_menu():
    print("\n-----Menu Principal-----")
    print("1. Agregar articulos a la venta\n2. Agregar articulos al iventario","\n3. Eliminar Articulos del inventario\n4. Salir")
    print("3. Eliminar Articulos del inventario\n4. Salir")
    print("Selecciona una opción: ")

def Agregar_articulos_venta():

    while True:
        print("---- ¿Que deceas hacer? ----")
        print("1. Ver registro de inventario \n2. Ver registro de ventas \n")
        print("3. Aplicar descuentos \n4. Registros de Facturas \n5. Saliendo del programa\n6. Volver al menu inicial")
        print()
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print("-----Ver registro de inventario-----")
            registro_intv()
        elif opcion == 2:
            print("----- Ver registro de ventas-----")
            registro_vent()
        elif opcion == 3:
            print("-----Aplicar descuentos-----")
            apli_descu()
        elif opcion == 4:
            print("-----Registros de Facturas-----")
            registros_fact()
        elif opcion == 5:
            print("Saliendo del programa...")
            sys.exit()
        elif opcion == 6:
            print("-----Volver al menu inicial-----")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def Agregar_articulos_inventario():
    print("\n---- Crear registro de asistencias ----\n")
    Agregar_articulos_inventario()

def Eliminar_articulos_inventario():
    print("\n----Ver registros de asistencias----\n")
    Eliminar_articulos_inventario()

def registro_intv():
   
    def clasesPerfumes():

        class Fragancia:
         def __init__(self, marca, fragancia, genero, cantidad, perdurabilidad, codigo, precio):
            self.marca = marca
            self.fragancia = fragancia
            self.genero = genero
            self.cantidad = cantidad
            self.perdurabilidad = perdurabilidad
            self.codigo = codigo
            self.precio = precio
            self.vende = False
            self.prueba = False

         def vender(self):
            self.vende = True

         def probar(self):
            self.prueba = True

         def imprimir(self):
            print(
                f"marca: {self.marca}\nfragancia: {self.fragancia} \n genero: {self.genero}\ncantidad: {self.cantidad} ml\nperdurabilidad: {self.perdurabilidad} horas\ncodigo: {self.codigo}\nprecio: {self.precio}\nvende: {self.vende}\nprueba: {self.prueba}\n"
            )

        class Perfume(Fragancia):
            pass

        print("----- Essenza Perfumes ------")

        APOLO = Perfume("APOLO", "dulce","masculino", 15, 3, 5665447, "$30")
        APOLO.imprimir()

        PARIS_HILTON = Perfume("PARIS HILTON", "frutal", "femenino", "236 ml", "4horas", 4584566, "$50" )
        PARIS_HILTON.imprimir()

        MANCERA_INSTANT = Perfume("MANCERA INSTANT","frutal","Unisex","100 ml","5 horas", 56622,"$120")
        MANCERA_INSTANT.imprimir()

        JUICY_COUTURE = Perfume("JUICY COUTURE","frutal","Femenino","100 ml","4 horas",555452,"$35")
        JUICY_COUTURE.imprimir()

        SAUVAGE = Perfume("SAUVAGE","FOUGERE","Masculino","200 ml","5 horas", 544112,"$100")
        SAUVAGE.imprimir()

        SHAKIRA_GOLDEN = Perfume("SHAKIRA GOLDEN","Floral","Femenino","80 ml", "3 horas",123589,"$45")
        SHAKIRA_GOLDEN.imprimir()

        GENTLE_ELSATYS = Perfume("GENTLE ELSATYS", "Floral","Masculino","100 ml","3 horas", 547889, "$40")
        GENTLE_ELSATYS.imprimir()

        INCANTO_CHARMS = Perfume("INCANTO CHARMS","Frutal", "Femenino","120 ml", "2 horas", 63359,"$50")
        INCANTO_CHARMS.imprimir()

        ESTUCHE_EIRESS = Perfume("ESTUCHE HEIRESS", "Floral","Femenino","300 ml","4 horas",54441,"$60")
        ESTUCHE_EIRESS.imprimir()

        POLO_VERDE = Perfume("POLO VERDE","Amaderada","Masculino","118 ml","4 horas",4455227,"$70")
        POLO_VERDE.imprimir()

    clasesPerfumes()
def main():
    while True:
        print("\n-----Menu Principal-----")
        print("1. Ver Clases de Perfumes")
        print("2. Agregar artículos a la venta")
        print("3. Agregar artículos al inventario")
        print("4. Eliminar Artículos del inventario")
        print("5. Salir")
        
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            registro_intv()
        elif opcion == 2:
            Agregar_articulos_venta()
            pass
        elif opcion == 3:
            Agregar_articulos_inventario()
            pass
        elif opcion == 4:
            Eliminar_articulos_inventario()
            pass
        elif opcion == 5:
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

    if __name__ == "__main__":
        main()


def registro_vent():
    import random

    class Fragancia:
        def __init__(self, marca, fragancia, genero, cantidad, perdurabilidad, codigo, precio, vendedor):
            self.marca = marca
            self.fragancia = fragancia
            self.genero = genero
            self.cantidad = cantidad
            self.perdurabilidad = perdurabilidad
            self.codigo = codigo
            self.precio = precio
            self.vendedor = vendedor

        def vender(self):
            self.vendido = True

        def probar(self):
            self.probado = True

    def obtener_perfume():
        marca = {
            'Perfume': ["APOLO", "PARIS_HILTON", "MANCERA_INSTANT", "JUICY_COUTURE", "SAUVAGE", "SHAKIRA_GOLDEN", "GENTLE_ELSATYS", "INCANTO_CHARMS", "ESTUCHE_EIRESS", "POLO_VERDE"],
        }
        return random.choice(marca['Perfume'])

    def mostrar_lista(lista):
        for i in range(len(lista)):
            print(f'{i + 1} - {lista[i]}')

    def main():
        inventario = []
        perfumes_vendidos = []
        for _ in range(11):
            inventario.append(obtener_perfume())

        while True:
            print('🟥🟥🟥🟥 Essencial perfumes 🟥🟥🟥🟥')
            print('=== perfumes disponibles ===')
            mostrar_lista(inventario)

            print("\n\n1. Vender perfume")
            print("2. Regresar al menú principal")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                indice_perfume_a_vender = int(input("\nCual perfume desea vender?: ")) - 1
                vendedor_de_perfume_a_vender = input("Nombre vendedor: ")

                perfume_vendido = obtener_perfume()

                if isinstance(perfume_vendido, Fragancia):
                    perfume_vendido.vendido = True
                    perfume_vendido.vendedor = vendedor_de_perfume_a_vender
                else:
                    print(f"El perfume {perfume_vendido} está vendido")

                print(f'\n\n{perfume_vendido}\n\n')
                perfumes_vendidos.append(perfume_vendido)
                inventario.pop(indice_perfume_a_vender)

                print('=== perfumes disponibles ===')
                mostrar_lista(inventario)
                print(' ++++++++++++++++++ ')
                mostrar_lista(perfumes_vendidos)

                print(f"Total de perfumes disponibles: {len(inventario)}")
            elif opcion == 2:
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    if __name__ == "__main__":
        main()

def apli_descu():
    import random

    class Fragancia:
        def __init__(self, marca, fragancia, genero, cantidad, perdurabilidad, codigo, precio, vendedor=None):
            self.marca = marca
            self.fragancia = fragancia
            self.genero = genero
            self.cantidad = cantidad
            self.perdurabilidad = perdurabilidad
            self.codigo = codigo
            self.precio = precio
            self.vendedor = vendedor
            self.vendido = False
            self.probado = False

        def vender(self, vendedor):
            self.vendido = True
            self.vendedor = vendedor

        def probar(self):
            self.probado = True

    def obtener_perfume():
        marcas = [
            ("APOLO", 100),
            ("PARIS_HILTON", 150),
            ("MANCERA_INSTANT", 200),
            ("JUICY_COUTURE", 120),
            ("SAUVAGE", 180),
            ("SHAKIRA_GOLDEN", 90),
            ("GENTLE_ELSATYS", 160),
            ("INCANTO_CHARMS", 130),
            ("ESTUCHE_EIRESS", 140),
            ("POLO_VERDE", 170)
        ]
        return random.choice(marcas)

    def mostrar_lista(lista):
        for i, fragancia in enumerate(lista, start=1):
            print(f'{i} - {fragancia.marca} ({fragancia.precio})')

    def main():
        inventario = []
        perfumes_vendidos = []
        contador_compras = 0

        for _ in range(11):
            marca, precio = obtener_perfume()
            fragancia = Fragancia(marca, "", "", 0, 0, 0, precio)  # Deja los campos en blanco para llenar después
            inventario.append(fragancia)

        while True:
            print('🟥🟥🟥🟥  Essenza Perfumes  🟥🟥🟥🟥')
            print('=== perfumes disponibles ===')
            mostrar_lista(inventario)

            print("\n\n1. Vender perfume")
            print("2. Regresar al menú principal")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                try:
                    indice_perfume_a_vender = int(input("\n¿Cuál perfume desea vender?: ")) - 1
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                
                vendedor_de_perfume_a_vender = input("Nombre vendedor: ")

                perfume_vendido = inventario.pop(indice_perfume_a_vender)
                perfume_vendido.vender(vendedor_de_perfume_a_vender)

                perfumes_vendidos.append(perfume_vendido)
                contador_compras += 1

                if contador_compras >= 2:
                    print("¡Tienes un 10% de descuento en tu compra!")
                    perfume_vendido.precio *= 0.9
                    print("¡Felicitaciones por tu descuento del 10%!")

                print(f'\n\n{perfume_vendido.marca} vendido\n\n')

                print('=== perfumes disponibles ===')
                mostrar_lista(inventario)
                print(' ++++++++++++++++++ ')
                mostrar_lista(perfumes_vendidos)
            elif opcion == 2:
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    if __name__ == "__main__":
        main()

def registros_fact():
    def obtener_perfume():
        marcas = ["APOLO", "PARIS_HILTON", "MANCERA_INSTANT", "JUICY_COUTURE", "SAUVAGE", "SHAKIRA_GOLDEN", "GENTLE_ELSATYS", "INCANTO_CHARMS", "ESTUCHE_EIRESS", "POLO_VERDE"]

        print("Marcas disponibles:")
        for index, marca in enumerate(marcas, start=1):
            print(f"{index}. {marca}")

        marca_index = int(input("Seleccione el número de la marca (0 para regresar al menú principal): ")) - 1

        if marca_index == -1:
            return None

        if 0 <= marca_index < len(marcas):
            marca_seleccionada = marcas[marca_index]

            cantidad = int(input(f"Cantidad comprada de {marca_seleccionada}: "))
            valor_unidad = int(input(f"Valor de la unidad de {marca_seleccionada}: "))

            precio = cantidad * valor_unidad
            print("Total a pagar:", precio)
        else:
            print("Selección de marca inválida.")

    if __name__ == "__main__":
        while True:
            print("----- Menú Principal -----")
            print("1. Comprar perfume")
            print("2. Salir")

            opcion_menu = int(input("Seleccione una opción: "))

            if opcion_menu == 1:
                obtener_perfume()
            elif opcion_menu == 2:
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    
def Agregar_articulos_inventario():
    import random

    class Fragancia:
        def __init__(self, marca, fragancia, genero, cantidad, perdurabilidad, codigo, precio, vendedor=None):
            self.marca = marca
            self.fragancia = fragancia
            self.genero = genero
            self.cantidad = cantidad
            self.perdurabilidad = perdurabilidad
            self.codigo = codigo
            self.precio = precio
            self.vendedor = vendedor
            self.vendido = False
            self.probado = False

        def vender(self, vendedor):
            self.vendido = True
            self.vendedor = vendedor

        def probar(self):
            self.probado = True

    def obtener_perfume():
        marcas = [
            ("APOLO", 100),
            ("PARIS_HILTON", 150),
            ("MANCERA_INSTANT", 200),
            ("JUICY_COUTURE", 120),
            ("SAUVAGE", 180),
            ("SHAKIRA_GOLDEN", 90),
            ("GENTLE_ELSATYS", 160),
            ("INCANTO_CHARMS", 130),
            ("ESTUCHE_EIRESS", 140),
            ("POLO_VERDE", 170)
        ]
        return random.choice(marcas)

    def mostrar_lista(lista):
        for i, fragancia in enumerate(lista, start=1):
            print(f'{i} - {fragancia.marca} ({fragancia.precio})')

    def agregar_articulo(inventario):
        marca = input("Ingrese la marca del nuevo perfume: ")
        precio = float(input("Ingrese el precio del nuevo perfume: "))
        fragancia = Fragancia(marca, "", "", 0, 0, 0, precio)
        inventario.append(fragancia)
        print(f"\nSe ha agregado '{marca}' a la lista de perfumes.")

    def main():
        inventario = []

        for _ in range(11):
            marca, precio = obtener_perfume()
            fragancia = Fragancia(marca, "", "", 0, 0, 0, precio)
            inventario.append(fragancia)

        while True:
            print('🟥🟥🟥🟥  Essenza Perfumes  🟥🟥🟥🟥')
            print('=== perfumes disponibles ===')
            mostrar_lista(inventario)

            print("\n\nOpciones:")
            print("1. Agregar más artículos")
            print("2. Salir")
            opcion = input("Seleccione una opción (1/2): ")

            if opcion == "1":
                agregar_articulo(inventario)
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione 1 o 2.")

    if __name__ == "__main__":
        main()       

def Eliminar_articulos_inventario():
    import random

    class Fragancia:
        def __init__(self, marca, fragancia, genero, cantidad, perdurabilidad, codigo, precio, vendedor=None):
            self.marca = marca
            self.fragancia = fragancia
            self.genero = genero
            self.cantidad = cantidad
            self.perdurabilidad = perdurabilidad
            self.codigo = codigo
            self.precio = precio
            self.vendedor = vendedor
            self.vendido = False
            self.probado = False

        def vender(self, vendedor):
            self.vendido = True
            self.vendedor = vendedor

        def probar(self):
            self.probado = True

    def obtener_perfume():
        marcas = [
            ("APOLO", 100),
            ("PARIS_HILTON", 150),
            ("MANCERA_INSTANT", 200),
            ("JUICY_COUTURE", 120),
            ("SAUVAGE", 180),
            ("SHAKIRA_GOLDEN", 90),
            ("GENTLE_ELSATYS", 160),
            ("INCANTO_CHARMS", 130),
            ("ESTUCHE_EIRESS", 140),
            ("POLO_VERDE", 170)
        ]
        return random.choice(marcas)

    def mostrar_lista(lista):
        for i, fragancia in enumerate(lista, start=1):
            print(f'{i} - {fragancia.marca} ({fragancia.precio})')

    def eliminar_articulo(inventario):
        mostrar_lista(inventario)
        try:
            indice_articulo_a_eliminar = int(input("Seleccione el perfume a eliminar: ")) - 1
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return

        if 0 <= indice_articulo_a_eliminar < len(inventario):
            perfume_eliminado = inventario.pop(indice_articulo_a_eliminar)
            print(f"\nSe ha eliminado '{perfume_eliminado.marca}' de la lista de perfumes.")
        else:
            print("Índice inválido. Por favor, seleccione un número válido.")

    def main():
        inventario = []

        for _ in range(11):
            marca, precio = obtener_perfume()
            fragancia = Fragancia(marca, "", "", 0, 0, 0, precio)
            inventario.append(fragancia)

        while True:
            print('🟥🟥🟥🟥  Essenza Perfumes  🟥🟥🟥🟥')
            print('=== perfumes disponibles ===')
            mostrar_lista(inventario)

            print("\n\nOpciones:")
            print("1. Eliminar un perfume")
            print("2. Salir")
            opcion = input("Seleccione una opción (1/2): ")

            if opcion == "1":
                eliminar_articulo(inventario)
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione 1 o 2.")

    if __name__ == "__main__":
        main()
  
def password():
    print("Ingrese su usuario de acceso:")
    username = input()

    print("Ingrese su contraseña:")
    password = input()

    with open("./users.txt", "a") as file:
        file.write(f"{username} {password}\n")

    print("Usuario y contraseña creados exitosamente.")

if __name__ == "__main__":
    while True:
        password()

        while True:
            show_main_menu()

            main_option = int(input())

            if main_option == 1:
                Agregar_articulos_venta()
            elif main_option == 2:
                Agregar_articulos_inventario()
            elif main_option == 3:
                Eliminar_articulos_inventario()
            elif main_option == 4:
                print("Saliendo del programa...")
                sys.exit()
            else:
                print("Opción inválida. Inténtalo de nuevo.")
