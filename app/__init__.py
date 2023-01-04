"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ceqjq1pa6gdovo0p821g-a.oregon-postgres.render.com",
        database="todo_cejy",
        user="root",
        password="zf4hXk0rSwK0ZY2vJ59ODu7X1NlwLLkf")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
