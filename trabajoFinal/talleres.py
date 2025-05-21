from datos import talleres,inscripcionesTupla,estudiantes
import inscripciones
import utilerias


def agregarTalleres():
  utilerias.limpiarPantalla()
  print("-"*51)
  print("Agregar un nuevo taller\n")
  while True:
        try:
            idtaller = int(input("ID del Taller: "))
            break
        except ValueError:
            print("Tipo de dato incorrecto, ingrese un número")
            continue
  if idtaller < 0:
     print("ID invalido escoga otro valor")   
     agregarTalleres() 
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
  utilerias.validarSiNo(respuestaAgregar)
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

  utilerias.ordenamientoTalleres(respuestaAgregar)
  respuestaAñadir = input("¿Quiere añadir otro taller?: ").upper()
  utilerias.validarSiNo(respuestaAñadir)
  if respuestaAñadir == "S":
    agregarTalleres()
  elif respuestaAñadir == "N":
    utilerias.llamarMenu

def bajaTalleres(resp):
    utilerias.ordenamientoTalleres(resp)
    while True:
        try:
          idtaller = int(input("Ingrese el ID del Taller (valor negativo para ir al Menú): "))

          if idtaller < 0:
            import menu
            menu.menu()
          break
        except ValueError:
            print("Tipo de dato incorrecto, ingrese un número")
            continue
          
    if idtaller not in talleres:
      print("El taller que busca dar de baja no existe en el catalogo.\n")
      bajaTalleres(resp)
    if idtaller in talleres:
      utilerias.mostrarTaller(idtaller)
      # Verificar inscripciones existentes
      inscripciones_taller = [i for i in inscripcionesTupla if i[3] == idtaller]

      if inscripciones_taller:
          print("\nInscripciones registradas")
          print("-"*80)
          print(f"{'Folio':<8}{'Tipo':<10}{'Fecha':<12}{'ID estudiante':<15}{'Nombre estudiante':<25}")
          print("-"*80)
          
          for insc in inscripciones_taller:
              try:
                  folio, fecha, idEstudiante, _ = insc
                  estudiante = next((e for e in estudiantes if e[0] == idEstudiante), None)
                  tipo = "Exenta" if estudiante and estudiante[4] else "General"
                  print(f"{folio:<8}{tipo:<10}{fecha:<12}{idEstudiante:<15}{estudiante[1] if estudiante else 'Desconocido':<25}")
              except (ValueError, TypeError) as e:
                  print(f"Error procesando inscripción: {insc} - {str(e)}")
          
          print("-"*80)
      eliminar = input("Confirmar baja del taller?: (S/N): ").upper()
      if eliminar == "S":
          if any(insc[3] == idtaller for insc in inscripcionesTupla):
            borrarInsc = input("Hay inscripciones a ese taller y requiere primero cancelar las inscripciones del taller,"
                              "\nantes de poder borrar el taller."
                              "\n¿Desea cancelar las inscripciones?"
                              "\nEn caso de que no, volvera al menu principal (S/N): ").upper()
            if borrarInsc == "S":
              inscripciones.cancelarInscripcionIDtaller(idtaller)
              eliminar = input("Inscripciones dadas de baja ¿Continuar baja de taller? (S/N): ").upper()
              if eliminar == "S":
                del talleres [idtaller]
                utilerias.ordenamientoTalleres(resp)
                resp=input("Presione enter para volver al menu:").upper()
                if resp == "":
                    utilerias.llamarMenu()
              if eliminar == "N":
                utilerias.llamarMenu()
            if borrarInsc == "N":
                utilerias.llamarMenu()
          del talleres [idtaller]
          utilerias.ordenamientoTalleres(resp)
          resp=input("Presione enter para volver al menu:").upper()
          if resp == "":
              utilerias.llamarMenu()

      if eliminar == "N":
        bajaTalleres(resp)


def actualizarTalleres(resp):
    utilerias.ordenamientoTalleres(resp)
    while True:
        idTaller = int(input("\nIngrese el ID del Taller (valor negativo para ir al Menú):"))

        if idTaller < 0:
          utilerias.llamarMenu()
        if idTaller in talleres:
          utilerias.mostrarTaller(idTaller)
          taller = talleres[idTaller]
          break
        else:
          print("\nNo hay ningún taller con ese ID, seleccione otra opción")
    print("Presione Enter si no desea actualizar nada")
    nuevoNombre = input("Nuevo nombre del taller: ")
    nuevaFecha = input("Nueva Fecha de inicio: ")
    nuevaHora = input("Nueva Hora de inicio: ")
    while True:
          try:
              nuevaDuracion = int(input(f"Nueva duración del taller en horas: "))
              break
          except ValueError:
              print("\nTipo de dato incorrecto, ingrese un número")
              continue
    nuevoLugar = input("Nueva Aula del taller: ")
    while True:
      try:
          nuevaCapacidad = int(input("Nueva capacidad de alumnos en el taller: "))
          break
      except ValueError:
          print("\nTipo de dato incorrecto, ingrese un número")
          continue
    while True:
      nuevoCosto = input("Nuevo Costo del taller: ")
      if nuevoCosto == "":  
            nuevoCosto = taller['costo']
            break
      try:
            nuevoCosto = float(nuevoCosto)
            break     
      except ValueError:
          print("\nTipo de dato incorrecto, ingrese un número")
          continue
    # Mostrar cambios
    print("\nInformación actualizada del taller")
    print("-"*50)
    print(f"Nombre: {taller['nombre']} -> {nuevoNombre}")
    print(f"Fecha: {taller['fecha']} -> {nuevaFecha}")
    print(f"Hora: {taller['hora']} -> {nuevaHora}")
    print(f"Duración: {taller['duracion']} -> {nuevaDuracion} horas")
    print(f"Lugar: {taller['lugar']} -> {nuevoLugar}")
    print(f"Capacidad: {taller['capacidad']} -> {nuevaCapacidad}")
    print(f"Costo: ${taller['costo']:.2f} -> ${nuevoCosto:.2f}")
    print("-"*50)
    
    actualizar = input("\n¿Confirmar la actualización? (S/N): ").upper()
    utilerias.validarSiNo(actualizar)
    if actualizar == "S":
      if nuevoNombre != "":
          taller['nombre'] = nuevoNombre
      if nuevaFecha != "":
          taller['fecha'] = nuevaFecha
      if nuevaHora != "":
          taller['hora'] = nuevaHora
      if nuevaDuracion != "":
          taller['duracion'] = f"{nuevaDuracion} horas"
      if nuevoLugar != "":
          taller['lugar'] = nuevoLugar
      if nuevaCapacidad != "":
          taller['capacidad'] = int(nuevaCapacidad)
      if nuevoCosto != "":
          taller['costo']=float(nuevoCosto)
      utilerias.ordenamientoTalleres(resp)
    if actualizar == "N":
      otroActualizar = input("¿Continuar con la actualización de otro Taller? (S/N): ").upper()
      utilerias.validarSiNo(otroActualizar)
      if otroActualizar == "S":
        actualizarTalleres(resp)
      if otroActualizar == "N":
        utilerias.llamarMenu()     
    otroActualizar = input("¿Continuar con la actualización de otro Taller? (S/N): ").upper()
    utilerias.validarSiNo(otroActualizar)
    if otroActualizar == "S":
       actualizarTalleres(resp)
    if otroActualizar == "N":
       utilerias.llamarMenu()
       
    
def mostrarListado(resp):
    utilerias.ordenamientoTalleres(resp)