from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_wealth(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Богатство",
        game_object=db_game_object,
        data={
            "dn": "Богатство",
            "type": "Богатство",
            "points": db_character.get_number("Богатство", 0)
        }
    )
