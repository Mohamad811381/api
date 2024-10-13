from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Product A",
        "price": 10.0,
        "description": "This is a description for Product A.",
        "image_url": "https://example.com/images/product_a.jpg"
    },
    {
        "id": 2,
        "name": "Product B",
        "price": 15.0,
        "description": "This is a description for Product B.",
        "image_url": "https://example.com/images/product_b.jpg"
    },
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
