import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Чтение переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# Базовый URL для GitHub API
API_URL = 'https://api.github.com'

# Создание нового репозитория
def create_repo():
    url = f'{API_URL}/user/repos'
    data = {'name': REPO_NAME, 'private': False}
    response = requests.post(url, json=data, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    return response

# Проверка наличия репозитория
def check_repo_exists():
    url = f'{API_URL}/user/repos'
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    repos = [repo['name'] for repo in response.json()]
    return REPO_NAME in repos

# Удаление репозитория
def delete_repo():
    url = f'{API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    return response

# Тест
def test_github_api():
    print("Создание репозитория...")
    response = create_repo()
    if response.status_code == 201:
        print("Репозиторий создан успешно.")
    else:
        print(f"Ошибка создания репозитория: {response.json()}")

    print("Проверка наличия репозитория...")
    if check_repo_exists():
        print("Репозиторий найден.")
    else:
        print("Репозиторий не найден.")

    print("Удаление репозитория...")
    response = delete_repo()
    if response.status_code == 204:
        print("Репозиторий удален успешно.")
    else:
        print(f"Ошибка удаления репозитория: {response.json()}")

if __name__ == '__main__':
    test_github_api()
