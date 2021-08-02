from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'main_dish': {
        'Sausage': 1.99,
        'Pie': 3.99,
        'Pizza': 4.99
    },
    'side_dish':{
        'Chips': 1.05
        'Garlic bread': 1.50
        'Mashed potato': 1.99
    }
}

@app.route('/post/meal', methods=['POST'])
def post_meal():
    main = request.json['main_dish']
    side = request.json['side_dish']
    price = prices['main_dish'][main] + prices['side_dish'][side]
    return jsonify(price)

if __name__ == '__main__':
    app.run(host='0.0.0.0') 