# the_factory_bot_task
___
Данное приложение является простым эхо-ботом. В нем реализованны:
- [x] Регистрация
- [x] Авторизация
- [x] Генерация токена для телеграм бота. (Только после авторизации)
- [x] Отправка сообщений своему боту (Только после авторизации)
- [x] Получение списка всех сообщений (Только после авторизации)
___

## стек

+ python3.10 <img height="24" width="24" src="https://cdn.simpleicons.org/python/5066b3" />
+ Django 4.1 <img height="24" width="24" src="https://cdn.simpleicons.org/django/5066b3" />
+ Postgres 15.0 <img height="24" width="24" src="https://cdn.simpleicons.org/postgresql/5066b3" />
+ Docker <img height="24" width="24" src="https://cdn.simpleicons.org/docker/5066b3" />
+ poetry<img height="24" width="24" src="https://cdn.simpleicons.org/poetry/" />
+ DRF 3.14
+ Redis<img height="24" width="24" src="https://cdn.simpleicons.org/redis/" />
+ Docker-compose
___

## swagger
http://vbodrin.tk:8080/docs/swagger
___

## Установка:
1. Клонируйте репозиторий с github на локальный компьютер
2. Создайте виртуальное окружение 
3. Создайте в корне проекта файл в .env и заполните переменными окружения из .env.example
4. Соберите и поднимите docker-контейнер командой `make local-start-docker-compose`
5. Для запуска тестов использовать команду `make start-test`
___

## Как пользоваться
 Сперва необходимо создать учетную запись, затем авторизоваться и создать токен. После чего зайти в телеграм-бот
 @Factofy_Bodrin_bot и подтвердить учетную запись отправив токен боту. Дальше можно отправлять сообщения по API
и они будут дублироваться в телеграм-боте, так же можно получить список всех своих сообщений (по 10 шт на странице)
___

## Endpoint:
+ /signup (Регистрация нового пользователя)
+ /login (Вход по логину и паролю)
+ /logout (Выход из учетной записи)
+ /token (Создание токена для авторизации в telegram боте)
+ /message (Написать сообщение)
