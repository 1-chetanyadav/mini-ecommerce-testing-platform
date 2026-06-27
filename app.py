from flask import Flask
from flask import request
from flask import render_template
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

@app.route("/login-ui", methods=["GET","POST"])
def login_ui():
    if request.method=="GET":
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")
    # print(username,password)
    response,status = validate_login(username,password)

    print(response)
    return render_template("login.html",message = response["message"])

def home():
    # with open("data/users.json",'r') as userfile:
    #     users = json.load(userfile)
        # print(users)
    username2 = request.args.get("name","Flask")
    return f"Hello, {escape(username2)}!"

@app.route("/login", methods=["POST"])
def server_login_api():
    # for debug
    # users = json.load(userfile)
    #login data
    
    data = request.get_json()
    # print(">> In server API")
    if data is None:
        return {
            "message":"Login Field Empty"
        },401
    login_username = data.get("username")
    login_password = data.get("password")
    return validate_login(login_username,login_password)
    
def validate_login(login_username,login_password):
    # print(">> in validate login",login_username,login_password)
    users=load_users()
    if users is None:
        return {
            "message":"User list empty"
        },401
    if not login_username:
        return {"message":"Missing Username"},400
    if not login_password:
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



    # return login_username,login_password
    

@app.route("/order", methods=["POST"])

def server_order():
    products = load_products()
    data = request.get_json()
    buy_user = data.get("username")
    product_price = 0
    
    
    for product in products:
        if product.get("product_id")==data.get("product_id"):
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

@app.route("/products",methods=["POST"])
def product():
    
    data = request.get_json()
    # print(data)
    if data is None:
        return {"message":"Search Field Empty"},401
    product_id = data.get("product_id")
    # print(product_id)
    return validate_product(product_id)
    
    

@app.route("/product-ui",methods=["GET","POST"])
def product_ui():
    if request.method=="GET":
        return render_template("product.html")
    product_id = request.form.get("product_id") 
    
    response,status = validate_product(product_id)
    return render_template("product.html",message = response["message"])


def validate_product(product_id):
    products = load_products()
    for product in products:
        if product.get("product_id") == int(product_id):
            # print(product.get("product_id"), product_id)
            return {"message":"Match Found"},200
        
        print(product.get("product_id"), product_id)
    else:
        return {"message":"No Match Found"},400
    
    
if __name__ == "__main__":
    app.run(debug=True)

    

