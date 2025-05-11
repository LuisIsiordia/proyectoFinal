import datos
import validar
def agregarTalleres():
  import menu
  while True:
        try:
            idtaller = int(input("ID del Taller: "))
            break
        except ValueError:
            print("Tipo de dato incorrecto, ingrese un número")
            continue
  for id in datos.talleres:
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

  respuestaAgregar = input("¿Confirmar el registro? (S/N): ").upper()
  validar.validarAgregar(respuestaAgregar)
  if respuestaAgregar == "N":
    agregarTalleres()
  elif respuestaAgregar == "S":
      datos.talleres[idtaller] = {
      "nombre": nombreTaller,
      "fecha": fechaInicio,
      "hora": horaCompleta,
      "duracion": f"{duracionTaller} horas",
      "lugar": lugarTaller,
      "capacidad": capEstudiantes,
      "costo": costoTaller  
    }
  for id,dato in sorted(datos.talleres.items()):  
    print(f"\n Taller ID: {id}")
    print(f" Nombre: {dato['nombre']}")
    print(f" Fecha: {dato['fecha']}")
    print(f" Hora: {dato['hora']}")
    print(f" Duración: {dato['duracion']}")
    print(f" Lugar: {dato['lugar']}")
    print(f" Capacidad: {dato['capacidad']} estudiantes")
    print(f" Costo: ${dato['costo']:.2f}")
  respuestaAñadir = input("¿Quiere añadir otro taller?: ").upper()
  validar.validarAñadir(respuestaAñadir)
  if respuestaAñadir == "S":
    agregarTalleres()
  elif respuestaAñadir == "N":
    menu.menu()


  
  
