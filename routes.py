from flask import Blueprint, request, jsonify
from models import db, Todo

api = Blueprint('api', __name__)

# 获取任务列表
@api.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{"id": t.id, "title": t.title, "done": t.done} for t in todos])

# 添加任务
@api.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json
    title = data.get('title')
    if not title:
        return jsonify({"error": "Task title required"}), 400
    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return jsonify({"id": todo.id, "title": todo.title, "done": todo.done}), 201

# 删除任务
@api.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return '', 204
