# FlaskProject1

FlaskProject1 — это веб-приложение на базе Flask, предназначенное для демонстрации базовой структуры и функциональности приложения. 

## Установка

Следуйте инструкциям ниже, чтобы настроить окружение и установить все зависимости для запуска проекта.

### Шаг 1: Создание виртуального окружения

Создайте виртуальное окружение для изоляции зависимостей проекта.

```bash
python -m venv .venv
```

### Шаг 2: Активация виртуального окружения
```bash
source .venv/bin/activate
```

### Шаг 3: Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск приложения
```bash
python app.py
```


### Настройка

Для правильной работы приложения требуется создать файл .env в корневой директории проекта и добавить в него следующие параметры:
.env file example

```ini
DB_HOSTNAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'test_db'
APP_SETTINGS = 'DevelopmentConfig'
```

### Пример запроса
```code
http://127.0.0.1:5000/api/version
```
### note
```code
API_PREFIX set as /api
```
