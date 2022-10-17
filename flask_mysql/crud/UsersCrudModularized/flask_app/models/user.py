from flask_app.config.mysqlconnection import connectToMySQL
class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.createdat = data["createdat"]
        self.updatedat = data["updatedat"]
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
        return connectToMySQL("users_schema").query_db(query,data)
    @classmethod
    def getall(cls):
        query = "SELECT * FROM users"
        users_from_db = connectToMySQL("users_schema").query_db(query)
        users = []
        for i in users_from_db:
            users.append(cls(i))
        return users
    @classmethod
    def userinfo(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query,data)
        if results:
            return cls(results[0])
    @classmethod
    def deleteuser(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL("users_schema").query_db(query,data)
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updatedat = NOW() WHERE id = %(id)s" 
        return connectToMySQL("users_schema").query_db(query,data)
