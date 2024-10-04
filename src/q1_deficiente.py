import json
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_deficiente(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Devuelve las 10 fechas con más tweets y el usuario que más tweets publicó en esas fechas.

    """

    # Cargar todos los tweets en memoria
    tweets = []

    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            tweet = json.loads(line)
            tweets.append(tweet)

    # Inicializa contadores de tweets por fecha y usuario
    date_tweet_count = defaultdict(int)
    date_user_tweets = defaultdict(lambda: defaultdict(int))

    # Procesar los tweets
    for tweet in tweets:
        date_str = tweet["date"][:10]  # Extrae la parte de la fecha
        username = tweet["user"]["username"]  # Obtiene el nombre de usuario

        # Incrementar el contador para la fecha y el usuario
        date_tweet_count[date_str] += 1
        date_user_tweets[date_str][username] += 1

    # Lista para almacenar la fecha y el usuario con más tweets
    top_dates_users = []

    for date, user_tweets in date_user_tweets.items():
        max_user = max(user_tweets.items(), key=lambda x: x[1])  # Usuario más activo

        # Agregar el resultado a la lista sin la cantidad total de tweets
        top_dates_users.append((datetime.strptime(date, '%Y-%m-%d').date(), max_user[0], date_tweet_count[date]))

    # Ordenar las fechas de forma descendente por la cantidad total de tweets
    sorted_dates = sorted(top_dates_users, key=lambda x: x[2], reverse=True)

    # Retornar solo las 10 fechas con más tweets (sin la cantidad total)
    return [(date, user) for date, user, _ in sorted_dates[:10]]

# Ejemplo de uso
file_path = "farmers-protest-tweets-2021-2-4.json"  # Especifica la ruta del archivo JSON
result = q1_deficiente(file_path)  # Llama a la función
print(result)  # Imprime el resultado
