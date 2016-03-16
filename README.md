Simple REST application built in Flask, Peewee ORM and AngularJS.

## Configuration Instructions:
1. Required installations: Flask, Peewee, Sqllite3, Jinja

## Operating Instructions:
- To start a web app run app.py
- Go to http://0.0.0.0:5000 where you will see the main page with users in a table format.
- There is an endpoint to create a new user: http://0.0.0.0:5000/create 
- There is also an endpoint to fetch all the users: http://0.0.0.0:5000/users
- Angular uses this endpoint to query for users and display the result on the web page.