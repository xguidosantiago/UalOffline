import scripts.banner as b
import scripts.mainmenu as m
import os
import json
import scripts.misregex as r
import scripts.abmInscripciones as i
import scripts.colors as co

base_path = os.path.dirname(os.path.abspath(__file__))
path_alumnos = os.path.join(base_path, '..', 'db', 'alumnos.json')
path_inscripciones = os.path.join(base_path, '..', 'db', 'inscripciones.json')


def listarAlumnos():
    b.bannerAlumnos()
    if os.path.exists(path_alumnos):
        with open(path_alumnos, "r") as js:
                alumnos = json.load(js)
                if len(alumnos) == 0:
                    print("\nNo hay alumnos cargados.")
                else:
                    print(f"{co.BOLD}Alumnos Actuales:{co.REG}")
                    #print("-------------------")
                    for alumno in alumnos:
                        print(f" dni: {alumno["dni"]}, nombre: {alumno["nombre"]}, apellido: {alumno["apellido"]}, fecha de nacimiento: {alumno["fechanac"]}, email: {alumno["email"]}")
                    #print("-------------------")
    else:
         print("\nNo hay alumnos cargados.")
                
    print(f"\n1. Alta de alumno")
    print(f"2. Modificar alumno")
    print(f"3. Eliminar alumno")
    print(f"4. Volver")
    opcionAlumno = input(f"{co.BOLD}\nSeleccione una opcion > {co.REG}")
    if r.esNumero(opcionAlumno):
        opcionAlumno = int(opcionAlumno)
        if opcionAlumno == 1:
                cargarAlumno()
        elif opcionAlumno == 2:
            modificarAlumno()
        elif opcionAlumno == 3:
                eliminarAlumno()
        elif opcionAlumno == 4:
                m.showmenu()
        else:
            print("la opcion seleccionada no es correcta")
            goback = input("presione enter para reintentar")
            goback = listarAlumnos()
    else:
        print("la opcion seleccionada no es correcta")
        goback = input("presione enter para reintentar")
        goback = listarAlumnos()

def cargarAlumno():
    flagDni = 0
    lstAlumnos = []
    if os.path.exists(path_alumnos):
        with open(path_alumnos, "r") as js:
                lstAlumnos.extend(json.load(js))
    pDni = input("dni: ")
    for pAlumno in lstAlumnos:
         if pDni == pAlumno["dni"]:
            flagDni = 1

    if flagDni == 1:
        print("el dni ingresado ya existe")
        input("presione enter para reintentar")
        cargarAlumno()
    else:
        pNombre = input("\nnombre: ") 
        pApellido = input("Apellido: ")
        pFechanac = input("Fecha de Nacimiento (formato: dd-mm-yy): ")
        pEmail = input("email: ")
        alumno={"dni": pDni,
                "nombre": pNombre,
                "apellido":pApellido,
                "fechanac":pFechanac,
                "email":pEmail}
        
        lstAlumnos.append(alumno)
        with open(path_alumnos, "w") as js:
            json.dump(lstAlumnos, js, indent=4)
        print("\nel alumno se cargó correctamente.")
        input("presione enter para continuar")
        listarAlumnos()

            
def eliminarAlumno():
    lstAlumnos = []
    lstInscripciones = []
    flag = 0
    with open(path_inscripciones, "r") as jsi:
         lstInscripciones = json.load(jsi)

    if os.path.exists(path_alumnos):
        with open(path_alumnos, "r") as js:
                lstAlumnos = json.load(js)
        dni = input("\nIngresar DNI de alumno a Eliminar (presione 0 para cancelar) > ")
        if r.esNumero(dni):
            if dni == "0":
                m.showmenu()
            else:
                for inscripcion in lstInscripciones:
                    for alumno in lstAlumnos:
                        if dni == inscripcion["idAlumno"]:
                             print("el alumno no se puede eliminar ya que se encuentra inscripto a un curso")
                             input("ingrese enter para reintentar")
                             eliminarAlumno()
                        elif alumno["dni"] == dni:
                            lstAlumnos.remove(alumno)
                            flag = 1
                    
                if flag == 1:
                    with open(path_alumnos, "w") as js:
                        json.dump(lstAlumnos, js, indent=4)
                    print(f"\nEl alumno con DNI {dni} se eliminó exitosamente")
                    goback = input("presione enter para continuar")
                    goback = m.showmenu()
                else:
                    print(f"El alumno con DNI {dni} no fue encontrado")
                    eliminarAlumno()
        else:
             print("el valor ingresado es incorrecto")
             input("ingrese enter para reintentar")
             eliminarAlumno()
             

def modificarAlumno():
     mdFlag = 0
     lstAlumnos = []
     with open(path_alumnos, "r") as js:
            lstAlumnos = json.load(js)
     dni = input("\nIngresar DNI de alumno a Modificar (presione 0 para cancelar) > ")
     if r.esNumero(dni):
        if dni == "0":
            m.showmenu()
        elif dni != 0:
            for alumno in lstAlumnos:
                if alumno["dni"] == dni:
                    print("\nIngrese los datos a modificar (presione enter para mantener los anteriores):")
                    pNombre = input(f"\nnombre ({alumno["nombre"]}): ") or alumno["nombre"]
                    pApellido = input(f"Apellido ({alumno["apellido"]}): ") or alumno["apellido"]
                    pFechanac = input(f"Fecha de Nacimiento ({alumno["fechanac"]}): ") or alumno["fechanac"]
                    pEmail = input(f"email({alumno["email"]}):") or alumno["email"]
                    lstAlumnos.remove(alumno)

                    alumno={"dni": dni,
                            "nombre": pNombre,
                            "apellido":pApellido,
                            "fechanac":pFechanac,
                            "email":pEmail}
                    
                    lstAlumnos.append(alumno)
                    with open(path_alumnos, "w") as js:
                        json.dump(lstAlumnos, js, indent=4)
                    print("\nel alumno se modificó correctamente.")
                    goback = input("presione enter para continuar")
                    goback = listarAlumnos()
                    mdFlag = 0
                else:
                    mdFlag = 1
            
            if mdFlag == 1:
                 print("El valor ingresado es incorrecto")
                 input("ingrese enter para reintentar")
                 modificarAlumno()
     else:
            print("El valor ingresado es incorrecto")
            input("ingrese enter para reintentar")
            modificarAlumno()


if __name__ == "__main__":
    listarAlumnos()
    eliminarAlumno()
    modificarAlumno()
    cargarAlumno()
     