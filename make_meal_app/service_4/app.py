from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'main_dish': {
        'Sausage': 2,
        'Pie': 3,
        'Burger': 4
    },
    'side_dish': {
        'Jacket potato': 1,
        'French fries': 2,
        'Spicy rice': 3
    }
}

@app.route('/post/meal', methods=['POST'])
def post_meal():
    main = request.json['main_dish']
    side = request.json['side_dish']
    price = prices['main_dish'][main] + prices['side_dish'][side]
    
    return jsonify(price)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
    