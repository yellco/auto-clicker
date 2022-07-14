# auto-clicker
Приложение для автоматического совершения постоянных кликов через определенный интервал на python.

![Простой авто-кликер на питоне c интерфейсом](https://raw.githubusercontent.com/yellco/auto-clicker/master/screenshot.jpeg)

## Инструкция по использованию

1) Необходимо определить целевые координаты нажатием кнопки "Получить координаты" и после кликнуть по целевому месту клика

2) Запустить авто-кликер нажатием кнопки "Запустить". Доступна остановка кликера нажатием кнопки "Остановить"

## Инструкция по разворачиванию

1) Необходима версия python = 3.9. Также необходим установленный poetry

2) Скопировать файл /deploy/.env-copy в /.env

3) Установить все зависимости:
```sh
poetry install
```

4) Запустить приложение:
```sh
poetry run app
```

***Примечание: инструкция актуальна для версии 0.1.1***

## Для запуска тестов (автотестирование пока не настроено)
```sh
poetry run pytest -vv
```
