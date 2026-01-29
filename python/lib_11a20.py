from math import sqrt

# prod_direcao: usada em p11
def prod_direcao(matriz_quadrada, i, j, n):
  result = 1
  direcoes = [[0, 1], [1, 0], [1, -1], [1, 1]]
  for vetor in direcoes:
    prod = 1
    limite_vertical = i+(n-1)*vetor[0]
    limite_horizontal = j+(n-1)*vetor[1]
    indice_maximo = len(matriz_quadrada)
    if (limite_horizontal >= 0 and limite_horizontal < indice_maximo and limite_vertical >= 0 and limite_vertical < indice_maximo):
      for k in range(n):
        prod *= matriz_quadrada[i+k*vetor[0]][j+k*vetor[1]]
      result = max(result, prod)
  return result

#crivo: usada em p12
def crivo(n):
  lista = [1] * (n + 1)
  lista[0] = 0
  lista[1] = 0
  for i in range(2, int(sqrt(n))):
    j = i*i
    while (j <= n):
      lista[j] = 0
      j += i
  return lista

#primos: usada em p12
def primos(n):
  lista = crivo(n)
  result = []
  for primo, i in enumerate(lista):
    if (i):
      result.append(primo)
  return result

#fatores: usada em p12
def fatores(n, primos):
  expoente = 0
  result = {}
  div = n
  for p in primos:
    expoente = 0
    while (div%p == 0):
      expoente += 1
      result[p] = expoente
      div /= p
    if div == 1:
      break
  if (div > 1):
    result[div] = 1
  return result

#num_divisores: usada em p12
def num_divisores(n, primos):
  result = 1
  primos = fatores(n, primos)
  for p in primos:
    result *= (primos[p] + 1)
  return result

#triangular: usada em p12
def triangular(n):
  return int((n*(n+1))/2)

# collatz: usada em p14
def collatz(n):
  colls = [0]
  for i in range(1, n+1):
    termo = i
    registro = 0
    while (termo != 1):
      if (termo < i):
        registro += colls[termo]
        break
      registro += 1
      if (termo%2 == 0):
        termo //= 2
      else:
        termo = 3*termo + 1
    if (termo == 1):
      registro += 1
    colls.append(registro)
  return colls

# fatorial: usada em p15
def fatorial(n):
  prod = 1
  for i in range(2, n+1):
    prod *= i
  return prod

# permut_repet: usada em p15
def permut_repet(n, lista):
  quociente = 1
  for p in lista:
    quociente *= fatorial(p)
  return fatorial(n) // quociente  