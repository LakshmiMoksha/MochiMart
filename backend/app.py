from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


products = [
    {"id": 1, "name": "Fluffy Sweater", "price": 799},
    {"id": 2, "name": "Cute Skirt", "price": 599},
    {"id": 3, "name": "Cozy Hoodie", "price": 999},
]

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
