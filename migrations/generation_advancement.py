from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_generation_advancement(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="generation_advancement",
        game_object=db_game_object,
        data={
            "dn": "generation_advancement",
            "type": "generation_advancement"
        }
    )
