from os.path import dirname, join
from uuid import uuid4
import requests
import pytest

HOST = "http://127.0.0.1:5000"


def create(class_card="Strength", type_card="Creature", type_creature="People", rare_card="Legendary", mana_card="1",
           attack_card="1", life_card="1", keyword_card="Guard", mechanics_card="Pilfer", **kwargs):
    title = uuid4()

    description_card = uuid4()

    script_dir = dirname(__file__)

    rel_path = join("files", "png.png")

    abs_file_path = join(script_dir, rel_path)

    with open(abs_file_path, "rb") as f:
        file = f.read()

    files = {"file": file}

    payload = {

        "title_card": title,
        "description_card": description_card,
        "class_card": class_card,
        "type_card": type_card,
        "type_creature": type_creature,
        "rare_card": rare_card,
        "mana_card": mana_card,
        "attack_card": attack_card,
        "life_card": life_card,
        "keyword_card": keyword_card,
        "mechanics_card": mechanics_card,

    }

    assert "update_cards" in requests.post(HOST, files=files, data=payload).url
