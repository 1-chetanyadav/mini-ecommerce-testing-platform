from flask import Flask
from flask import request
from markupsafe import escape
import requests
import json

app = Flask(__name__)

def load_users():

    with open("data/users.json",'r') as userfile:
        users = json.load(userfile)   
    return users

@app.route("/")
def home():
    # with open("data/users.json",'r') as userfile:
    #     users = json.load(userfile)
        # print(users)
    username2 = request.args.get("name","Flask")
    return f"Hello, {escape(username2)}!"

@app.route("/login", methods=["POST"])

def server_login():
    # for debug
    # users = json.load(userfile)
    #login data
    users=load_users()
    data = request.get_json()
    if data is None:
        return {
            "message":"User list empty"
        },401
    login_username = data.get("username")
    login_password = data.get("password")
    
    if login_username=="":
        return {"message":"Missing Username"},400
    if login_password=="":
        return {"message":"Missing Password"},400

    for user in users:
        if user.get("username")==login_username and user.get("password")!=login_password:
            return {
                "message": "Incorrect Password"
            },401
        elif user.get("username")!=login_username and user.get("password")==login_password:
            return {
                "message": "Incorrect Username"
            },401
        
        elif user.get("username")==login_username and user.get("password")==login_password:
            return {
                "message": "Login Success"
            },200
    return {
        "message": "Incorrect Username and Password"
        },401


if __name__ == "__main__":
    app.run(debug=True)
    

