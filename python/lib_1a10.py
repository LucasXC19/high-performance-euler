from math import sqrt

# soma_multiplos: usado em P1
def soma_multiplos(n, sup):
  quantidade_multiplos = (sup - 1) // n
  maior_multiplo = n * quantidade_multiplos
  return int((n + maior_multiplo) * quantidade_multiplos / 2)

# soma_fib_par: usado em P2
def soma_fib_par(sup):
  fib_par_menos1 = 1
  fib_par = 2
  fib_par_mais1 = 3
  soma = 0
  while fib_par <= sup:
    soma += fib_par
    fib_par_menos1 = fib_par + fib_par_mais1
    fib_par = fib_par_mais1 + fib_par_menos1
    fib_par_mais1 = fib_par_menos1 + fib_par
  return soma

# fatores: usado em P3
def fatores(n):
  result = []
  div = n
  p = 2
  while (div != 1):
    while (div%p == 0):
      result.append(p)
      div /= p
    p += 1
  return result

# maior_pali: usado em P4
def maior_pali(inf, sup):
  prod = 1
  result = 1
  for i in range(inf, sup):
    for j in range(i, sup):
      prod = i*j
      if (str(prod) == str(prod)[::-1]):
        result = max(prod, result)
  return result

# mmc_1n: usado em P5
def mmc_1n(primos, sup):
  prod = 1
  pot = 1
  for p in primos:
    while (pot*p <= sup):
      pot *= p
    prod *= pot
    pot = 1
  return prod

# soma_dos_quadrados: usado em P6
def soma_dos_quadrados(n):
  soma = 0
  for i in range(n+1):
    soma += i*i
  return soma

# quadrado_da_soma: usado em P6
def quadrado_da_soma(n):
  return int((n*(n+1)/2)**2)

# crivo: usado em P7 e P10
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

# primos: usado em P7 e P10
def primos(n):
  lista = crivo(n)
  result = []
  for i in range(len(lista)):
    if (lista[i]):
      result.append(i)
  return result

# maior_prod: usado em P8
def maior_prod(n, arq):
  prod = 1
  digitos = ""
  for linha in arq.readlines():
    digitos += linha.replace("\n", "")
  for i in range(len(digitos) - n + 1):
    prod_aux = 1
    if (digitos[i: i+n].count("0") > 0):
      continue
    for j in digitos[i: i+n]:
      prod_aux *= int(j)
    prod = max(prod, prod_aux)
  return prod

# produto_pitagorico: usado em P9
def produto_pitagorico(soma):
  result = 0
  for a in range(int(soma/3)):
    if result:
      break
    for b in range(int(soma/2)):
      c = soma - a - b
      if (a**2 + b**2 == c**2):
        result = a*b*c
        break
  return result