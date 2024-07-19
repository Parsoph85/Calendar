import db
import re
from model import Note


class Events:
    def __init__(self, *a):
        pass

    def create(self, data: str):
        self.data = data
        ext_mess_ttl = ''
        ext_mess_txt = ''
        inp_str = data.split("|")
        data = inp_str[0]
        data_m = re.match(r'^[0-9]{4}-{1}[0-9]{2}-{1}[0-9]{2}$', inp_str[0])
        if data_m:
            title = inp_str[1]
            text = inp_str[2]

            if len(title) > Note.title_len:
                title = title[0:Note.title_len]

            if len(text) > Note.text_len:
                text = text[0:Note.text_len]

            db_string = f"INSERT INTO events (data, title, text) VALUES ('{data}','{title}','{text}')"
            answer = db.db_work(db_str=db_string)
            return("Success. ")
        else:
            return("Дата не соответствует формату. ")

    def read(self, n_id: int):
        self.n_id = n_id
        if n_id==0:
            db_string = f"SELECT * FROM events"
        else:
            db_string = f"SELECT * FROM events WHERE id = '{n_id}'"
        answer = db.db_work(db_str=db_string)
        return (answer)

    def update(self,n_id: int, data: str):
        self.data = data
        self.n_id = n_id
        ext_mess_ttl = ''
        ext_mess_txt = ''
        inp_str = data.split("|")
        data = inp_str[0]
        title = inp_str[1]
        text = inp_str[2]

        if len(title) > Note.title_len:
            title = title[0:Note.title_len]

        if len(text) > Note.text_len:
            text = text[0:Note.text_len]
        db_string = f"UPDATE events SET data = '{data}', title = '{title}', text = '{text}' WHERE id = '{n_id}'"
        answer = db.db_work(db_str=db_string)
        return ("Success. ")

    def delete(self, n_id: int):
        self.n_id = n_id
        db_string = f"DELETE FROM events WHERE id='{n_id}'"
        answer = db.db_work(db_str=db_string)
        return ("Success. ")

"""
Нужна проверка на добавление в одну дату
"""