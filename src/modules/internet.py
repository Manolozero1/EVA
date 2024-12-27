import requests

class InternetManager:
    def __init__(self):
        self.search_url = "https://www.google.com/search?q="

    def search(self, query):
        try:
            print(f"Buscando en internet: {query}")
            response = requests.get(self.search_url + query)
            if response.status_code == 200:
                return "He encontrado resultados en internet. Por favor, revisa el navegador."  # Ajustar para procesar respuestas
            else:
                return "No pude realizar la búsqueda en este momento."
        except requests.RequestException as e:
            return f"Error al realizar la búsqueda: {e}"