from project import db


class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_card = db.Column(db.String, unique=True)
    description_card = db.Column(db.String, unique=True)
    class_card = db.Column(db.String)
    type_card = db.Column(db.String)
    type_creature = db.Column(db.String)
    rare_card = db.Column(db.String)
    uses_support = db.Column(db.String)
    attack_card = db.Column(db.INTEGER)
    mana_card = db.Column(db.INTEGER)
    life_card = db.Column(db.INTEGER)
    keyword_card = db.Column(db.String)
    mechanics_card = db.Column(db.String)
    img = db.Column(db.String)
    time_create = db.Column(db.String)
