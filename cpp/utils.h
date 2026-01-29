#pragma once
using ll = long long;

// soma_multiplos: usada em p001
inline ll soma_multiplos(ll n, ll sup){
  ll quantidade_multiplos = (sup - 1) / n;
  ll maior_multiplo = n * quantidade_multiplos;
  return (n + maior_multiplo) * quantidade_multiplos / 2;
}