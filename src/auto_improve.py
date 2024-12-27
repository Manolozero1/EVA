import subprocess
import os

class AutoImprover:
    def __init__(self):
        self.source_code_path = "src/"

    def improve_self(self):
        print("Analizando y mejorando el código...")
        self.run_static_analysis()
        return "He analizado y mejorado mi propio código."

    def run_static_analysis(self):
        try:
            subprocess.run(["black", self.source_code_path], check=True)  # Formatea el código
            subprocess.run(["flake8", self.source_code_path], check=True)  # Verifica problemas de calidad
            print("Análisis estático y formato completados.")
        except subprocess.CalledProcessError as e:
            print(f"Error durante el análisis estático: {e}")