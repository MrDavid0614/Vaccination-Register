# Aplicacion para registrar las personas que se vacunan
# con por el covid, la aplicacion sera usada para registrar
# las personas que son vacunadas en varias dosis.
from db import registrarVacunado
from exportarHTML import exportarAHTML
from configurar import configurar
from os import system
from time import sleep

menu_principal = """
----- Menu Principal -------
1- Registrar vacunado.
2- Exportar a HTML.
3- Configurar Provincias o Marcas de vacunas.
4- Salir.
"""

while True:
    system("cls")
    print(menu_principal)
    opcion = input("Elija su opción: ")

    if opcion == "1":
        registrarVacunado()

    elif opcion == "2":
        exportarAHTML()

    elif opcion == "3":
        configurar()

    elif opcion == "4":
        break

    else:
        system("cls")
        print("Opción no válida...")
    
    sleep(1)
    system("cls")

    print("¿Quieres salir o volver al menú?\n 1- Volver al menú.\n 2- Salir.")
    opcionFinal = input("\nElija su opción: ")

    if opcionFinal == "2":
        break