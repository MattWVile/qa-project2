from . import db

class Make_meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_dish = db.Column(db.String(30), nullable=False)
    side_dish = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer)