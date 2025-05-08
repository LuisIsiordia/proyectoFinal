import talleres

print("1.Agregar un nuevo taller al catalogo\n",
      "2.Dar de baja un taller del catalogo\n",
      "3.Actualizar los datos de un taller\n",
      "4.Mostrar el listado de talleres en el catalogo\n",
      "5.Registrar una inscripción por folio\n",
      "6.Cancelar una inscripción por folio\n",
      "7.Mostrar el listado de inscripciones por taller\n",
      "8.Mostrar los estudiantes vigentes\n",
      "9.Terminar operacion\n")
resp=input("Teclee su opción: ")

if resp=='1':
    print(talleres.agregarTalleres)
elif resp=='2':
    print("2")
elif resp=='3':        
    print("3")
elif resp=='4':
    print("4")
elif resp=='5':
    print("5")
elif resp=='6':
    print("6")
elif resp=='7':
    print("7")
elif resp=='8':
    print("8")
elif resp=='9':
    print("fin")
