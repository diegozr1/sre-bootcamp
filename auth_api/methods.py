# These functions need to be implemented
from database import get_connection

import jwt, os
import logging, hashlib

from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidSignatureError

class Token:

    def generate_token(self, username, password):
        
        db = get_connection()
        db_users_query = "SELECT password, salt, role FROM users WHERE username = %s"
       
        with db.cursor() as cursor:
            cursor.execute(db_users_query, (username,))
            user = cursor.fetchone()
        
        db.close()
        
        if user is not None:
            user_password = user[0]
            user_salt     = user[1]
            user_role     = user[2]
        else:
            return "Forbidden"
        
        hashed = hashlib.sha512(
                str(password + user_salt).encode("utf-8")
            ).hexdigest()
        
        if hashed != user_password:
            return "Forbidden"
        
        return jwt.encode( {"role": user_role}, os.getenv("db_secret"), algorithm="HS512")
        

class Restricted:

    def access_data(self, authorization):
        try:
            
            authorization_token = str.replace( str(authorization), "Bearer ", "")
            
            jwt.decode(authorization_token, os.getenv("db_secret"), algorithms=["HS512"])
            
            return "You are under protected data"
            
            
        except jwt.DecodeError:
            return "Forbidden"
        except jwt.InvalidTokenError:
            return "Forbidden"
        except jwt.ExpiredSignatureError:
            return "Forbidden"
        except jwt.InvalidSignatureError:
            return "Forbidden"