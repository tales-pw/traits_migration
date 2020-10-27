from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_weapon(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="weapon",
        game_object=db_game_object,
        data={
            "dn": "weapon",
            "type": "weapon"
        }
    )
