from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_speed(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Скорость",
        game_object=db_game_object,
        data={
            "dn": "Скорость",
            "type": "Скорость"
        }
    )
