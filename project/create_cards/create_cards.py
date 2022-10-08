import json
import os
import uuid
from datetime import datetime

from flask import Blueprint, render_template, request, redirect

from project.models import db, Cards

create_cards_bp = Blueprint("create_cards", __name__, template_folder="templates")

UPLOAD_FOLDER = os.path.join("img", "cards")


@create_cards_bp.route("/", methods=["GET", "POST"])
@create_cards_bp.route("/create_cards", methods=["GET", "POST"])
def create_cards():
    lst_class_cards = ["Strength", "Intelligence", "Willpower", "Agility", "Endurance", "Netural", "Archer",
                       "Assassin", "Battlemage", "Crusader", "Mage", "Monk", "Scout", "Sorcerer", "Spellsword",
                       "Warrior"]

    type_card = ["Creature", "Action", "Item", "Support"]

    type_creature = ["People", "Orcs", "Elves", "Undead", "Demons", "Water races", "Animals"]

    rare_card = ["Legendary", "Epic", "Rare", "Common"]

    attack_card = [x for x in range(0, 16)]

    mana_card = [x for x in range(0, 21)]

    life_card = [x for x in range(0, 16)]

    mechanics_card = ["Pilfer", "Last Gaps", "Summon"]

    keyword_card = ["Guard", "Ward", "Drain", "Lethal", "Breakthrough", "Charge"]

    default_title_card = ""

    default_description_card = ""

    default_class_card = "Класс карты"

    default_type_card = "Тип карты"

    default_rare_card = "Редкость карты"

    default_attack_card = "Атака"

    default_mana_card = "Манакост"

    default_life_card = "Жизнь"

    if request.method == "POST":
        title_card = request.form["title_card"]

        description_card = request.form["description_card"]

        class_card = request.form["class_card"]

        type_card = request.form["type_card"]

        type_creature = json.dumps(request.form.getlist("type_creature"))

        rare_card = request.form["rare_card"]

        attack_card = request.form["attack_card"]

        mana_card = request.form["mana_card"]

        life_card = request.form["life_card"]

        keyword_card = json.dumps(request.form.getlist("keyword_card"))

        mechanics_card = json.dumps(request.form.getlist("mechanics_card"))

        file = request.files["file"]

        file.filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1].lower()}'

        file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        time_create = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:

            uses_support = request.form["uses_support"]

        except Exception:

            uses_support = ""

        create_cards = Cards(title_card=title_card, description_card=description_card, class_card=class_card,
                             type_card=type_card, rare_card=rare_card, type_creature=type_creature,
                             uses_support=uses_support,
                             attack_card=attack_card,
                             mana_card=mana_card, life_card=life_card, keyword_card=keyword_card,
                             mechanics_card=mechanics_card, img=file.filename, time_create=time_create)

        db.session.add(create_cards)
        db.session.flush()
        db.session.commit()

        query = Cards.query.filter_by(title_card=request.form["title_card"]).first()

        return redirect(f"/update_cards/{query.id}")

    return render_template("create_cards.html", default_title_card=default_title_card,
                           default_description_card=default_description_card, default_class_card=default_class_card,
                           lst_class_cards=lst_class_cards,
                           type_card=type_card,
                           type_creature=type_creature, rare_card=rare_card,
                           attack_card=attack_card, mana_card=mana_card, life_card=life_card, keyword_card=keyword_card,
                           mechanics_card=mechanics_card, default_type_card=default_type_card,
                           default_rare_card=default_rare_card, default_attack_card=default_attack_card,
                           default_mana_card=default_mana_card, default_life_card=default_life_card)


@create_cards_bp.route("/update_cards/<int:cards_id>", methods=["GET", "POST"])
def update_cards(cards_id):
    query = Cards.query.filter_by(id=cards_id).first()

    print(query.img)

    if request.method == "POST":

        try:

            uses_support = request.form["uses_support"]

        except Exception:

            uses_support = ""

        type_creature = json.dumps(request.form.getlist("type_creature"))

        keyword_card = json.dumps(request.form.getlist("keyword_card"))

        mechanics_card = json.dumps(request.form.getlist("mechanics_card"))

        file = request.files["file"]

        if file.filename != "":

            file.filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1].lower()}'

            file_name = file.filename

            file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        else:

            file_name = query.img

        Cards.query.filter_by(id=cards_id).update({Cards.title_card: request.form["title_card"],
                                                   Cards.description_card: request.form["description_card"],
                                                   Cards.class_card: request.form["class_card"],
                                                   Cards.type_card: request.form["type_card"],
                                                   Cards.rare_card: request.form["rare_card"],
                                                   Cards.uses_support: uses_support,
                                                   Cards.type_creature: type_creature,
                                                   Cards.attack_card: request.form["attack_card"],
                                                   Cards.mana_card: request.form["mana_card"],
                                                   Cards.life_card: request.form["life_card"],
                                                   Cards.keyword_card: keyword_card,
                                                   Cards.mechanics_card: mechanics_card,
                                                   Cards.img: file_name
                                                   })

        db.session.flush()
        db.session.commit()

        return redirect(f"/update_cards/{query.id}")

    lst_class_cards = ["Strength", "Intelligence", "Willpower", "Agility", "Endurance", "Netural", "Archer",
                       "Assassin", "Battlemage", "Crusader", "Mage", "Monk", "Scout", "Sorcerer", "Spellsword",
                       "Warrior"]

    type_card = ["Creature", "Action", "Item", "Support"]

    rare_card = ["Legendary", "Epic", "Rare", "Common"]

    attack_card = [x for x in range(0, 16)]

    mana_card = [x for x in range(0, 21)]

    life_card = [x for x in range(0, 16)]

    type_creature = ["People", "Orcs", "Elves", "Undead", "Demons", "Water races", "Animals"]

    keyword_card = ["Guard", "Ward", "Drain", "Lethal", "Breakthrough", "Charge"]

    mechanics_card = ["Pilfer", "Last Gaps", "Summon"]

    return render_template("update_cards.html", default_title_card=query.title_card,
                           default_description_card=query.description_card, default_class_card=query.class_card,
                           lst_class_cards=lst_class_cards,
                           default_type_card=query.type_card, type_card=type_card,
                           default_rare_card=query.rare_card, rare_card=rare_card, default_mana_card=query.mana_card,
                           mana_card=mana_card,
                           default_attack_card=query.attack_card, attack_card=attack_card,
                           default_life_card=query.life_card, life_card=life_card,
                           type_creature=type_creature, data_in_db_type_creature=query.type_creature,
                           keyword_card=keyword_card, data_in_db_keyword_card=query.keyword_card,
                           mechanics_card=mechanics_card, data_in_db_mechanics_card=query.mechanics_card, img=query.img)
