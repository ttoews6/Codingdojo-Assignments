from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_user import User

db = 'dojo_wall_db'

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.user = None


    @classmethod
    def create_post(cls, data):
        query = """
                INSERT INTO posts ( content, user_id )
                VALUES ( %(content)s, %(user_id)s )
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def all_posts(cls):
        query = """
                SELECT * FROM posts
                JOIN users ON users.id = posts.user_id
                WHERE posts.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query)
        posts = []
        for result in results:
            posts.append(cls(result))
            user_data = {
                    'id' : result['users.id'],
                    'first_name' : result['first_name'],
                    'last_name': result['last_name'],
                    'email' : result['email'],
                    'password' : result['password'],
                    'created_at' : result['users.created_at'],
                    'updated_at' : result['users.updated_at'],
                    }
        return posts
