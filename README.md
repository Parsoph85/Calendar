<div id="header" align="center">
<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/></div>
<div id="count" align="center">
<img src="https://komarev.com/ghpvc/?username=Parsoph85&style=flat-square&color=blue" alt="" align="center"/>
</div>
<h1 align="center">
  Привет
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>

---

### :man_technologist: О проекте :

Проект API (далее просто Проект) для ведения календаря на языке Python создан для выполнения домашнего задания.В данном файле описан функционал проекта.
#### Требования:
* API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
* Модель данных "Событие": ID, Дата, Заголовок, Текст
* Локальное хранилище данных
* Максимальная длина заголовка — 30 символов
* Максимальная длина поля Текст — 200 символов
* Нельзя добавить больше одного события в день
* API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)
* Формат данных: "ГГГГ-ММ-ДД|заголовок|текст"

#### Состав:
Проект состоит из модулей: основной скрипт, скрипт для сервера, скрипт моделей, скрипт логики, скрипт работы с БД и сама БД.
В модулях реализован функционал работы с постами и пользователями:
* Модуль main - основной обработчик.
* Модуль model - для описания объектов заметок и их свойств. Здесь задается тип данных и длина заголовка и текста.
* Модуль logic - основная логика. Сюда передаются входящие параметры из запросов. Затем идет проверка на типы запросов, тела и параметры. Идет проверка на соответствие даты заданному шаблону. Заголовок и текст обрезаются до заданной величины.
* Модуль db - для создания локальной бд (SQLite) и рабочей таблицы. Также для отправки запросов в БД. 
* Файл БД.
#### Техническая часть:
* Основные зависимости находятся в файле requirements.txt
* Для хранения сущностей (объектов) будем использовать легкую (и встроенную) SQLite.
* Так как проект учебный, для уменьшения кода отсутствует проверка на спецсимволы в запросах и использование несуществующих ИД.
* Ввод и вывод данных в соответствии с заданием.
* Тестирование выполнялось при помощи ПО Postman https://www.postman.com/downloads/

> ## Внимание!!!
> Помните, что проект учебный.
> А это значит, что функционал делался именно под установленные задачи.
> В связи с этим, работа проекта не гарантируется (а скорее гарантируется неработоспособность) при использовании не описанного функционала.

#### Описание запросов:

|Функция| Идентификатор | Метод | Тело запроса                                      |
|-------|----------|---------|---------------------------------------------------|
|Добавление поста| /api/v1/calendar/  | POST    | ГГГГ-ММ-ДД \|заголовок \|текст |
|Просмотр определенного поста| /api/v1/calendar/<ИД> | GET      | нет                                               |
|Просмотр всех постов| /api/v1/calendar/    | GET   | нет                                               |
|Изменение поста| /api/v1/calendar/<ИД> |PUT   | ГГГГ-ММ-ДД\|заголовок \|текст                     |
|Удаление поста| /api/v1/calendar/<ИД>  | DELETE  | нет                                               |

#### Запуск проекта:
Для корректной работы необходимо установить зависимости pip install -r requirements.txt
Для тестирования проекта достаточно запустить выполнение скрипта main.py. 
Запросы рекомендуется передавать через Postman. Тип запроса выбирается из списка, в поле вводится адресная строка, в тело в формате "ГГГГ-ММ-ДД|заголовок|текст".
#### Примеры запросов:
* GET http://localhost:5000/api/v1/calendar/6 - Выдает пост с ИД = 6
* GET http://localhost:5000/api/v1/calendar/ - выдает все посты
* POST http://localhost:5000/api/v1/calendar/ 2015-05-20|Первый-н...|Эх, прокачу! - Запишет в БД заметку.
* PUT http://localhost:5000/api/v1/calendar/10 2016-05-20|Второй-н...|С Федота на Якова - Заменит заметку под номером 10 на новую.
* DELETE http://localhost:5000/api/v1/calendar/2 - Удалит пост с ИД = 2

> ## Важно знать.
> Количество строк в тестовой БД - 2. А значит, действия с заметками можно проводить только в пределах этого значения.
> Исключение - добавление заметки. Добавление приведет к увеличению количества строк и, соответственно, диапазона работы.
