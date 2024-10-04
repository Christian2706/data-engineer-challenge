import json
import re
from collections import Counter
from typing import List, Tuple

def q2_deficiente(file_path: str) -> List[Tuple[str, int]]:
    """
    Este método es deficiente porque carga todos los datos en memoria antes de procesarlos.
    Esto puede resultar en un uso elevado de memoria y un tiempo de ejecución más largo,
    especialmente con grandes volúmenes de datos.

    """

    # Patrón regex para encontrar emojis en el texto.
    emoji_pattern = re.compile(
        r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|[\U0001F900-\U0001F9FF]|[\u2600-\u2B55]'
    )

    # Carga todos los tweets en memoria (ineficiente)
    tweet_list = open(file_path, 'r', encoding='utf-8').readlines()
    
    # Inicializa un contador para los emojis.
    emoji_counter = Counter()

    # Procesa cada línea (tweet) del archivo.
    for line in tweet_list:
        try:
            # Convierte la línea JSON a un diccionario.
            tweet = json.loads(line)
            
            # Verifica que el tweet contenga la clave 'content'.
            if 'content' in tweet:
                # Busca todos los emojis en el contenido del tweet.
                emojis = emoji_pattern.findall(tweet["content"])
                
                # Incrementa el contador para cada emoji encontrado.
                for emoji in emojis:
                    emoji_counter[emoji] += 1
                    
        except (json.JSONDecodeError, KeyError):
            # Ignora líneas que no se pueden decodificar como JSON o que no tienen la clave 'content'.
            continue

    # Obtiene los 10 emojis más comunes y sus conteos.
    top_emojis = emoji_counter.most_common(10)

    # Retorna la lista de los 10 emojis más utilizados.
    return top_emojis

# Ejemplo de uso
file_path = "farmers-protest-tweets-2021-2-4.json"  # Especifica la ruta del archivo JSON
result = q2_deficiente(file_path)  # Llama a la función
print(result)  # Imprime el resultado
