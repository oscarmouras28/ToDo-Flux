from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
  jToDos = jsonify(todos)
  print(jToDos)
  return jToDos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    print(request_body)
    todos.append(request_body)
    jtodos=jsonify(todos)
    return jtodos
  
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    jtodos=jsonify(todos)
    return jtodos

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)