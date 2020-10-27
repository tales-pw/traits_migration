from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_defence(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Защита",
        game_object=db_game_object,
        data={
            "dn": "Защита",
            "type": "Защита"
        }
    )
