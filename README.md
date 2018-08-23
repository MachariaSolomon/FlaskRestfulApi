# FlaskRestfulApi

A simple project on using FlaskRestful to create Restful API endpoints.

[![Build Status](https://travis-ci.org/MachariaSolomon/FlaskRestfulApi.svg?branch=master)](https://travis-ci.org/MachariaSolomon/FlaskRestfulApi)

## Getting Started

**Ensure you have:**

* python3
* created an empty folder in your machine

### Installation

1. **Clone the repository into the empty folder**

`https://github.com/MachariaSolomon/FlaskRestfulApi.git`

2. **Create a virtual environment**

>`python3 -m venv /path/to/new/virtual/environment`

3. **To activate the virtual environment**

`source .env/bin/activate`

4. **Insall dependancies**

Run:

`pip install -r requirements.txt`

`pip freeze > requirements.txt`

5. **To run the app**

Simply run in the command line:

`python app.py` 

Using either Postman/ Insomnia:

Run the following routes to test that the endpoints are functioning as expected:

**To fetch Todo items**
Run:

`http://localhost/todos` to fetch all your Todo items.

`http://localhost/todos/<todo_id>` to fetch a single Todo item.

**To create a new Todo item**
Run:

`http://localhost/todos` Remember to change the method to >POST

**To modify a Todo item**
Run:

`http://localhost/todos/<todo_id>` Remember to change the method to >PUT

**To Delete a todo_item**
Run:

`http://localhost/todos/<todo_id>` Remember to change the method to >DELETE

## Running the tests

In the command line, run

`python tests.py`

or simply

`nosetests`

or

`pytest`

