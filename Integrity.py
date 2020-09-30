from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter

def migrate_integrity(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Целостность",
        game_object=db_game_object,
        data={
            "dn": "Целостность",
            "type": "Целостность",
            "points": db_character.get_number("Целостность", 7)
        })