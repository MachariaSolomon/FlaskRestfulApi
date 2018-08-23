from uuid import uuid4
from time import time
import json

# class JsonSerializable(object):
#     def toJson(self):
#         return json.dumps(self.__dict__)

#     def __repr__(self):
#         return self.toJson()

class TodoItem(object):
    def __init__(self, title, description=''):
        self._id = uuid4().int # generate id
        self.title = title
        self.description = description
        self.created_at = time()
    
    def serialize(self):
        return {
            'id': self._id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at
        }

    # def __repr__(self):
    #     return self.title
