import datos
def agregarTalleres():
  idtaller = int(input("ID del Taller: "))
  for id in datos.talleres:
    if idtaller == id:
      print("Ya hay un taller con ese ID \npor favor seleccione otro número\n ")
      agregarTalleres()
  nombreTaller = input("Nombre del Taller: ")
  fechaInicio = input ("Fecha de inicio del taller: ")
  turno = input ("Ingrese el turno AM/PM").upper()
  horaInicio = input ("Hora inicio del taller: ")
  duracionTaller = input ("Duración del taller en horas: ")
  lugarTaller = input ("Aula del taller: ").upper()
  capEstudiantes = int(input("Cupo maximo de estudiantes: "))
  costoTaller = float(input("Costo del taller: "))
  
  respuestaAgregar = input("¿Confirmar el registro? (S/N): ").upper()
  validar.validarAgregar(respuestaAgregar)
  if respuestaAgregar == "N":
    agregarTalleres()
