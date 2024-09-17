import scripts.banner as b
import scripts.abmAlumnos as a
import scripts.abmCursos as c
import scripts.abmInscripciones as i
import scripts.misregex as r
import os
import time
import scripts.colors as co



def showmenu():
    os.system("cls")
    b.bannerMenu()
    #print("\n# MENU #")
    print("1. Ver Cursos")
    print("2. Ver alumnos")
    print("3. Ver Inscripciones")
    print("4. Salir")
    opcion = input(f"{co.BOLD}\nSeleccione una opcion > {co.REG}")
    if r.esNumero(opcion):
        opcion = int(opcion)
        if opcion == 1:
            c.listarCursos()
        if opcion == 2:
            a.listarAlumnos()
        if opcion == 3:
            i.listarInscripciones()
        if opcion == 4:
            print("\nMuchas gracias por utilizar UAL OFFLINE")
            print("Cerrando Sistema...")
            time.sleep(2)
            os.system("cls")
            exit()
        else:
            print("Opcion incorrecta")
            input("presione enter para reintentar")
            showmenu()
    else:
        print("Opcion incorrecta")
        input("presione enter para reintentar")
        showmenu()

if __name__ == "__main__":
    showmenu()