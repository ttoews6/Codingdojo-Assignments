from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

db = "cookie_orders"

class Cookie:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders"
        results = connectToMySQL(db).query_db(query)
        cookies = []
        for cookie in results:
            cookies.append(cls(cookie))
        return cookies

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])
    
    #update order
    @classmethod
    def update(cls, data):
        query = """
                UPDATE cookie_orders
                SET first_name = %(first_name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s 
                WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, data)

    #create order
    @classmethod 
    def new_order(cls, data):
        query = """
                INSERT INTO cookie_orders ( first_name, cookie_type, num_boxes )
                VALUES ( %(first_name)s, %(cookie_type)s, %(num_boxes)s )
                """
        return connectToMySQL(db).query_db(query, data)

    #validate order
    @staticmethod
    def validate_order( data ):
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(data['cookie_type']) < 2:
            flash("Cookie Type must be at least 2 characters.")
            is_valid = False
        if len(data['num_boxes']) < 1:
            flash("Minimum number of boxes required is 1.")
            is_valid = False
        return is_valid