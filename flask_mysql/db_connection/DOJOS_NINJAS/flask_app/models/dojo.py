from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.datecreated = data["datecreated"]
        self.dateupdated = data["dateupdated"]
        self.ninjas = []
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,datecreated,dateupdated)  VALUES (%(name)s,NOW(),NOW())"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
    @classmethod
    def getall(cls):
        query = "SELECT * FROM dojos"
        dojos_from_db = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for i in dojos_from_db:
            dojos.append(cls(i))
        return dojos
    @classmethod
    def dojoinfo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'date_created': row['date_created'],
                'date_updated': row['date_updated']
                }
            dojo.ninjas.append(Ninja(n))
        return dojo