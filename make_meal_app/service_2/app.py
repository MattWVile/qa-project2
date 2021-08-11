from flask import Flask
import random

app = Flask(__name__)

main_dish = ['Pasty', 'Pasta', 'Pasata']

@app.route('/get/main_dish')
def get_main_dish():
    return random.choice(main_dish)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 