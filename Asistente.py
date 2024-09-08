contratos = []


def CrearContrato():
    empleado = input("Ingrese el nombre del empleado: ")
    metroCuadrados = input("Ingrese la cantidad de metros cuadrados en los que se realizara el aseo: ")
    nombre = input("Ingrese el nombre completo del cliente: ")
    identidad = input("Ingrese su numero de identidad del cliente: ")
    precio = input("Ingrese el precio del contrato: ")
    estado = ["En espera", "En proceso", "Finalizado"]
    contrato = {
        "empleado": empleado,
        "metroCuadrados": metroCuadrados,
        "nombre": nombre,
        "identidad": identidad,
        "precio": precio,
        "Estado": estado[0]
    }
    contratos.append(contrato)
    print("Contrato creado con éxito:")
    print(contrato)


def CambiarEstado(contrato):
    print(f"Estado actual del contrato: {contrato['Estado']}")
    print("0. En espera")
    print("1. En Proceso")
    print("2. Finalizado")
    opcion = input("Ingrese el nuevo estado: ")
    if opcion == "0":
        contrato["Estado"] = "En espera"
    elif opcion == "1":
        contrato["Estado"] = "En proceso"
    elif opcion == "2":
        contrato["Estado"] = "Finalizado"
    else:
        print("Opcion invalida")
    print("Estado actualizado:")
    print(contrato)


def BuscarContrato():
    print("Buscar contrato por: ")
    print("1. Nombre del empleado")
    print("2. Nombre del cliente")
    print("3. Identidad del cliente")
    opcion = input("Ingrese la opcion que desee: ")

    if opcion == "1":
        nombre_empleado = input("Ingrese el nombre del empleado: ")
        for contrato in contratos:
            if contrato['empleado'] == nombre_empleado:
                print(contrato)
    elif opcion == "2":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        for contrato in contratos:
            if contrato['nombre'] == nombre_cliente:
                print(contrato)
    elif opcion == "3":
        identidad_cliente = input("Ingrese la identidad del cliente: ")
        for contrato in contratos:
            if contrato['identidad'] == identidad_cliente:
                print(contrato)
    else:
        print("Opcion invalida")


def ListarContratos():
    print("Lista de contratos:")
    for contrato in contratos:
        print(contrato)
    print("---------------------------------------------------")


# Menu principal
while True:
    print("Menu principal: ")
    print("1. Agregar contrato")
    print("2. Cambiar estado del contrato")
    print("3. Buscar contrato")
    print("4. Listar contratos")
    print("5. Salir")
    opcion = input("Ingrese la opcion que desee: ")

    if opcion == "1":
        CrearContrato()
    elif opcion == "2":
        if contratos:
            contrato_idx = int(input("Ingrese el número del contrato que desea modificar (empezando desde 0): "))
            if 0 <= contrato_idx < len(contratos):
                CambiarEstado(contratos[contrato_idx])
            else:
                print("Índice de contrato no válido.")
        else:
            print("No hay contratos disponibles.")
    elif opcion == "3":
        BuscarContrato()
    elif opcion == "4":
        ListarContratos()
    elif opcion == "5":
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opcion invalida, por favor intente de nuevo")
