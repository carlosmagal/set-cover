import numpy as np

def getInput():
  
  n, m = map(int, input().split())
  c = np.array([input().strip().split()], int)
  matriz = np.array([input().strip().split() for _ in range(n)], int)

  return n, m, matriz, c

def main():

  n, m , matriz, c = getInput()

  pesos = c[0]
  pontos = np.zeros(n, int)
  sc = np.zeros(m, int)

  menor = 1000000
  indexMenor = -1
  estaCoberto = False

  for i in range(n):
    for j in range(m):

      if matriz[i][j] == 1:
        if sc[j] == 1:
          estaCoberto = True
        elif sc[j] == 0 and pesos[j] < menor:
          indexMenor = j
          menor = pesos[j]

    else:
      if not estaCoberto:
        for k in range(m):
          if matriz[i][k] == 1:
            pesos[k] -= menor
      
        sc[indexMenor] = 1 # colocando subconj na solucao
        pontos[i] = menor # peso

      menor = 1000000
      indexMenor = -1
      estaCoberto = False

  print()
  print(*sc)
  print(*pontos)

main()