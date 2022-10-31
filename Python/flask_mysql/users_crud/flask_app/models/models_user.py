from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

from pprint import pprint

db = "users_schema"


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(db).query_db(query)
        pprint(results)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    #Create User
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users ( first_name, last_name, email ) 
                VALUES ( %(first_name)s, %(last_name)s, %(email)s )
                """
        return connectToMySQL(db).query_db(query, data)
    
    #Update User
    @classmethod
    def update(cls, form_data):
        query = """
                UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, form_data)

    #Delete User
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    #Validate New User info
    @staticmethod
    def validate_user( data ):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) == 0:
            flash("First name is required.")
            is_valid = False
        if len(data['last_name']) == 0:
            flash("Last name is required.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid