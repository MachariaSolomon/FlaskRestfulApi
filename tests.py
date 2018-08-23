import unittest
import json
from app import app

class Test_Api(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_get(self):
        expected = 200
        actual = self.client.get('/todos')

        self.assertEqual(actual.status_code, expected)

    def test_get_one(self):
         # create setup data
        payload = {
            'title': 'Testing',
            'description': 'desc'
        }
        actual = self.client.post('/todos', data=payload)
        self.assertEqual(actual.status_code, 201)
        created_todo = json.loads(actual.get_data())
        expected = self.client.get('/todos/' + str(created_todo['id']))
        self.assertEqual(expected.status_code, 200)
        invalid =self.client.get('/todos' + str(created_todo['id']))
        self.assertEqual(invalid.status_code, 404)

    def test_post(self):
        # create setup data
        payload = {
            'title': 'Testing',
            'description': 'desc'
        }
        expected = 201
        # post
        actual = self.client.post('/todos', data=payload)
        # Assert that posting worked
        self.assertEqual(actual.status_code, expected)

    def test_put(self):
        # create setup data
        payload = {
            'title': 'Testing',
            'description': 'desc'
        }
       # post data
        actual = self.client.post('/todos', data=payload)
        self.assertEqual(actual.status_code, 201)

        created_todo = json.loads(actual.get_data())
        # create setup data
        payload = {
            'title': 'Testing2',
            'description': 'desc'
        }
        expected = self.client.put('/todos/' + str(created_todo['id']), data=payload)
        self.assertEqual(expected.status_code, 201)



    def test_delete(self):
       payload = {
           'title': 'A Title',
           'description': 'Something new'
       }
       actual = self.client.post('/todos', data=payload)
       self.assertEqual(actual.status_code, 201)
       
       created_todo = json.loads(actual.get_data())
       expected = self.client.delete('/todos/' + str(created_todo['id']))
       self.assertEqual(expected.status_code, 204)
       response = self.client.get('/todo/' + str(created_todo['id']))
       self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
