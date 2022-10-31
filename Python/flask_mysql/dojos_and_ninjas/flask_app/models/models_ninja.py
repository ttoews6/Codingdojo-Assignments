from sqlite3 import connect
from types import ClassMethodDescriptorType
from flask_app import app
from flask_app.models.models_dojo import Dojo
from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in ninjas:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = """
                INSERT INTO ninjas ( first_name, last_name, age, dojo_id )
                VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s )
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def ninjas_and_dojos(cls, data):
        query = """
                SELECT * FROM ninjas
                LEFT JOIN dojos
                ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        ninjas = []
        for ninja in results:
            ninja_dojo = cls(ninja)
            dojo_data = {
                'id' : ninja['dojos.id'],
                'name' : ninja['name'], 
                'created_at' : ninja['dojos.created_at'],
                'updated_at' : ninja['dojos.updated_at']
            }
            ninja_dojo.dojo = Dojo(dojo_data)
            ninjas.append(ninja_dojo)
        return ninjas