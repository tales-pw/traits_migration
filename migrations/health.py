from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_health(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Здоровье",
        game_object=db_game_object,
        data={
            "dn": "Здоровье",
            "type": "Здоровье",
            "lethal": db_character.get_number("Очки летального урона", 0),
            "bashing": db_character.get_number("Очки легкого урона", 0),
            "aggravated": db_character.get_number("Очки агравированного урона", 0)
        }
    )
