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

def load_products():
    with open("data/product.json",'r') as productfile:
            products =json.load(productfile)
            return products

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

@app.route("/products", methods=["POST"])

def server_products():
    products = load_products()
    data = request.get_json()
    buy_user = data.get("username")
    product_price = 0
    
    
    for product in products:
        if product.get("productid")==data.get("product_id"):
            product_price = product.get("price")
            break
            
    users = load_users()
    print("Buy User:", buy_user)

    for user in users:
        if user.get("username") == buy_user:
            wallet_money = user.get("wallet")
            break

    print("Wallet:", wallet_money)
    if wallet_money>=product_price:
        return {"Message":"Purchase Success"},200
    else:
        return{"Message":"Purchase Failed"},400
    
if __name__ == "__main__":
    app.run(debug=True)
    

