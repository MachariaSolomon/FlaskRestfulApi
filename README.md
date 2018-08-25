# FlaskRestfulApi

A simple project on using FlaskRestful to create Restful API endpoints.

[![Build Status](https://travis-ci.org/MachariaSolomon/FlaskRestfulApi.svg?branch=master)](https://travis-ci.org/MachariaSolomon/FlaskRestfulApi)

## Getting Started

**Ensure you have:**

* python3
* created an empty folder in your machine

### Installation

1. **Clone the repository into the empty folder**

      >`https://github.com/MachariaSolomon/FlaskRestfulApi.git`

2. **Create a virtual environment**

      >`python3 -m venv /path/to/new/virtual/environment`

3. **To activate the virtual environment**

      >`source .env/bin/activate`

4. **To install required dependancies**

      >`pip install -r requirements.txt`

      >`pip freeze > requirements.txt`

5. **To run the app**

      Simply run in the command line:

      >`python app.py` 

**Using either Postman/ Insomnia:**

Run the following routes to test that the endpoints are functioning as expected:

**To fetch Todo items**

Run:

To fetch **all** Todo items.

>`http://localhost/todos`

To fetch a **single** Todo item.

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

### A break down of the tests

Test the **GET/todos** endpoint.

using POST,create a todo item. Assert that this returns a **201** staus code meaning the item is successfully created. Use the get method to see that the created todo item is returned.Assert that the item returned is equal to the one created. The method should return a **200** status code.

Also try getting a todo item that does not exist and assert that the returned result is a **404** status code and the Error message todo item {} does not exist.  -->

Test the **POST/todos** endpoint.

initialize
Use POST method to create a new todo item.