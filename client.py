import requests
from collections import Counter

# Configurar URLs de los endpoints
BASE_URL = "http://127.0.0.1:5000"
AUTH_URL = f"{BASE_URL}/api/v1/auth/"
BREEDS_URL = f"{BASE_URL}/api/v1/breeds/"
DOGS_URL = f"{BASE_URL}/api/v1/dogs/"
ANSWER_URL = f"{BASE_URL}/api/v1/answer/"

# Tus credenciales
EMAIL = "admin@example.com"
PASSWORD = "1234"


# Función para autenticarse y obtener un token JWT.
def authenticate():
    response = requests.post(AUTH_URL, json={"email": EMAIL, "password": PASSWORD})
    response.raise_for_status()
    return response.json().get("token", "")


# Obtener la lista de razas
def get_breeds(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(BREEDS_URL, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    return data.get("count", 0), data.get("results", [])


# Obtener la lista de perros
def get_dogs(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(DOGS_URL, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    return data.get("count", 0), data.get("results", [])


# Encontrar la raza y el nombre de perro más comunes.
def find_common_breed_and_name(dogs):
    breeds = [dog.get("breed", "Desconocido") for dog in dogs]
    names = [dog.get("name", "Desconocido") for dog in dogs]

    most_common_breed = Counter(breeds).most_common(1)
    most_common_name = Counter(names).most_common(1)

    return (most_common_breed[0][0] if most_common_breed else "Desconocido",
            most_common_name[0][0] if most_common_name else "Desconocido")


# Enviar los resultados
def send_answer(token, total_breeds, total_dogs, common_breed, common_name):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "totalBreeds": total_breeds,
        "totalDogs": total_dogs,
        "commonBreed": common_breed,
        "commonDogName": common_name
    }
    response = requests.post(ANSWER_URL, json=payload, headers=headers)

    try:
        response.raise_for_status()
        print("✅ Respuesta enviada correctamente:", response.json())
    except requests.exceptions.HTTPError as err:
        print(f"❌ Error al enviar la respuesta: {err}, Detalles: {response.text}")


# Ejecución del flujo de trabajo
try:
    token = authenticate()
    print(f"✅ Token obtenido: {token}")

    total_breeds, breeds = get_breeds(token)
    print(f"✅ Total de razas: {total_breeds}, Datos: {breeds}")

    total_dogs, dogs = get_dogs(token)
    print(f"✅ Total de perros: {total_dogs}, Datos: {dogs}")

    common_breed, common_name = find_common_breed_and_name(dogs)
    print(f"✅ Raza más común: {common_breed}, Nombre más común: {common_name}")

    send_answer(token, total_breeds, total_dogs, common_breed, common_name)
except Exception as e:
    print(f"❌ Error general: {e}")

