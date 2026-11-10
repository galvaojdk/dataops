# run_pipeline.py

import sys
import subprocess

def run_pipeline():
    print("🚀 Iniciando execução do pipeline...")

    python = sys.executable
    subprocess.run([python, "scripts/01_ingestao.py"], check=True)
    subprocess.run([python, "scripts/02_transformacao.py"], check=True)
    subprocess.run([python, "scripts/03_carga.py"], check=True)
    subprocess.run([python, "scripts/04_consumo.py"], check=True)

    print("🏁 Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()