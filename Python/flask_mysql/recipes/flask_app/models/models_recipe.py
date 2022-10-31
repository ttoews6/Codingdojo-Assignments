from datetime import date
from flask_app import app
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
import re
from flask_app.models.models_user import User

db = 'recipes_db'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.user_id = data['user_id']
        self.users = None
        self.user = None

    @classmethod
    def create_recipe(cls, data):
        query = """
                INSERT INTO recipes ( name, description, instructions, date_made, under, user_id )
                VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s, %(user_id)s )
                """
        return connectToMySQL(db).query_db(query, data)
        
    @classmethod
    def all_recipes(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                """
        results = connectToMySQL(db).query_db(query)
        pprint(results)
        all = []
        for result in results:
            recipes = cls(result)
            user_data = {
                'id' : result['users.id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'email' : result['email'],
                'password' : result['password'],
                'created_at' : result['users.created_at'],
                'updated_at' : result['users.updated_at'],
            }
            recipes.users = User(user_data)
            all.append(recipes)
        return all

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM recipes 
                JOIN users ON users.id = recipes.user_id
                WHERE recipes.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        recipe = cls(results[0])
        user_data = {
                'id' : results[0]['users.id'],
                'first_name' : results[0]['first_name'],
                'last_name' : results[0]['last_name'],
                'email' : results[0]['email'],
                'password' : results[0]['password'],
                'created_at' : results[0]['users.created_at'],
                'updated_at' : results[0]['users.updated_at'],
            }
        recipe.user = User(user_data)
        return recipe
    
    @classmethod
    def update_recipe(cls, form_data, recipe_id):
        query = f"UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under = %(under)s WHERE id =   {recipe_id}"
        return connectToMySQL(db).query_db(query, form_data)
    
    @classmethod
    def delete_recipe(cls, data):
        query = """
                DELETE FROM recipes WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, data)
    
    @staticmethod
    def recipe_validator(data):
        DATE_REGEX = re.compile(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')
        is_valid = True
        if len(data['name']) < 3:
            flash('Name must be at least 3 characters', 'recipe')
            is_valid = False
        if len(data['description']) < 3:
            flash('Description must be at least 3 characters', 'recipe')
            is_valid = False
        if len(data['instructions']) < 3:
            flash('Instructions must be at least 3 characters', 'recipe')
        # if not DATE_REGEX.match(data['date_made']):
        #     flash('Please enter valid date', 'recipe')
        #     is_valid = False
        return is_valid
