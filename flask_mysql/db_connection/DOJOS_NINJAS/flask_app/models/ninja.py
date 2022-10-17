from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.date_created = data["date_created"]
        self.date_updated = data["date_updated"] 
        #Foreign key doesn't need to be included in the initialization
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,date_created,date_updated,dojo_id)  VALUES (%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW(),%(dojo_id)s)"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
    @classmethod
    def getall(cls):
        query = "SELECT * FROM ninjas"
        ninjas_from_db = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        ninjas = []
        for i in ninjas_from_db:
            ninjas.append(cls(i))
        return ninjas