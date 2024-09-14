#convertir en fila transpolada:
#si tiene 4 filas 3 col, tiene que tener 3 filas y 4 col

#armar tateti


import random

def main():

  filas = int(input("ingrese las filas: "))
  columnas = int(input("ingrese las columnas: "))
  matriz = crear_matriz(filas, columnas)
  imprimir_matriz(matriz)
  print()
  ordenarFilas(matriz)
  print("")

  columna_a_invertir1 = int(input("ingrese la primera columna a invertir: ")) - 1
  columna_a_invertir2 = int(input("ingrese la segunda columna a invertir: ")) - 1

  matriz_columnas_invertidas = invertir_columnas(matriz, columna_a_invertir1, columna_a_invertir2)
  imprimir_matriz(matriz_columnas_invertidas)  


def crear_matriz(filas, columnas):
  matriz = []
  for i in range(filas):
    fila = []
    for j in range(columnas):
      numero = random.randint(1, 9)
      fila.append(numero)
    matriz.append(fila)
  return matriz



def invertir_columnas(matriz, columna1, columna2):
  
  matriz_nueva = matriz
  for fila in matriz_nueva:
    col1 = fila[columna1]
    col2 = fila[columna2]
    fila[columna1] = col2
    fila[columna2] = col1
  return matriz_nueva

def imprimir_matriz(matriz):
  for fila in matriz:
    print(fila)

def ordenarFilas(matriz):
  for fila in matriz:
    fila.sort()
    print(fila)



if __name__ == "__main__":
  main()