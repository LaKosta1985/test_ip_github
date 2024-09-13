import requests
from dotenv import load_dotenv
import os

load_dotenv() # Загружаем переменные окружения

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USER")
REPO_NAME = os.getenv("REPO_NAME")



# Заголовок авторизации с токеном
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json", 
}

def create(NAME):
    url = "https://api.github.com/user/repos"
    data = {
        "name": NAME, 
        "private": False,
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Репозиторий '{NAME}' создан.")
    else:
        print(f"Не удалось создать репозиторий {NAME}: {response.status_code}, {response.json()}")

def get_repos():
    #Получение списка репозиториев.
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        return [repo['name'] for repo in repos]  # Возвращаем список репозиториев
    else:
        print(f"Не удалось получить список репозиториев: {response.status_code}, {response.json()}")
        return []

def delete(NAME):
    #Удаление репозитория.
    url = f"https://api.github.com/repos/{USERNAME}/{NAME}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Репозиторий '{NAME}' успешно удален.")
    else:
        print(f"Не удалось удалить репозиторий: {response.status_code}, {response.json()}")

# Создаем репозиторий
create(REPO_NAME)
# Проверяем его наличие в списке репозиториев
repos = get_repos()
if REPO_NAME in repos:
    print(f"Репозиторий '{REPO_NAME}' присутствует в списке репозиториев.")
else:
    print(f"Репозиторий '{REPO_NAME}' не найден.")

# Удаляем репозиторий
delete(REPO_NAME)
