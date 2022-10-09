import pytest

from testing.utilities.create import create


def test_create():
    create()


@pytest.mark.parametrize('value', ["Strength", "Intelligence", "Willpower", "Agility", "Endurance", "Netural", "Archer",
                                   "Assassin", "Battlemage", "Crusader", "Mage", "Monk", "Scout", "Sorcerer",
                                   "Spellsword",
                                   "Warrior"])
def test_check_class_card(value):
    create(class_card=value)


@pytest.mark.parametrize('value', ["Creature", "Action", "Item"])
def test_check_type_card(value):
    create(type_card=value)


@pytest.mark.parametrize('value', ["People", "Orcs", "Elves", "Undead", "Demons", "Water races", "Animals"])
def test_check_type_creature(value):
    create(type_creature=value)


@pytest.mark.parametrize('value', ["People", "Orcs", "Elves", "Undead", "Demons", "Water races", "Animals"])
def test_check_rare_card(value):
    create(rare_card=value)


@pytest.mark.parametrize('value', [x for x in range(0, 16)])
def test_check_attack_card(value):
    create(attack_card=value)


@pytest.mark.parametrize('value', [x for x in range(0, 16)])
def test_check_mana_card(value):
    create(mana_card=value)


@pytest.mark.parametrize('value', [x for x in range(0, 16)])
def test_check_life_card(value):
    create(life_card=value)


@pytest.mark.parametrize('value', ["Pilfer", "Last Gaps", "Summon"])
def test_check_mechanics_card(value):
    create(mechanics_card=value)


@pytest.mark.parametrize('value', ["Guard", "Ward", "Drain", "Lethal", "Breakthrough", "Charge"])
def test_check_keyword_card(value):
    create(keyword_card=value)
