from . import app, db
from .models import Make_meal

@app.route('/')
def home():
    main_dish = requests.get('http://service-2:5000/get/main_dish').text
    side_dish = requests.get('http://service-2:5000/get/side_dish').text
    get_total = {'main_dish': main_dish, 'side_dish':side_dish}
    total = requests.post('http://service-4:5000/post/meal', json=get_total).json()
    meal = Make_meal(main_dish=main_dish, side_dish=side_dish, price=total)
    db.session.add(meal)
    db.commit()