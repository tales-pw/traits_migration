from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_initiative_mod(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Модификатор_Инициативы",
        game_object=db_game_object,
        data={
            "dn": "Модификатор_Инициативы",
            "type": "Модификатор_Инициативы"
        })
