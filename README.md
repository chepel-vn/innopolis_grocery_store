[![Build Status](https://app.travis-ci.com/chepel-vn/innopolis_grocery_store.svg?branch=master)](https://app.travis-ci.com/chepel-vn/innopolis_grocery_store)

Клонирование себе репозитория с github на локальную машину

    git clone <ссылка на репозиторий>

Настройка виртуального окружения

    python -m venv env
    venv\Scripts\activate

Установка необходимых пакетов

    pip install -r requirements.txt

Настройка Linter

    Используются файлы конфигурационные файлы:
        .toml
        pre-commit-config.yaml
        .flake8

    Запуск проверок:
        pre-commit run --all-files

Запуск тестов с html отчетом

    pytest --html=report.html --self-contained-html

Использование Travis CI

    конфигурационный файл .travis.yml

Краткое описание проекта

    Необходимо написать ui тесты:
    1. Поиск товаров (негативный и позитивный сценарий)
    2. Добавление товара в корзину
    3. Работа с корзиной: удаление/добавление товара и покупка



