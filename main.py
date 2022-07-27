from fastapi import FastAPI
# from email_validator import  validate_email, EmailNotValidError
from config.db import con
# from schemas.users import User
# from models.users import users


app=FastAPI();    #creating object for FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World Ashok to Heroku"}

# @app.get('/api/users')                                  #used to fetch data from my sql
# async def index():                                      #asynchronous function
#     data=con.execute(users.select()).fetchall()         #quey statement to fetch data from mysql
#     return data                                         #returning the state of object
#
# @app.post('/api/users')
# async def store(obj:User):
#
#        data=con.execute(users.select().where (users.c.email == obj.email)).fetchall()
#        #condition to check whether the email present in mysql already
#
#        val_email = obj.email
#
#        try:
#            val_email=validate_email(val_email).email
#        except EmailNotValidError as e:
#            return "Please enter valid Email! :("
#
#        if  (data.__len__()==0): #check_email is a function used to validate email
#         data=con.execute(users.insert().values(
#         name=obj.name,
#         age=obj.age,                        #query to insert data in the database
#         email=obj.email
#         ))
#         data=con.execute(users.select()).fetchall()
#         return data
#        else:
#            return "Email already in use!!! :("
#
#
# @app.put('/api/users/{id}')
# async def func_to_update(id:int,obj:User):   #asynchronous function to update the date to my sql
#
#     data = con.execute(users.select().where(users.c.email == obj.email)).fetchall() #refer the above statement
#
#     val_email = obj.email
#
#     try:
#         val_email = validate_email(val_email).email
#     except EmailNotValidError as e:
#         return "Please enter valid Email! :("
#
#
#     if (data.__len__() == 0):
#
#         data=con.execute(users.update().values(
#         name=obj.name,
#         age=obj.age,
#         email=obj.email,
#         ).where(users.c.id == id))
#         data = con.execute(users.select()).fetchall()
#         return data
#
#     else :
#         return "Email in use!!"
#
#
# @app.delete('/api/users/{id}')             #asynchronous function to delete the data from the database
# async def delete(id:int):
#     data=con.execute(users.delete().where(users.c.id==id))
#     data = con.execute(users.select()).fetchall()
#     return data
