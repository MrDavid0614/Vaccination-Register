from os import system
from time import sleep
from pysondb import db
from datetime import date
from vacunado import Vacunado
from msvcrt import getch

tabla_vacunado = db.getDb("vacunado.json")
tabla_provincia = db.getDb("provincia.json")
tabla_marca_vacuna = db.getDb("vacuna.json")

def obtenerVacunados():
    return tabla_vacunado.getAll()

def obtenerVacunas():
    return tabla_marca_vacuna.getAll()

def obtenerProvincias():
    return tabla_provincia.getAll()

def registrarProvincia(provincia):
    tabla_provincia.add({ "provincia": provincia })

def registrarVacuna(vacuna):
    tabla_marca_vacuna.add({ "vacuna": vacuna })

def registrarVacunado():
    provincias = obtenerProvincias()
    vacunas = obtenerVacunas()

    system("cls")

    if len(provincias) != 0 and len(vacunas) != 0:
        cedula = input("Ingrese su cédula: ")
        if len(tabla_vacunado.getBy({ "cedula": cedula })) == 0:
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            telefono = input("Ingrese su telefono: ")
            fechaNacimiento = input("Ingrese su fecha de nacimiento: ")

            system("cls")

            print("Vacunas registradas:\n")
            for i in range(len(vacunas)):
                vacuna = vacunas[i]["vacuna"]
                print(f"{ i + 1 }- { vacuna }")

            print()
            tipoVacuna = vacunas[ int(input("Ingrese su tipo de vacuna: ")) - 1 ]["vacuna"]

            print("Provincias registradas:\n")
            for i in range(len(provincias)):
                provincia = provincias[i]["provincia"]
                print(f"{ i + 1 }- { provincia }")

            print()
            provincia = provincias[ int(input("Ingrese su provincia: ")) - 1 ]["provincia"]
            dosisFecha = input("Ingrese la fecha en que se inyectó la dosis: ")
            dosis = [{ "tipoVacuna": tipoVacuna, "fecha": dosisFecha }]
            fechaRegistro = date.today().strftime("%d-%m-%Y")

            vacunado = Vacunado(cedula, nombre, apellido, telefono, fechaNacimiento, dosis, provincia, fechaRegistro)

            tabla_vacunado.add(vacunado.__dict__)

            print("La persona vacunada ha sido registrada exitosamente.")
            sleep(1)
        else:
            print("Esta persona ya está registrada.\n")
            print("Vacunas registradas:\n")
            for i in range(len(vacunas)):
                vacuna = vacunas[i]["vacuna"]
                print(f"{ i + 1 }- { vacuna }")
            
            print()
            tipoVacuna = vacunas[ int(input("Ingrese su tipo de vacuna: ")) - 1 ]["vacuna"]
            dosisFecha = input("Ingrese la fecha en que se inyectó la nueva dosis: ")

            vacunado = tabla_vacunado.getBy({ "cedula": cedula })[0]
            vacunado["dosis"].append({ "tipoVacuna": tipoVacuna, "fecha": dosisFecha })
            tabla_vacunado.updateByQuery({ "cedula": cedula }, vacunado)
            print(f"\nNueva dosis registrada para el vacunado: { cedula } ")

    else:
        print("\nNo hay ninguna provincia o vacuna registrada, debe verificar la lista de provincias y vacunas antes de continuar.")
        getch()