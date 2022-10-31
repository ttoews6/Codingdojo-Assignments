from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers.controllers_users import User

db = 'exam_db'

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.user_id = data['user_id']
        self.users = None
        self.user = None

    @classmethod
    def create_car(cls, data):
        query = """
                INSERT INTO cars ( price, model, make, year, description, user_id )
                VALUES ( %(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s )
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def all_cars(cls):
        query = """
                SELECT * FROM cars
                JOIN users ON cars.user_id = users.id
                """
        results = connectToMySQL(db).query_db(query)
        all = []
        for result in results:
            cars = cls(result)
            user_data= {
                'id' : result['users.id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'email' : result['email'],
                'password' : result['password'],
                'created_at' : result['users.created_at'],
                'updated_at' : result['users.updated_at'],
            }
            cars.users = User(user_data)
            all.append(cars)
        return all

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM cars
                JOIN users on users.id = cars.user_id
                WHERE cars.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        car = cls(results[0])
        user_data= {
                'id' : results[0]['users.id'],
                'first_name' : results[0]['first_name'],
                'last_name' : results[0]['last_name'],
                'email' : results[0]['email'],
                'password' : results[0]['password'],
                'created_at' : results[0]['users.created_at'],
                'updated_at' : results[0]['users.updated_at'],
            }
        car.user = User(user_data)
        return car
    
    @classmethod
    def update_car(cls, form_data, car_id):
        query = f"UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE id =   {car_id}"
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def delete_car(cls, data):
        query = """
                DELETE FROM cars WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def car_validator(data):
        is_valid=True
        if len(data['price']) <= 0:
            flash('Price must be greater than 0', 'car')
            is_valid = False
        if len(data['model']) < 2:
            flash('Model must be at least 3 characters', 'car')
            is_valid = False
        if len(data['make']) < 2:
            flash('Make must be at least 2 characters', 'car')
            is_valid = False
        if len(data['year']) <= 0:
            flash('Year must be greater than 0', 'car')
            is_valid = False
        if len(data['description']) < 10:
            flash('Description must be a minimum 10 characters', 'car')
            is_valid = False
        return is_valid