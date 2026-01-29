#include <iostream>
#include "utils.h"

using namespace std;

int main(){
  cout << soma_multiplos(3, 1000) + soma_multiplos(5, 1000) - soma_multiplos(15, 1000) << endl;
  return 0;
}