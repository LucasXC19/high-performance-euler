import subprocess
import time
import os
import sys

# Cores
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
RESET = "\033[0m"

def rodar(arquivo):
    # Compila, executa e DELETA o executável gerado.

    caminho_arquivo = "cpp/" + arquivo + ".cpp"
    if not os.path.exists(caminho_arquivo):
        print(f"{VERMELHO}❌ Erro: Arquivo '{caminho_arquivo}' não encontrado!{RESET}")
        return

    # Define nome do executável (sem extensão)
    executavel = os.path.splitext(caminho_arquivo)[0]

    try:
        # --- 1. COMPILAÇÃO ---
        cmd_compilacao = ["g++", "-O3", "-Wall", caminho_arquivo, "-o", executavel]
        proc_compilacao = subprocess.run(cmd_compilacao, capture_output=True, text=True)

        if proc_compilacao.returncode != 0:
            print(f"{VERMELHO}❌ FALHA NA COMPILAÇÃO:{RESET}")
            print("-" * 60)
            print(proc_compilacao.stderr)
            print("-" * 60)
            return

        # --- 2. EXECUÇÃO ---
        inicio = time.time()
        proc_execucao = subprocess.run([executavel], capture_output=True, text=True)
        fim = time.time()
        
        tempo_ms = (fim - inicio) * 1000

        # --- 3. EXIBIÇÃO ---
        if proc_execucao.returncode != 0:
            print(f"{VERMELHO}❌ ERRO DE EXECUÇÃO (Runtime Error):{RESET}")
            print(proc_execucao.stderr)
        else:
            print(f"{VERDE}✅ Sucesso!{RESET} | ⏱️ {tempo_ms:.4f} ms")
            if proc_execucao.stdout:
                print("--- SAÍDA ---")
                print(proc_execucao.stdout.strip())
                print("-------------")

    finally:
        # --- 4. LIMPEZA (Sempre roda, mesmo se der erro no meio) ---
        if os.path.exists(executavel):
            os.remove(executavel)
            # Se quiser ver que apagou, descomente a linha abaixo:
            # print(f"{AMARELO}🧹 Faxina: Executável removido.{RESET}")