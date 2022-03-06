from db import obtenerProvincias, obtenerVacunas, registrarProvincia, registrarVacuna, tabla_provincia, tabla_marca_vacuna

provincias = obtenerProvincias()
vacunas = obtenerVacunas()

def configurar():
    opcion = input("Configurar provincias o marcas de vacunas:\n 1- Provincias\n 2- Marcas de vacunas\n")
    
    if opcion == "1":
        configurarProvincias()
    elif opcion == "2":
        configurarMarcasVacunas()

def configurarProvincias():
    provincia = input("Ingrese el nombre de la provincia: ")

    if tabla_provincia.getBy({ "provincia": provincia }):
        print("Esta provincia ya existe.")
    else:
        registrarProvincia(provincia)
        print("Provincia registrada exitosamente.")


def configurarMarcasVacunas():
    vacuna = input("Ingrese el nombre de la vacuna: ")
    if tabla_marca_vacuna.getBy({ "vacuna": vacuna }):
        print("Esta vacuna ya existe.")
    else:
        registrarVacuna(vacuna)
        print("Vacuna registrada exitosamente.")