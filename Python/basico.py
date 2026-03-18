habitaciones = {
    101: {"ocupada": False, "huésped": ""},
    102: {"ocupada": False, "huésped": ""},
    103: {"ocupada": False, "huésped": ""},
    # Agrega más habitaciones según sea necesario
}

def mostrar_disponibilidad():
    print("\nEstado de las habitaciones:")
    for num_habitacion, info_habitacion in habitaciones.items():
        estado = "Ocupada" if info_habitacion["ocupada"] else "Libre"
        huésped = info_habitacion["huésped"]
        print(f"Habitación {num_habitacion}: {estado} - Huésped: {huésped}")

def reservar_habitacion(num_habitacion, nombre_huesped):
    if num_habitacion in habitaciones:
        if habitaciones[num_habitacion]["ocupada"] == False:
            habitaciones[num_habitacion]["ocupada"] = True
            habitaciones[num_habitacion]["huésped"] = nombre_huesped
            print(f"Habitacion {num_habitacion} asignada a: {nombre_huesped} ")
            
        else: print(f"Habitacion {num_habitacion} ya ocupada")
    else: print(f"No existe habitacion {num_habitacion}")

def liberar_habitacion(num_habitacion):
    if num_habitacion in habitaciones:
        if habitaciones[num_habitacion]["ocupada"] == True:
            habitaciones[num_habitacion]["ocupada"]=False
            habitaciones[num_habitacion]["huésped"] = ""
            print(f"Habitacion {num_habitacion} ha sido desocupada")
            
        else: print(f"Habitacion {num_habitacion} ya estaba desocupada")

    else: print(f"No existe habitacion {num_habitacion}")

    pass

# Uso del programa
mostrar_disponibilidad()            

reservar_habitacion(102, "Juan Pérez")
reservar_habitacion(102, "Juan SSSS")


reservar_habitacion(105, "María Gómez")

mostrar_disponibilidad()

liberar_habitacion(102)
liberar_habitacion(102)

mostrar_disponibilidad()