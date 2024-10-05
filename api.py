from flask import Flask, jsonify

app = Flask(__name__)

# نمونه داده‌های محصولات
products = [
    {
        'id': 1,
        'title': 'محصول 1',
        'price': 100000,
        'image': 'https://dkstatics-public.digikala.com/digikala-products/be908c704a2e73e620bcb59e1c1c51bdf023c7d4_1727594405.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/format,webp/quality,q_90'
    },
    {
        'id': 2,
        'title': 'محصول 2',
        'price': 200000,
        'image': 'https://dkstatics-public.digikala.com/digikala-products/be908c704a2e73e620bcb59e1c1c51bdf023c7d4_1727594405.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/format,webp/quality,q_90'
    },
    {
        'id': 3,
        'title': 'محصول 3',
        'price': 300000,
        'image': 'https://dkstatics-public.digikala.com/digikala-products/be908c704a2e73e620bcb59e1c1c51bdf023c7d4_1727594405.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/format,webp/quality,q_90'
    },
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
