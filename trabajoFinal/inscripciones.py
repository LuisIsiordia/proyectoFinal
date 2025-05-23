import utilerias
from datos import talleres, estudiantes, inscripcionesTupla
from datetime import date

def registroInscripcionTaller(resp):
    utilerias.limpiarPantalla()
    utilerias.ordenamientoTalleres(resp)
    #Selección de taller
    while True:
        idTaller = int(input("\nIngrese el ID del taller al que quiere hacer una inscripción"
                             "\nEn caso de querer cancelar la inscripción ingrese un valor negativo (-1,-2, etc): "))
        if idTaller < 0:
            import menu
            menu.menu()
        if idTaller in talleres:
            utilerias.mostrarTaller(idTaller)
            break
        else:
            print("\nNo hay ningún taller con ese ID, seleccione otra opción")

    #Selección de estudiante a inscribir
    while True:
            idEstudiante = int(input("\nIngrese el ID del estudiate que se va a inscribir: "))
            estudianteExistente = None

            #Recorrido de la tupla para encotrar el ID y guardarlo para uso posterior
            for estudiante in estudiantes:
                if estudiante[0] == idEstudiante:
                    estudianteExistente = estudiante
                    break
            #Verificación de si el estudiante ya esta inscrito al taller
            while True:
                inscrito = any(i[2] == idEstudiante and i[3] == idTaller for i in inscripcionesTupla)
                if inscrito:
                    print("\nEl estudiante ya está inscrito en este taller")
                    empiezo = input("Quiere seleccionar otro taller (S/N): ").upper()
                    utilerias.validarSiNo(empiezo)
                    if empiezo == "S":
                        registroInscripcionTaller(resp)
                    if empiezo == "N":
                        utilerias.llamarMenu()
                else:
                    break    

            #Mostrado de los datos del estudiante
            if any(idEstudiante == ID[0] for ID in estudiantes):
                print("\n----------------------------Datos del estudiante--------------------------")
                print(f"Nombre: {estudianteExistente[1]}")
                print(f"Correo: {estudianteExistente[2]}")
                print(f"Teléfono: {estudianteExistente[3]}")
                print(f"exento: {'Sí' if estudianteExistente[4] else 'No'}")
                break
            else:
                print("\nNo hay ningún estudiante con ese ID, seleccione otra opción")

    ConfirmarRegistro = input("¿Confirmar el registro? (S/N): ").upper()
    utilerias.validarSiNo((ConfirmarRegistro))
    if ConfirmarRegistro == "S":
        #Fecha de la inscripción
        fechaInscripcion = date.today().isoformat()
        #Generar folio
        if inscripcionesTupla:
            folio = inscripcionesTupla[-1][0] + 1
        else:
            folio = 1
        inscripcion = (folio, fechaInscripcion, idEstudiante, idTaller)
        inscripcionesTupla.append(inscripcion)
    utilerias.mostrarTaller(idTaller)
    print("\n----------------------------Datos de la inscripción-----------------------")

    print(f"Folio: {folio}")
    print(f"fecha inscripcion: {fechaInscripcion}")
    print(f"ID: {estudianteExistente[0]}")
    # Mostrar datos del estudiante
    print("\n----------------------------Datos del estudiante--------------------------")
    print(f"Nombre: {estudianteExistente[1]}")
    print(f"Correo: {estudianteExistente[2]}")
    print(f"Teléfono: {estudianteExistente[3]}")
    print(f"exento: {'Sí' if estudianteExistente[4] else 'No'}")
    # Mostrar detalles del cobro
    print("\n----------------------------Detalles del cobro---------------------------")
    if estudianteExistente[4]:
        print("El estudiante está exento de cobro\n")
    else:
        print(f"Se cobrará: ${talleres[idTaller]['costo']:.2f}\n")
    
    if ConfirmarRegistro == "N":
        HacerOtroRegistro = input("¿Continuar con otra inscripción a un taller (S/N)?: ").upper()

    HacerOtroRegistro = input("¿Continuar con otra inscripción a un taller (S/N)?: ").upper()
    while HacerOtroRegistro != "S" and HacerOtroRegistro != "N":
        print("Tipo de respuesta invalida escoja solo entre estos dos caracter ('S' o 'N')")
        HacerOtroRegistro = input("¿Continuar con otra inscripción a un taller (S/N)?: ").upper()
    if HacerOtroRegistro == "S":
        registroInscripcionTaller(resp)
    if HacerOtroRegistro == "N":
        import menu
        menu.menu()

def cancelarInscripcionFolio():
    global inscripcionesTupla
    #Mostrar todas las inscripciones ordenadas por folio
    utilerias.formatoListadoInsc()
    for insc in inscripcionesTupla:
        folio, fechaInscripcion, idEstudiante, idTaller = insc
    # Buscar información del estudiante
    estudiante = next((e for e in estudiantes if e[0] == idEstudiante), None)
    # Buscar información del taller
    taller = talleres.get(idTaller, {"nombre": "Taller Desconocido", "costo": 0})
    
    while True:
        folio = int(input("\nSeleccione un folio de una inscripción a cancelar"
                          "\nEn caso de querer volver al menu ingrese un valor negativo (-1,-2, etc): "))
        if folio < 0:
            utilerias.llamarMenu()
        if any(folio == folioTupla[0] for folioTupla in inscripcionesTupla):  
            # Mostrar datos de la inscripción
            print("\n----------------------------Datos de la inscripción-----------------------")
            print(f"Folio: {folio:06d}")
            print(f"Taller: {taller['nombre']}")
            print(f"Fecha de la inscripción: {fechaInscripcion}")
            print(f"ID del estudiante: {idEstudiante:011d}")
            if estudiante:
                print(f"Nombre: {estudiante[1]}")
                print(f"Correo electrónico: {estudiante[2]}")
                print(f"Teléfono: {estudiante[3]}")
                print(f"¿Exento?: {'Sí' if estudiante[4] else 'No'}")
            print("\n----------------------------Detalles del cobro---------------------------")
            if estudiante and estudiante[4]:
                print("El estudiante está exento de cobro.")
            else:
                print(f"Se cobrará: ${taller['costo']:.2f}")
            cancelar = input("¿Confirmar que desea eliminar la inscripción? (S/N): ").upper()
            utilerias.validarSiNo(cancelar)
            if cancelar == "S":
                inscripcionesTupla = [i for i in inscripcionesTupla if i[0] != folio]
                break
            if cancelar == "N":
                cancelarInscripcionFolio()
        else:
            print("\nNo hay ninguna inscripcón con ese folio, seleccione otra opción")
        
     #cancelación confirmada mostrar el listado de nuevo
    print("\nLista actualizada de inscripciones:")
    print("-"*90)
    print(f"{'Folio':<8}{'Taller':<20}{'ID Estudiante':<15}{'Nombre estudiante':<25}{'Costo':>10}")
    print("-"*90)
                
    for insc in inscripcionesTupla:
        folio, fechaInscripcion, idEstudiante, idTaller = insc
        estudiante = next((e for e in estudiantes if e[0] == idEstudiante), None)
        taller = talleres.get(idTaller, {"nombre": "Taller Desconocido", "costo": 0})
        costo = "0.00" if estudiante and estudiante[4] else f"{taller['costo']:.2f}"
        print(f"{folio:<8}{taller['nombre']:<20}{idEstudiante:<15}{estudiante[1] if estudiante else 'Desconocido':<25}${costo:>9}")
                
    print("-"*90)
    print(f"Total de inscripciones: {len(inscripcionesTupla)}")
    print("-"*90)
    respuestaCancelar = input("¿Quiere cancelar otra inscripción? (S/N): ").upper()
    utilerias.validarSiNo(respuestaCancelar)
    if respuestaCancelar == "S":
        cancelarInscripcionFolio()
    elif respuestaCancelar == "N":
        utilerias.llamarMenu
        
def cancelarInscripcionIDtaller(idtaller):
    global inscripcionesTupla
    inscripcionesTupla = [i for i in inscripcionesTupla if i[3] != idtaller]

def listadoInscripcionesTaller():
    print("-"*51)
    print("Listado de inscripciones por taller")
    while True:
        ordenar = input("\n¿Desea un listado ordenado? (S/N): ").upper()
        orden = 'A'  # Por defecto ascendente
        if ordenar == 'S':
            while True:
                orden = input("Indique el orden (A=ascendente, D=descendente): ").upper()
                if orden in ['A', 'D']:
                    break
                print("Error: Debe ingresar A o D")
        

        # Preparar datos para mostrar
        datos = []
        for insc in inscripcionesTupla:
            folio, fechaInscripcion, idEstudiante,idTaller = insc  # Desempaquetar tupla
            # Buscar estudiante en la lista de tuplas
            estudiante = None
            for e in estudiantes:
                if e[0] == idEstudiante:
                    estudiante = e
                    break
            if estudiante is None:
                # Si no lo encontró, usar valores por defecto
                exento = False
            else:

                exento = estudiante[4]
            taller = talleres.get(idTaller, {"nombre": "Taller Desconocido", "Costo": 0})
            
            costo = "0.00" if exento else f"{taller['costo']:.2f}"
            
            datos.append({
                "Folio": folio,
                "Taller": taller["nombre"],
                "ID_Estudiante": idEstudiante,
                "Nombre": estudiante[1],
                "Costo": costo,
                "Fecha": fechaInscripcion
            })

        
        # Aplicar ordenamiento si se solicitó
        if ordenar == 'S':
            reverseOrder = (orden == 'D')
            datos.sort(key=lambda x: x["Taller"], reverse=reverseOrder)
        
        # Mostrar resultados
        print("\nListado de Inscripciones a Talleres")
        print("-" * 90)
        print(f"{'Folio':<8}{'Taller':<20}{'ID Estudiante':<15}{'Nombre':<25}{'Costo':>10}{'Fecha':>12}")
        print("-" * 90)
        
        for item in datos:
            print(f"{item['Folio']:<8}{item['Taller']:<20}{item['ID_Estudiante']:<15}"
                f"{item['Nombre']:<25}${item['Costo']:>9}{item['Fecha']:>12}")
        
        print("-" * 90)
        print(f"Total de inscripciones: {len(inscripcionesTupla)}")
        print("-" * 90)
        resp=input("Presione enter para volver al menu:").upper()
        if resp == "":
            utilerias.llamarMenu()

