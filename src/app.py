from flask import Flask, jsonify, request

app=Flask(__name__)

todos=[
      {"label": "Mi primera tarea", "done":False},
      {"label": "Mi 2da tarea", "done":True}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    texto_en_json = jsonify(todos)
    return texto_en_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body= request.json
    todos.append(request_body)
    print("viene una solicitud entrante con la siguiente body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is to positiion to delete:", position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)