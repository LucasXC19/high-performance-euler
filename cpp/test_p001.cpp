#include <iostream>
#include <cassert>
#include "utils.h"

using namespace std;

int main() {
    cout << "--------------------------------------" << endl;
    cout << "🧪 TEST SUITE: Problem 001" << endl;
    cout << "--------------------------------------" << endl;

    // Teste 1: Exemplo do Enunciado (Abaixo de 10)
    // 3, 5, 6, 9 -> Soma = 23
    ll resultado_exemplo = soma_multiplos(3, 10) + soma_multiplos(5, 10) - soma_multiplos(15, 10);
    assert(resultado_exemplo == 23);
    cout << "✅ [PASS] Exemplo do Enunciado (Limit 10) = 23" << endl;

    // Teste 2: Exemplo Menor (Abaixo de 6)
    // 3, 5 -> Soma = 8
    ll resultado_pequeno = soma_multiplos(3, 6) + soma_multiplos(5, 6) - soma_multiplos(15, 6);
    assert(resultado_pequeno == 8);
    cout << "✅ [PASS] Limite Pequeno (Limit 6) = 8" << endl;

    // Teste 3: Limite Exato (Abaixo de 5)
    // Apenas 3 -> Soma = 3 (O 5 não entra pois é "below 5")
    ll resultado_limite = soma_multiplos(3, 5) + soma_multiplos(5, 5) - soma_multiplos(15, 5);
    assert(resultado_limite == 3);
    cout << "✅ [PASS] Limite Exato (Limit 5) = 3" << endl;

    cout << "\n🎉 SUCESSO! A lógica matemática está perfeita." << endl;
    return 0;
}
