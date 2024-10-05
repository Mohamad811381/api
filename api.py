from flask import Flask, jsonify

app = Flask(__name__)

# نمونه داده‌های محصولات
products = [
    {
        'id': 1,
        'title': 'محصول 1',
        'price': 100000,
        'image': 'https://example.com/image1.jpg'
    },
    {
        'id': 2,
        'title': 'محصول 2',
        'price': 200000,
        'image': 'https://example.com/image2.jpg'
    },
    {
        'id': 3,
        'title': 'محصول 3',
        'price': 300000,
        'image': 'https://example.com/image3.jpg'
    },
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
