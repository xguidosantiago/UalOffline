import scripts.banner as b
import scripts.mainmenu as m
import scripts.colors as co
import os
import sys
import json
import time

base_path = os.path.dirname(os.path.abspath(__file__))
path_Cursos = os.path.join(base_path, '..', 'db', 'cursos.json')
path_alumnos = os.path.join(base_path, '..', 'db', 'alumnos.json')
path_inscripciones = os.path.join(base_path, '..', 'db', 'inscripciones.json')

def listarInscripciones():
    totalAlumnos = 0
    flagEliminado = 0
    flagCurso = 0
    Cursos = []
    b.bannerInsc()

    if os.path.exists(path_inscripciones):
        with open(path_inscripciones, "r") as jsi:
            inscripciones = json.load(jsi)

            print(f"{co.BOLD}\nListado de cursos:{co.REG}")
            
            if os.path.exists(path_Cursos):
                with open(path_Cursos, "r") as jsc:
                    Cursos = json.load(jsc)

                    for curso in Cursos:
                        if curso["eliminado"] == 0:
                            print(f" Id: {curso["id"]}, Curso: {curso["nombre"]}")
                codCurso = input("\nseleccionar ID de curso para ver inscripciones (ingrese 0 para volver) > ")
                if codCurso == "0":
                    m.showmenu()

                with open(path_Cursos, "r") as jsc:
                    Cursos = json.load(jsc)
                    for curso in Cursos:  
                        if curso["eliminado"] == 0: 
                            if int(codCurso) == curso["id"]:
                                flagCurso = 1
                    if flagCurso == 1:
                         if os.path.exists(path_alumnos):
                                    with open(path_alumnos, "r") as jsa:
                                        alumnos = json.load(jsa)
                                        b.bannerInsc()
                                        print("Alumnos Inscriptos:")
                                        for inscripto in inscripciones:
                                            if inscripto["idCurso"] == str(codCurso):
                                                for alumno in alumnos:
                                                    if inscripto["idAlumno"] == alumno["dni"]:
                                                        print(f" #{totalAlumnos+1} dni: {alumno["dni"]}, nombre: {alumno["nombre"]}, apellido: {alumno["apellido"]}")
                                                        totalAlumnos +=1
                                        print(f"\ntotal alumnos: {totalAlumnos}")
                    else:  
                        print("no se encontró el curso") 
                        input("presione enter para reintentar")
                        listarInscripciones()    
                        
    else:
         print(f"\nNo hay inscripciones cargadas.")
         
    print("\n1. Inscribir alumno")
    print("2. Eliminar inscripcion")
    print("3. Volver")
    opcionInsc = int(input("\nSeleccione una opcion > "))
    if opcionInsc == 1:
            cargarInscripcion(codCurso)
    elif opcionInsc == 2:
            eliminarInscripcion(codCurso)
    elif opcionInsc == 3:
            listarInscripciones()

def cargarInscripcion(idcurso):
     b.bannerInsc()
     inscriptoFlag = 0
     lstInscripciones= []

     if os.path.exists(path_inscripciones):
          with open(path_inscripciones, "r") as jsi:
               lstInscripciones = json.load(jsi)

     if os.path.exists(path_alumnos):
        with open(path_alumnos, "r") as js:
                alumnos = json.load(js)
                
                if len(alumnos) == 0:
                    print(f"\nNo hay alumnos cargados.")
                    
                else:
                    print(f"\nAlumnos Disponibles:")
                    
                    print("-------------------")
                    for alumno in alumnos:
                        print(f" dni: {alumno["dni"]}, nombre: {alumno["nombre"]}, apellido: {alumno["apellido"]}, fecha de nacimiento: {alumno["fechanac"]}, email: {alumno["email"]}")
                    print("-------------------")
                    idAlumno = input ("Ingrese DNI de alumno (ingrese 0 para volver) > ")

                    inscripcion={"idCurso": idcurso,
                                "idAlumno": idAlumno}

        if int(idAlumno) == 0:
                listarInscripciones()
        else: 
                for inscripto in lstInscripciones:
                    if inscripto["idCurso"] == inscripcion["idCurso"]:
                        if inscripto["idAlumno"] == inscripcion["idAlumno"]:
                            inscriptoFlag = 1
                            
                if inscriptoFlag == 1:
                    print(f"El alumno ya se encuentra inscripto al curso")
                    
                    input("presione enter para continuar")
                    cargarInscripcion(idcurso) 

                else:
                    with open(path_alumnos, "r") as js:
                        alumnos = json.load(js)
                        flagDNI = 0
                        for alumno in alumnos:
                            if idAlumno == alumno["dni"]: 
                                flagDNI = 1 
                        if flagDNI == 1:
                            lstInscripciones.append(inscripcion)
                            with open(path_inscripciones, "w") as jsi:
                                    json.dump(lstInscripciones, jsi, indent=4)
                            print(f"\ninscripción realizada exitosamente")
                        else:
                            input("no se encontró alumno, intente nuevamente")
                            cargarInscripcion(idcurso)              
     else:
        print("\nNo hay alumnos cargados.")

#def modificarInscripcion(codCurso):

def eliminarInscripcion(codCurso):
     b.bannerInsc()
     lstInscripciones=[]
     eliminaFlag = 0

     if os.path.exists(path_inscripciones):
        with open(path_inscripciones, "r") as jsi:
            lstInscripciones = json.load(jsi)

     if os.path.exists(path_alumnos):
            with open(path_alumnos, "r") as jsa:
                alumnos = json.load(jsa)

     if len(lstInscripciones) == 0:
        print(f"no hay inscriptos al curso")
        
     else:
            for inscripto in lstInscripciones:
                if inscripto["idCurso"] == str(codCurso):
                    for alumno in alumnos:
                        if inscripto["idAlumno"] == alumno["dni"]:
                            print(f"dni: {alumno["dni"]}, nombre: {alumno["nombre"]}, apellido: {alumno["apellido"]}")

     eliminaDni = input ("\nSeleccione DNI de alumno a eliminar (Presione 0 para volver) > ")

     if eliminaDni == "0":
          listarInscripciones()
     else: 
        with open(path_inscripciones, "r") as jsi:
            lstInscripciones = json.load(jsi)

        for inscripto in lstInscripciones:
            if inscripto["idCurso"] == str(codCurso) and inscripto["idAlumno"] == eliminaDni:
                lstInscripciones.remove(inscripto)
                eliminaFlag = 1

        if eliminaFlag == 1:
            with open(path_inscripciones, "w") as js:
                json.dump(lstInscripciones, js, indent=4)
            print(f"\nSe eliminó al alumno con DNI {eliminaDni}")
            
            input("presione enter para continuar")
            goback =listarInscripciones()
        else:
            print(f"\nNo se encontró el alumno")
            
            input("presione enter para reintentar")
            eliminarInscripcion(codCurso)

               
          


        
    

                                
