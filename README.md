#### Python скрипт для создания, проверки и удаления репозитория на GitHub

#### Задание:

Создание нового репозитория
Проверка его наличия в списке репозиториев
Удаление репозитория

#### Последовательность действий:

1. Клонируйте репозиторий:
   git clone https://github.com/LaKosta1985/test_ip_github
   cd github-api-test
2. Установите зависимости
   pip install -r requirements.txt
3. Создайте файл .env в корне проекта и добавьте ваши данные
   TOKEN="you_token"
   USER="user_name"
   REPO_NAME="you_repository"
4. Запустите скрипт
   python test_api.py

> Примечание:Ваш GitHub токен(TOKEN="you_token")должен имееть разрешения для создания и удаления репозиториев.
