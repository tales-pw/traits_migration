from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_willpower(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Сила_воли",
        game_object=db_game_object,
        data={
            "dn": "Сила_воли",
            "type": "Сила_воли",
            "points": None
        }
    )
