from flask import Flask
import random

app = Flask(__name__)

side_dish = ['Jacket potato', 'French fries', 'Spicy rice']

@app.route('/get/side_dish')
def get_side_dish():
    return random.choice(side_dish)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 