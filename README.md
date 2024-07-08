# Тествое задание на позицию "Junior Python Developer"

## Сервис прохождения опросов на Django

### Технологии

Python 3.11.4
Django 5.0.6

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/elenashovtyuk/test_kokoc_group
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```
* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### Загрузка тестовых данных

```
python3 manage.py loaddata db.json
```

### Запуск проекта в dev-режиме

- В папке с файлом manage.py выполните команду:

```
python3 manage.py runserver
```

### Автор

Шовтюк Елена
