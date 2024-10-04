import json
import re
from collections import Counter
from typing import List, Tuple

def process_tweet_memory(line: str, mention_counter: Counter) -> None:
    """
    Procesa un tweet para extraer menciones de usuarios.

    """
    try:
        # Cargar el tweet desde la línea JSON
        tweet = json.loads(line)
        # Obtener el nombre de usuario del autor
        user = tweet.get("user", {}).get("username")
        # Obtener el contenido del tweet
        content = tweet.get("content", "")

        if user:
            # Incrementar el contador para el autor del tweet
            mention_counter[user] += 1
            # Extraer menciones de otros usuarios en el contenido del tweet
            mention_counter.update(re.findall(r'@(\w+)', content))
    except json.JSONDecodeError as e:
        # Imprimir un mensaje de error si hay un problema con el formato JSON
        print(f"Error de JSON: {e}")

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Analiza un archivo de tweets y cuenta las menciones de usuarios.

    """
    mention_counter = Counter()  # Contador de menciones

    try:
        # Abrir el archivo JSON para leer línea por línea
        with open(file_path, 'r', encoding='utf-8') as json_file:
            for line in json_file:
                # Procesar cada línea y actualizar el contador
                process_tweet_memory(line, mention_counter)

        # Devolver las 10 menciones más comunes
        return mention_counter.most_common(10)

    except FileNotFoundError:
        # Imprimir un mensaje de error si el archivo no se encuentra
        print(f"Error: El archivo '{file_path}' no se encuentra.")
        return []



# Ejemplo de uso
file_path = "farmers-protest-tweets-2021-2-4.json"  # Especifica la ruta del archivo JSON
result = q3_memory(file_path)  # Llama a la función
print(result)  # Imprime el resultado
