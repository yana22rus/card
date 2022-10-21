import json

from flask import Blueprint, render_template
from sqlalchemy import text

from project.models import db

page_filter_bp = Blueprint("page_filter", __name__, template_folder="templates")


@page_filter_bp.route("/cards/<int:cards_id>", methods=["GET", "POST"])
def cards(cards_id):
    sql = text(f'SELECT * FROM Cards WHERE mana_card == {cards_id}')
    result = db.engine.execute(sql)

    data = []

    for x in result:
        data.append({"title": x[1], "description": x[2], "class": x[3], "type_card": x[4],
                     "attack_card": x[8], "mana_card": cards_id, "life_card": x[9]})

    return render_template("page_filter.html", jsonStr=json.dumps(data, sort_keys=False, default=str))
