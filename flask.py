from flask import Flask, jsonify, request

app = Flask(__name__)

# لیست اولیه غذاها
foods = [
    {"id": 1, "title": "چلو کباب", "price": 50000, "description": "یک غذای خوشمزه و سنتی", "image": "https://github.com/Expensify/App/blob/main/assets/images/simple-illustrations/simple-illustration__track-shoe.svg"},
    {"id": 2, "title": "کباب", "price": 40000, "description": "کباب مخصوص", "image": "https://github.com/Expensify/App/blob/main/assets/images/simple-illustrations/simple-illustration__track-shoe.svg"}
]

@app.route('/api/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

@app.route('/api/foods', methods=['POST'])
def add_food():
    new_food = request.json
    foods.append(new_food)
    return jsonify(new_food), 201

@app.route('/api/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    global foods
    foods = [food for food in foods if food['id'] != food_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
