# FlaskRestfulApi

A simple project on using FlaskRestful to create Restful API endpoints.

[![Build Status](https://travis-ci.org/MachariaSolomon/FlaskRestfulApi.svg?branch=master)](https://travis-ci.org/MachariaSolomon/FlaskRestfulApi)
[![Coverage Status](https://coveralls.io/repos/github/MachariaSolomon/FlaskRestfulApi/badge.svg?branch=master)](https://coveralls.io/github/MachariaSolomon/FlaskRestfulApi?branch=master)

## Getting Started

**Ensure you have:**

* python3

### Installation

1. **Clone the repository into the empty folder**

      >`https://github.com/MachariaSolomon/FlaskRestfulApi.git`

2. **Create a virtual environment**

      >`python3 -m venv /path/to/new/virtual/environment`

3. **Activate the virtual environment**

      >`source yourvirtualenvironment/bin/activate`

4. **Install required dependancies**

      >`pip install -r requirements.txt`

      >`pip freeze > requirements.txt`

5. **Run the app**

      Simply run in the command line:

      >`python app.py` 

**Using either Postman/ Insomnia:**

Run the following routes to test that the endpoints are functioning as expected:

**To fetch Todo items**

To fetch **all** Todo items.

Use:

>`http://localhost/todos`

To fetch a **single** Todo item.

Use:

>`http://localhost/todos/<todo_id>`

**To create a new Todo item**

Remember to change the method to **POST** then use:

>`http://localhost/todos` 

**To modify a Todo item**

Remember to change the method to **PUT** then use:

>`http://localhost/todos/<todo_id>`

**To Delete a todo_item**

Remember to change the method to **DELETE** then use:

`http://localhost/todos/<todo_id>`

## Running the tests

To run the tests in the **command line**, use either:

>`python tests.py` ,
Runs unittest

or

>`nosetests`

>`nosetests -v`
Runs nosetests in verbose

or simply

>`pytest`

### A breakdown of the tests

Test the **GET/todos** endpoint.

Using **POST**,create a todo item. Assert that this returns a **201** staus code meaning the item is successfully created. Use the get method to see that the created todo item is returned.Assert that the item returned is equal to the one created. Assert The method is returning a **200** status code.

Try getting a todo item that does not exist and assert that the returned result is a **404** status code and the Error message todo item {} does not exist.

Test the **POST/todos** endpoint.

initialize
Use POST method to create a new todo item.
