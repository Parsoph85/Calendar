import logic

from flask import Flask, request

app = Flask(__name__)

api_root = "/api/v1"
note_api_root = api_root + "/calendar"


@app.route(note_api_root + "/", methods=["POST"])
def create():
    try:
        data = str(request.get_data().decode('utf-8'))
        info = logic.Events().create(data=data)
        return f"{info}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(note_api_root + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        _id = int(_id)
        info = logic.Events().read(n_id=_id)
        return f"{info}", 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(note_api_root + "/", methods=["GET"])
def lists():
    try:
        _id = 0
        info = logic.Events().read(n_id=_id)
        return f"{info}", 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(note_api_root + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        _id = int(_id)
        data = str(request.get_data().decode('utf-8'))
        info = logic.Events().update(n_id=_id, data=data)
        return f"{info}", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(note_api_root + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _id = int(_id)
        info = logic.Events().delete(n_id=_id)
        return f"{info}", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404


if __name__ == '__main__':
    app.run()
