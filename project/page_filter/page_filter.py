from flask import Blueprint,render_template,redirect,request

from project.models import db, Cards
from sqlalchemy import text

page_filter_bp = Blueprint("page_filter", __name__, template_folder="templates")


@page_filter_bp.route("/cards/<int:cards_id>", methods=["GET", "POST"])
def cards(cards_id):
    query = Cards.query.filter_by(id=cards_id).first()

    sql = text(f'select img from Cards where mana_card == {cards_id}')
    result = db.engine.execute(sql)
    img = [row[0] for row in result]
    print(img)


    return render_template("page_filter.html",lst=[x for x in range(1,11)],img=img)
