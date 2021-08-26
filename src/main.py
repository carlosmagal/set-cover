import numpy as np
# n(linhas) vai ser o numero de pontos
# m(colunas) vai ser o numero de subconjs
# Ci é o peso do subconj i
def getInput():
  n, m = map(int, input().split())
  c = np.array([input().strip().split()], int)#pegando o c
  matrix = np.array([input().strip().split() for _ in range(n)], int)#matriz

  return n, m,  matrix, c

def main():

	n, m , matrix, c = getInput()
	
main()