import csv
import os

print("\n" + "=" * 50)
print("Sistema de Agenda de Contactos")
print("=" * 50)

# 0 Crear Archivos si no existen
# contactos.csv
if not os.path.exists("contactos.csv"):
    print(f"\n Creando archivo contactos.csv")
    with open("contactos.csv","w",newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre','Telefono','Correo','Direccion'])
    print("Archivo: contactos.csv creado")

# 1 Cargar contactos desde el archivo CSV
# Crear Listas vacias
contactos = []

with open("contactos.csv","r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        contactos.append({
            "Nombre":fila["Nombre"].strip(),
            "Telefono":fila["Telefono"].strip(),
            "Correo":fila["Correo"].strip(),
            "Direccion":fila["Direccion"].strip()
        })
print(f"{len(contactos)} contactos cargados desde el csv")

# 2 Bucle Principal del Sistema
while True:
    print("\n" + "-" * 50)
    print("Menú de Opciones")
    print("-" * 50)
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("-" * 50)
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        print("\n" + "*" * 30)
        print("Agregar Nuevo Contacto")
        print("*" * 30)
        
        nombre = input("Ingrese Nombre: ").strip()
        telefono = input("Ingrese Teléfono: ").strip()
        correo = input("Ingrese Correo: ").strip()
        direccion = input("Ingrese Dirección: ").strip()
        
        contactos.append({
            "Nombre": nombre,
            "Telefono": telefono,
            "Correo": correo,
            "Direccion": direccion
        })
        
        with open("contactos.csv", "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, telefono, correo, direccion])
            
        print("\n>> Contacto guardado exitosamente.")
        
    elif opcion == '2':
        print("\n" + "*" * 30)
        print("Lista de Contactos")
        print("*" * 30)
        
        if len(contactos) == 0:
            print("No hay contactos registrados.")
        else:
            for i, c in enumerate(contactos, 1):
                print(f"{i}. Nombre: {c['Nombre']}")
                print(f"   Teléfono: {c['Telefono']}")
                print(f"   Correo: {c['Correo']}")
                print(f"   Dirección: {c['Direccion']}")
                print("   " + "-" * 20)
                
    elif opcion == '3':
        print("\n" + "*" * 30)
        print("Actualizar Contacto")
        print("*" * 30)
        
        if len(contactos) == 0:
            print("No hay contactos para actualizar.")
        else:
            for i, c in enumerate(contactos, 1):
                print(f"{i}. {c['Nombre']} - {c['Telefono']}")
                
            try:
                indice = int(input("\nSeleccione el número del contacto a modificar: "))
                if 1 <= indice <= len(contactos):
                    idx = indice - 1
                    print("\n(Deje el espacio en blanco y presione Enter si no desea modificar el campo)")
                    
                    nuevo_nombre = input(f"Nombre actual ({contactos[idx]['Nombre']}): ").strip()
                    nuevo_telefono = input(f"Teléfono actual ({contactos[idx]['Telefono']}): ").strip()
                    nuevo_correo = input(f"Correo actual ({contactos[idx]['Correo']}): ").strip()
                    nueva_direccion = input(f"Dirección actual ({contactos[idx]['Direccion']}): ").strip()
                    
                    if nuevo_nombre: contactos[idx]['Nombre'] = nuevo_nombre
                    if nuevo_telefono: contactos[idx]['Telefono'] = nuevo_telefono
                    if nuevo_correo: contactos[idx]['Correo'] = nuevo_correo
                    if nueva_direccion: contactos[idx]['Direccion'] = nueva_direccion
                    
                    with open("contactos.csv", "w", newline="", encoding="utf-8") as archivo:
                        escritor = csv.DictWriter(archivo, fieldnames=['Nombre', 'Telefono', 'Correo', 'Direccion'])
                        escritor.writeheader()
                        escritor.writerows(contactos)
                        
                    print("\n>> Contacto actualizado correctamente.")
                else:
                    print("\n>> Opción inválida. Seleccione un número de la lista.")
            except ValueError:
                print("\n>> Error: Por favor ingrese un valor numérico.")
                
    elif opcion == '4':
        print("\n" + "*" * 30)
        print("Eliminar Contacto")
        print("*" * 30)
        
        if len(contactos) == 0:
            print("No hay contactos para eliminar.")
        else:
            for i, c in enumerate(contactos, 1):
                print(f"{i}. {c['Nombre']} - {c['Telefono']}")
                
            try:
                indice = int(input("\nSeleccione el número del contacto a eliminar: "))
                if 1 <= indice <= len(contactos):
                    idx = indice - 1
                    contacto_eliminado = contactos.pop(idx)
                    
                    with open("contactos.csv", "w", newline="", encoding="utf-8") as archivo:
                        escritor = csv.DictWriter(archivo, fieldnames=['Nombre', 'Telefono', 'Correo', 'Direccion'])
                        escritor.writeheader()
                        escritor.writerows(contactos)
                        
                    print(f"\n>> El contacto '{contacto_eliminado['Nombre']}' ha sido borrado.")
                else:
                    print("\n>> Opción inválida. Seleccione un número de la lista.")
            except ValueError:
                print("\n>> Error: Por favor ingrese un valor numérico.")
                
    elif opcion == '5':
        print("\nCerrando el sistema de agenda...")
        break
        
    else:
        print("\n>> Opción no reconocida. Intente con un número del 1 al 5.")