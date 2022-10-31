from flask_app import app
from flask import flash
from flask_app.models.models_user import User
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

db = 'pet_boarding_db'

class Pet:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.dob = data['dob']
        self.gender = data['gender']
        self.hair_color = data['hair_color']
        self.information = data['information']
        self.user_id = data['user_id']
        self.owner = None
        self.all_who_liked = []

    @classmethod
    def create_pet(cls, data):
        query = """
                INSERT INTO pets ( name, breed, dob, gender, hair_color, information, user_id )
                VALUES ( %(name)s, %(breed)s, %(dob)s, %(gender)s, %(hair_color)s, %(information)s, %(user_id)s )
                """
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def all_pets(cls):
        query = "SELECT * FROM pets"
        results = connectToMySQL(db).query_db(query)
        pets = []
        for pet in results:
            pets.append(cls(pet))
        return pets

    # @classmethod
    # def get_one(cls, data):
    #     query = """
    #             SELECT * FROM pets WHERE id = %(id)s
    #             """
    #     results = connectToMySQL(db).query_db(query, data)
    #     return cls(results[0])
    
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM pets
                JOIN users on users.id = pets.user_id
                WHERE pets.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        pet = cls(results[0])
        owner_data = {
            'id' : results[0]['users.id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at'],
        }
        pet.owner = User(owner_data)
        return pet
    
    @classmethod
    def like(cls, data):
        query = """
                INSERT INTO likes ( user_id, pet_id )
                VALUES ( %(user_id)s, %(pet_id)s )
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def dislike(cls, data):
        query = """
                DELETE FROM likes
                WHERE pet_id = %(pet_id)s
                AND user_id = %(user_id)s
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_who_liked(cls):
        query = """
                SELECT * FROM pets
                JOIN users ON users.id = pets.user_id
                LEFT JOIN likes ON pets.id = likes.pet_id
                LEFT JOIN users AS users2 ON users2.id = likes.user_id
                """
        results = connectToMySQL(db).query_db(query)
        pprint(results)
        likes = []
        for result in results:
            new_like = True
            liked_user_data = {
                'id' : result['users2.id'],
                'first_name' : result['users2.first_name'],
                'last_name' : result['users2.last_name'],
                'email' : result['users2.email'],
                'password' : result['users2.password'],
                'created_at' : result['users2.created_at'],
                'updated_at' : result['users2.updated_at'],
            }
            if len(likes) > 0 and likes[len(likes)-1].id == result['id']:
                likes[len(likes)-1].all_who_liked.append(User(liked_user_data))
                new_like = False
            if new_like: 
                like = cls(result)
                user_data = {
                    'id' : result['users.id'],
                    'first_name' : result['first_name'],
                    'last_name' : result['last_name'],
                    'email' : result['email'],
                    'password' : result['password'],
                    'created_at' : result['users.created_at'],
                    'updated_at' : result['users.updated_at'],
                }
                user = User(user_data)
                like.user = user
                if result['users2.id'] is not None:
                    like.all_who_liked.append(User(liked_user_data))
                likes.append(like)
        pprint(likes)
        return likes

    @classmethod
    def update_pet(cls, form_data, pet_id):
        query = f"UPDATE pets SET name = %(name)s, breed = %(breed)s, dob = %(dob)s, gender = %(gender)s, hair_color = %(hair_color)s, information = %(information)s WHERE id = {pet_id}"
        return connectToMySQL(db).query_db(query, form_data)
    
    @classmethod
    def delete_pet(cls, data):
        query = "DELETE FROM pets WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)