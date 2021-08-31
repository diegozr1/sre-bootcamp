import pymysql, os
    
db_host     = os.getenv("db_host")
db_user     = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name     = os.getenv("db_name")

def get_connection():
    return pymysql.connect(host     = db_host,
                           user     = db_user,
                           password = db_password,
                           db       = db_name)