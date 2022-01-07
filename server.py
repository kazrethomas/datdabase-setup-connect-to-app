from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine


db_connect = create_engine('sqlite:///tester.db')
app = Flask(__name__)
api = Api(app)

class Stufftodo(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from stufftodo") # This line performs query and returns json result
        return {'stufftodo': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID


api.add_resource(Stufftodo, '/stufftodo') # Route_1

if __name__ == '__main__':
     app.run(port='5002')

