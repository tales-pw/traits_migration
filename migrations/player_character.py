from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_player_character(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="player_character",
        game_object=db_game_object,
        data={"dn": "player_character", "type": "player_character", "createdTraits": ["Опыт"]}
    )
