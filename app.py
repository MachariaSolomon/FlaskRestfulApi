import time
from uuid import uuid4
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

from models import TodoItem

app = Flask(__name__)
api = Api(app)

Todos = []

parser = reqparse.RequestParser()
# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        # import pdb; pdb.set_trace()
        for todo in Todos:
            # print('sol1', todo._id, 'sol end')
            if todo._id == int(todo_id):
                # print('sol1', todo, 'solend')
                return todo.serialize()
            else:
                abort(404, message="Todo {} doesn't exist".format(todo_id))

    def delete(self, todo_id):
        for todo in Todos:
            # if todo_id not in Todos:
            #     abort(404)
            if todo._id == int(todo_id):
                Todos.remove(todo)
                return '', 204
            else:
                abort(404, message="Todo {} doesn't exist".format(todo_id))

    def put(self, todo_id):
         # validate incoming data
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        # parse args
        args = parser.parse_args()

        for todo in Todos:
            if todo._id == int(todo_id):
                todo.title = args['title']
                todo.description = args['description']
                return todo.serialize(), 201
# TodoList
# shows a list of all todos, and lets you POST to add new todos

class TodoList(Resource):
    def get(self):
        return jsonify([item.serialize() for item in Todos])

    def post(self):
        # validate incoming data
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)

        # parse args
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        
        # create new todo
        new_todo = TodoItem(title, description)
        print(new_todo)

        # save todo
        Todos.append(new_todo)

        # return8888 created todo
        return new_todo.serialize(), 201
##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
