Datos_Basicos = {"Nombres": "Juan Carlos",
                 "Apellidos": "Pérez García",
                 "DUI": "354350304-4",
                 "Fecha_Nacimiento": "23/07/1980",
                 "Lugar_Nacimiento": "Soya City",
                 "Nacionalidad": "Salvadoreña",
                 "Estado Civil": "Complicado"
                 }

print("\nDetalle del Diccionario")
print("=================================")

print("\n Claves del diccionario:", Datos_Basicos.keys())
print("\n Valores del diccionario:", Datos_Basicos.values())
print("\n Elementos del diccionario:", Datos_Basicos.items())


print("\nInscripción del curso")
print("==================================")


print("\nDatos del participante")
print("==================================")

print("DUI:", Datos_Basicos["DUI"])
print("Nombre Completo:", Datos_Basicos["Nombres"]+" "+Datos_Basicos["Apellidos"])