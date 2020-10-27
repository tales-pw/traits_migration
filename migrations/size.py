from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_size(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Размер",
        game_object=db_game_object,
        data={
            "dn": "Размер",
            "type": "Размер"
        }
    )
