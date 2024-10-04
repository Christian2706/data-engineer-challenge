import json
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def process_tweet_time(line: str) -> defaultdict:
    """
    Procesa un tweet para extraer menciones de usuarios.

    """
    local_counter = defaultdict(int)  # Usar un diccionario simple
    try:
        tweet = json.loads(line)
        user = tweet.get("user", {}).get("username")
        content = tweet.get("content", "")

        if user:
            local_counter[user] += 1  # Incrementa el conteo para el usuario

            # Extrae menciones de otros usuarios en el contenido
            mentions = re.findall(r'@(\w+)', content)
            for mention in mentions:
                local_counter[mention] += 1  # Incrementa el conteo para cada mención
    except json.JSONDecodeError:
        pass  # Ignora líneas que no se pueden decodificar como JSON

    return local_counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Analiza un archivo de tweets y cuenta las menciones de usuarios.

    """
    total_counter = defaultdict(int)  # Contador global

    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            with ThreadPoolExecutor() as executor:
                # Procesa cada línea del archivo de forma concurrente
                results = executor.map(process_tweet_time, json_file)

                # Suma los contadores locales al contador total
                for local_counter in results:
                    for user, count in local_counter.items():
                        total_counter[user] += count

        # Obtiene las 10 menciones más comunes
        return sorted(total_counter.items(), key=lambda x: x[1], reverse=True)[:10]

    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encuentra.")
        return []


# Ejemplo de uso
file_path = "farmers-protest-tweets-2021-2-4.json"  # Especifica la ruta del archivo JSON
result = q3_time(file_path)  # Llama a la función
print(result)  # Imprime el resultado

