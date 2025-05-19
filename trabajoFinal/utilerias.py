from datos import talleres

#Validación para agregar un taller
def validarSiNo(respuestaAgregar):
    while respuestaAgregar != "S" and respuestaAgregar != "N":
        print("Tipo de respuesta invalida escoja solo entre estos dos caracter ('S' o 'N')")
        respuestaAgregar = input("¿Confirmar el registro? (S/N): ").upper()
    return respuestaAgregar

def llamarMenu():
    import menu
    menu.menu()



def ordenamientoTalleres(resp):
    if resp == "4":
        
        # Mostrar opciones de ordenamiento
        print("\nMostrar el listado de talleres")
        print("Indique el campo de interés (I=ID, D=duración, L=lugar, C=costo):")
        campo = input("-> ").upper()
        if campo == "":
            import menu
            menu.menu()
        print("Indique el Orden (A=ascendente, D=Descendente):")
        orden = input("-> ").upper()

        # Validar entrada del campo
        while campo not in ['I', 'D', 'L', 'C']:
            print("Opción no válida. Intente nuevamente.")
            campo = input("Indique el campo de interés (I=ID, D=duración, L=lugar, C=costo)-> ").upper()

        # Validar entrada del orden
        while orden not in ['A', 'D']:
            print("Opción no válida. Intente nuevamente.")
            orden = input("Indique el Orden (A=ascendente, D=Descendente)-> ").upper()

        # Determinar la clave de ordenamiento y el orden
        if campo == 'I':
            clave = lambda x: x[0]  # Ordenar por ID
        elif campo == 'D':
            clave = lambda x: x[1]['duracion']  # Ordenar por duración
        elif campo == 'L':
            clave = lambda x: x[1]['lugar']  # Ordenar por lugar
        elif campo == 'C':
            clave = lambda x: x[1]['costo']  # Ordenar por costo

        # Ordenar los talleres
        talleresOrdenados = sorted(talleres.items(), key=clave, reverse=(orden == 'D'))
        
        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Fecha", "Hora", "Duración", "Lugar", "Capacidad", "Costo"]

        # Anchos fijos para las columnas
        anchoID = 6
        anchoNombre = 25
        anchoFecha = 12
        anchoHora = 12
        anchoDuracion = 12
        anchoLugar = 10
        anchoCapacidad = 10
        anchoCosto = 10

        # Formato de impresión
        formato = f"{{:<{anchoID}}}  {{:<{anchoNombre}}}  {{:<{anchoFecha}}}  {{:<{anchoHora}}}  {{:<{anchoDuracion}}}  {{:<{anchoLugar}}}  {{:<{anchoCapacidad}}}  {{:<{anchoCosto}}}"

        # Imprimir encabezado
        print("Talleres disponibles en la Semana de ISW")
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))
        print(formato.format(*headers))
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))

        # Imprimir cada taller desde el diccionario talleres
        for idTaller, datosTaller in talleresOrdenados:
            print(formato.format(
                str(idTaller),
                datosTaller["nombre"],
                datosTaller["fecha"],
                datosTaller["hora"],
                datosTaller["duracion"],
                datosTaller["lugar"],
                str(datosTaller["capacidad"]),
                f"${datosTaller['costo']:.2f}"
            ))

        # Contar los talleres
        totalTalleres = len(talleres)
        # Total de talleres
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))
        print(f"Total de Talleres:{totalTalleres}")
        
        resp=input("Presione enter para volver al menu:").upper()
        if resp == "":
            import menu
            menu.menu()

        
    if resp == "S" or resp == "5" or resp == "4" or resp == "3" or resp == "2":
        # Encabezados de la tabla
        headers = ["ID", "Nombre", "Fecha", "Hora", "Duración", "Lugar", "Capacidad", "Costo"]

        # Anchos fijos para las columnas
        anchoID = 6
        anchoNombre = 25
        anchoFecha = 12
        anchoHora = 12
        anchoDuracion = 12
        anchoLugar = 10
        anchoCapacidad = 10
        anchoCosto = 10

        # Formato de impresión
        formato = f"{{:<{anchoID}}}  {{:<{anchoNombre}}}  {{:<{anchoFecha}}}  {{:<{anchoHora}}}  {{:<{anchoDuracion}}}  {{:<{anchoLugar}}}  {{:<{anchoCapacidad}}}  {{:<{anchoCosto}}}"

        # Imprimir encabezado
        print("Talleres disponibles en la Semana de ISW")
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))
        print(formato.format(*headers))
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))

        # Imprimir cada taller desde el diccionario talleres
        for idTaller,dato in sorted(talleres.items()):  
            print(formato.format(
                str(idTaller),
                dato["nombre"],
                dato["fecha"],
                dato["hora"],
                dato["duracion"],
                dato["lugar"],
                str(dato["capacidad"]),
                f"${dato['costo']:.2f}"
            ))

        # Contar los talleres
        totalTalleres = len(talleres)
        # Total de talleres
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))
        print(f"Total de Talleres:{totalTalleres}")

def mostrarTaller(idtaller):
     # Encabezados de la tabla
        headers = ["ID", "Nombre", "Fecha", "Hora", "Duración", "Lugar", "Capacidad", "Costo"]

        # Anchos fijos para las columnas
        anchoID = 6
        anchoNombre = 25
        anchoFecha = 12
        anchoHora = 12
        anchoDuracion = 12
        anchoLugar = 10
        anchoCapacidad = 10
        anchoCosto = 10

        # Formato de impresión
        formato = f"{{:<{anchoID}}}  {{:<{anchoNombre}}}  {{:<{anchoFecha}}}  {{:<{anchoHora}}}  {{:<{anchoDuracion}}}  {{:<{anchoLugar}}}  {{:<{anchoCapacidad}}}  {{:<{anchoCosto}}}"

        # Imprimir encabezado
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))
        print(formato.format(*headers))
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))

        # Imprimir cada taller desde el diccionario talleres
        if idtaller in talleres:
            dato = talleres[idtaller] 
            print(formato.format(
                str(idtaller),
                dato["nombre"],
                dato["fecha"],
                dato["hora"],
                dato["duracion"],
                dato["lugar"],
                str(dato["capacidad"]),
                f"${dato['costo']:.2f}"
            ))
        print("-" * (anchoID + anchoNombre + anchoFecha + anchoHora + anchoDuracion + anchoLugar + anchoCapacidad + anchoCosto + 15))
def limpiarPantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
