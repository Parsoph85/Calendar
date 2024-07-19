"""
— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
— модель данных "Событие": ID, Дата, Заголовок, Текст
— локальное хранилище данных
— максимальная длина заголовка — 30 символов
— максимальная длина поля Текст — 200 символов
— нельзя добавить больше одного события в день
— API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" (по аналогии с заметкой)
"""

import sqlite3
#import model
#import logic

from flask import Flask, request

app = Flask(__name__)

conn = sqlite3.connect('calendar.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, title TEXT, text TEXT)''')
conn.commit()
cursor.close()

api_root = "/api/v1"
note_api_root = api_root + "/note"


@app.route(note_api_root + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')



       # note = _from_raw(data)
       # _id = _note_logic.create(note)

        return f"new id: {data}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(note_api_root + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        note = _note_logic.read(_id)
        raw_note = _to_raw(note)
        return raw_note, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404






"""



@app.route('/posts', methods=['POST'])  # Создание поста
def create_post():
    post_json = request.get_json()  # Получаем данные из запроса
    json_data = json.dumps(post_json)  # Применяем кунг-фу для...
    post = json.loads(json_data)  # ... адекватного преобразования JSON в словарь
    body = post.get('body')  # Вытаскиваем из запроса значения
    user = post.get('user')
    posts = Posts().create(body=body, user=user)  # Хитрой магией отправляем значения на запись в БД
    return jsonify({'Status': posts})  # Информируем, что все хорошо



@app.route('/posts', methods=['GET'])  # Выводим нужный пост. Если нет id - ставим 0
def read_post():
    post_id = request.args.get('post_id', default=0, type=int)
    posts = Posts().read(post_id=post_id)
    return jsonify({'posts': posts})  # Экспорт в FE


@app.route('/posts', methods=['DELETE']) # Удаляем нужный пост
def del_post():
    post_id = request.args.get('post_id', type=int)
    posts = Posts().delete(post_id=post_id)
    return jsonify({'posts': posts})  # Экспорт в FE


@app.route('/posts', methods=['PUT'])  # Изменяем нужный пост
def change_post():
    post_id = request.args.get('post_id', type=int)
    post_json = request.get_json()  # Получаем данные из запроса
    json_data = json.dumps(post_json)  # Применяем кунг-фу для...
    post = json.loads(json_data)  # ... адекватного преобразования JSON в словарь
    body = post.get('body')  # Вытаскиваем из запроса значения
    user = post.get('user')
    posts = Posts().change(post_id=post_id,body=body,user=user)
    return jsonify({'posts': posts})  # Экспорт в FE

"""
