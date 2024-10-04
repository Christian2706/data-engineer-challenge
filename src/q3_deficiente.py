import json
import re
from collections import defaultdict
from typing import List, Tuple

def process_tweet(line: str, mention_counter: defaultdict) -> None:
    """
    Procesa un tweet para extraer menciones de usuarios de manera ineficiente.

    """
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
        mentions = re.findall(r'@(\w+)', content)

        # Incrementar el contador de menciones por cada usuario mencionado
        for mention in mentions:
            # Incrementa el contador de menciones para cada mención
            mention_counter[mention] += 1

def q3_deficiente(file_path: str) -> List[Tuple[str, int]]:
    """
    Analiza un archivo de tweets y cuenta las menciones de usuarios de manera ineficiente.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas con el nombre de usuario y el conteo
        de menciones, ordenados de mayor a menor.
    
    Este método abre el archivo, procesa cada tweet y retorna las 10 menciones más comunes.
    """
    # Inicializar un contador de menciones
    mention_counter = defaultdict(int)

    # Abrir el archivo JSON y procesar línea por línea
    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            process_tweet(line, mention_counter)  # Procesar cada línea

    # Ordenar los usuarios por el conteo de menciones de forma descendente
    sorted_mentions = sorted(mention_counter.items(), key=lambda x: x[1], reverse=True)

    # Devolver las 10 menciones más comunes
    return sorted_mentions[:10]

# Ejemplo de uso
file_path = "farmers-protest-tweets-2021-2-4.json"  # Especifica la ruta del archivo JSON
result = q3_deficiente(file_path)  # Llama a la función
print(result)  # Imprime el resultado
