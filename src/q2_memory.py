import json
import re
from collections import Counter
from typing import List, Tuple

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Devuelve los 10 emojis más usados en el archivo JSON de tweets.
    Este método está optimizado para el uso de memoria al procesar el archivo línea por línea.
    
    """

    # Patrón regex para encontrar emojis en el texto.
    emoji_pattern = re.compile(
        r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|[\U0001F900-\U0001F9FF]|[\u2600-\u2B55]'
    )

    # Inicializa un contador para los emojis.
    emoji_counter = Counter()
    
    try:
        # Abre el archivo JSON para leer línea por línea.
        with open(file_path, 'r', encoding='utf-8') as json_file:
            # Procesa cada línea (tweet) del archivo.
            for line in json_file:
                try:
                    # Convierte la línea JSON a un diccionario.
                    tweet = json.loads(line)
                    
                    # Verifica que el tweet contenga la clave 'content'.
                    if 'content' in tweet:
                        # Busca todos los emojis en el contenido del tweet.
                        emojis = emoji_pattern.findall(tweet["content"])
                        
                        # Actualiza el contador con los emojis encontrados.
                        emoji_counter.update(emojis)

                except (json.JSONDecodeError, KeyError):
                    # Ignora líneas que no se pueden decodificar como JSON o que no tienen la clave 'content'.
                    continue

        # Obtiene los 10 emojis más comunes y sus conteos.
        top_emojis = emoji_counter.most_common(10)
        
        # Retorna la lista de los 10 emojis más utilizados.
        return top_emojis

    except FileNotFoundError:
        # Maneja el caso en que el archivo no se encuentra.
        print(f"Error: El archivo '{file_path}' no se encuentra.")
        return []


# Ejemplo de uso
file_path = "farmers-protest-tweets-2021-2-4.json"  # Especifica la ruta del archivo JSON
result = q2_memory(file_path)  # Llama a la función
print(result)  # Imprime el resultado

