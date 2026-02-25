from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://djcarbajal_db_user:dCgHo9EcZ8fbf2OR@cluster0.qupfqm3.mongodb.net/?appName=Cluster0")

db = client["grocery_db"]
collection = db["items"]

@app.route("/")
def index():
    items = list(collection.find())
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    item_name = request.form.get("item")
    quantity = request.form.get("quantity")

    if item_name and quantity:
        collection.insert_one({
            "name": item_name,
            "quantity": int(quantity)
        })

    return redirect("/")

@app.route("/delete/<item_id>", methods=["POST"])
def delete_item(item_id):
    collection.delete_one({"_id": ObjectId(item_id)})
    return redirect("/")

@app.route("/update/<item_id>", methods=["POST"])
def update_quantity(item_id):
    new_quantity = request.form.get("quantity")
    if new_quantity:
        collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": {"quantity": int(new_quantity)}}
        )
    return redirect("/")

app.run(host="0.0.0.0", port=5050)