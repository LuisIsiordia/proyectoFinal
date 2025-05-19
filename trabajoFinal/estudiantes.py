import datos
import utilerias

def estudiantes():
    print("-"*90)
    print("-"*33,"Listado de Estudiantes","-"*33)
    print("-"*90)
    totalEstudiantes=0
    headers = ["ID", "Nombre", "Correo", "Teléfono", "Exento"]

    # Asignar anchos fijos a las columnas 
    anchoID = 6
    anchoNombre = 25
    anchoCorreo = 30
    anchoTel = 12
    anchoExentos = 7

    # Formato de impresión
    formato = f"{{:<{anchoID}}}  {{:<{anchoNombre}}}  {{:<{anchoCorreo}}}  {{:<{anchoTel}}}  {{:<{anchoExentos}}}"

    # Imprimir encabezado
    print(formato.format(*headers))
    print("-" * (anchoID + anchoNombre + anchoCorreo + anchoTel + anchoExentos + 10))

    # Imprimir filas con "Sí"/"No"
    for est in datos.estudiantes:
        exentos = "Sí" if est[4] else "No"
        print(formato.format(str(est[0]), est[1], est[2], est[3], exentos))
        totalEstudiantes+=1
    
    print("-"*90)
    print("estudiantes inscritos:",totalEstudiantes)
    
    resp=input("Presione enter para volver al menu:").upper()
    if resp == "":
       utilerias.llamarMenu()
       
