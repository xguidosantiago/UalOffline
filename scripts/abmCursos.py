import scripts.banner as b
import scripts.mainmenu as m
import os
import json
import scripts.colors as co

base_path = os.path.dirname(os.path.abspath(__file__))
path_Cursos = os.path.join(base_path, '..', 'db', 'cursos.json')


def listarCursos():
    b.bannerCursos()
    if os.path.exists(path_Cursos):
        with open(path_Cursos, "r") as js:
                Cursos = json.load(js)
                if len(Cursos) == 0:
                    print("\nNo hay Cursos cargados.")
                else:
                    print(f"{co.BOLD}\nCursos Cargados:{co.REG}")
                    
                    #print("-------------------")
                    for Curso in Cursos:
                        if Curso["eliminado"] == 0:
                            print(f"id:{Curso["id"]}, nombre: {Curso["nombre"]}, fecha de Inicio: {Curso["fechaInicio"]}, fecha de Finalizacion: {Curso["fechaFin"]}")
                    #print("-------------------")
    else:
         print("\nNo hay Cursos cargados.")

    print("\n1. Alta de Curso")
    print("2. Modificar Curso")
    print("3. Eliminar Curso")
    print("4. Volver")
    opcionCurso = int(input("\nSeleccione una opcion >  "))
    if opcionCurso == 1:
            cargarCurso()
    elif opcionCurso == 2:
         modificarCurso()
    elif opcionCurso == 3:
         eliminarCurso()
    elif opcionCurso == 4:
         m.showmenu()

def cargarCurso():
    lstCursos = []
    if os.path.exists(path_Cursos):
        with open(path_Cursos, "r") as js:
            lstCursos.extend(json.load(js))
                                  
    pNombre = input("\nnombre: ")
    pFechainicio = input("fecha de inicio (formato dd-mm-yy): ")
    pFechaFin = input("Fecha de finalizacion (formato dd-mm-yy): ")

    if len(lstCursos) == 0:
         proximoId = 1
    else:
        ultimoCurso = lstCursos[-1]
        proximoId = int(ultimoCurso["id"])+1

    Curso={"id": proximoId,
            "nombre": pNombre,
            "fechaInicio":pFechainicio,
            "fechaFin":pFechaFin,
            "eliminado":0
            }
    
    lstCursos.append(Curso)
    with open(path_Cursos, "w") as js:
        json.dump(lstCursos, js, indent=4)
    print(f"{co.BOLD}\nEl Curso se cargó correctamente.{co.REG}")
    goback = input("presione enter para continuar")
    goback = listarCursos()

def eliminarCurso():
    lstCursos = []
    flag = 0
    if os.path.exists(path_Cursos):
        with open(path_Cursos, "r") as js:
                lstCursos = json.load(js)
        idCurso = int(input("\nIngresar ID de Curso a Eliminar (presione 0 para cancelar) > "))

        if idCurso == 0:
            m.showmenu()
        else:
            print(idCurso)
            for Curso in lstCursos:
                if Curso["id"] == idCurso:
                    Curso["eliminado"] = 1
                    flag = 1
                
            if flag == 1:
                with open(path_Cursos, "w") as js:
                    json.dump(lstCursos, js, indent=4)
                print(f"{co.BOLD}\nEl Curso con ID {idCurso} se eliminó exitosamente{co.REG}")
                goback = input("presione enter para continuar")
                goback = listarCursos()
            else:
                print(f"{co.BOLD}El Curso con ID {idCurso} no fue encontrado{co.REG}")
                eliminarCurso()
    else:
         print(f"{co.BOLD}\nNo hay Cursos cargados.{co.REG}")
         goback = input("presione enter para continuar")
         goback = listarCursos()

def modificarCurso():
     lstCursos = []
     if os.path.exists(path_Cursos):
        with open(path_Cursos, "r") as js:
                lstCursos = json.load(js)
        idCurso = int(input("\nIngresar ID de Curso a Modificar (presione 0 para cancelar) > "))
        if idCurso == 0:
            m.showmenu()
        else:
            for Curso in lstCursos:
                if Curso["id"] == idCurso:
                    lstCursos.remove(Curso)
                    pNombre = input("\nnombre: ") 
                    fechaInicio = input("Fecha de inicio: ")
                    fechaFin = input("fecha de fin: ")

                    Curso={"id": idCurso,
                            "nombre": pNombre,
                            "fechaInicio":fechaInicio,
                            "fechaFin":fechaFin,
                            "eliminado":0
                            }
    
                    lstCursos.append(Curso)
                    with open(path_Cursos, "w") as js:
                        json.dump(lstCursos, js, indent=4)
                    print(f"{co.BOLD}\nEl Curso se modificó correctamente.{co.REG}")
                    goback = input("presione enter para continuar")
                    goback = listarCursos()
                    flag = 1
     else:
         print(f"{co.BOLD}\nNo hay Cursos cargados.{co.REG}")
         goback = input("presione enter para continuar")
         goback = listarCursos()

if __name__ == "__main__":
    listarCursos()
    eliminarCurso()
    modificarCurso()
    cargarCurso()
     