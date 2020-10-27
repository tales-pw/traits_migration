from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_armor(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="armor",
        game_object=db_game_object,
        data={
            "dn": "armor",
            "type": "armor"
        }
    )
