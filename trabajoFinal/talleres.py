from datos import talleres
import utilerias


def agregarTalleres():
  while True:
        try:
            idtaller = int(input("ID del Taller: "))
            break
        except ValueError:
            print("Tipo de dato incorrecto, ingrese un número")
            continue
  for id in talleres:
    if idtaller == id:
      print("Ya hay un taller con ese ID \npor favor seleccione otro número\n ")
      agregarTalleres()
      break
  nombreTaller = input("Nombre del Taller: ")
  fechaInicio = input ("Fecha de inicio del taller: ")
  turno = input ("Ingrese el turno AM/PM: ").upper()
  while turno != "AM" and turno != "PM":
    turno = input ("Tipo de turno invalido escoja entre AM o PM: ").upper()
  horaInicio = input ("Hora inicio del taller: ")
  horaCompleta = f"{horaInicio} {turno}"
  duracionTaller = input ("Duración del taller en horas: ")
  duracionHoras = f"{duracionTaller} horas"
  lugarTaller = input ("Aula del taller: ").upper()
  capEstudiantes = int(input("Cupo maximo de estudiantes: "))
  costoTaller = float(input("Costo del taller: "))
  #mostrar datos con formato aplicado antes de confirmacion
  print("\n---------------Datos Adicionales--------------------",
  "\nNombre del taller:",nombreTaller,
  "\nFecha:",fechaInicio,
  "\nHora de inicio:",horaCompleta,
  "\nDuración:",duracionHoras,
  "\nLugar:",lugarTaller,
  "\nCapacidad máxima:",capEstudiantes,
  "\nCosto:$",costoTaller ,
  )
  print("-"*53)
  respuestaAgregar = input("¿Confirmar el registro? (S/N): ").upper()
  utilerias.validarAgregar(respuestaAgregar)
  if respuestaAgregar == "N":
    agregarTalleres()
  elif respuestaAgregar == "S":
      talleres[idtaller] = {
      "nombre": nombreTaller,
      "fecha": fechaInicio,
      "hora": horaCompleta,
      "duracion": f"{duracionTaller} horas",
      "lugar": lugarTaller,
      "capacidad": capEstudiantes,
      "costo": costoTaller  
    }
  for id,dato in sorted(talleres.items()):  
    print(f"\n Taller ID: {id}")
    print(f" Nombre: {dato['nombre']}")
    print(f" Fecha: {dato['fecha']}")
    print(f" Hora: {dato['hora']}")
    print(f" Duración: {dato['duracion']}")
    print(f" Lugar: {dato['lugar']}")
    print(f" Capacidad: {dato['capacidad']} estudiantes")
    print(f" Costo: ${dato['costo']:.2f}")
  respuestaAñadir = input("¿Quiere añadir otro taller?: ").upper()
  utilerias.validarAñadir(respuestaAñadir)
  if respuestaAñadir == "S":
    agregarTalleres()
  elif respuestaAñadir == "N":
    import menu
    menu.menu()

def actualizarTalleres():
  print("opcion para actualizar talleres")

def bajaTalleres():
  print("opcion para dar de baja talleres")
 
def mostrarListado():

  # Mostrar opciones de ordenamiento
  print("\nMostrar el listado de talleres")
  print("Indique el campo de interés (I=ID, D=duración, L=lugar, C=costo):")
  campo = input("-> ").upper()
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
  
  resp=input("ingrese 1 para volver al menu:").upper()
  if resp == "1":
      import menu
      menu.menu()
