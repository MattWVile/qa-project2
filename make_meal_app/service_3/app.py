from flask import Flask
import random

app = Flask(__name__)

side_dish = ['Chips', 'Garlic bread', 'Mashed potato']

@app.route('/get/side_dish')
def get_side_dish():
    return random.choice(side_dish)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 