from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter

__old_new_relation = {
    "Порок": "Порок",
    "Концепт": "Концепт",
    "Добродетель": "Добродетель",
    "Раса": "Race",
    "Игрок": "Player",
    "Народ": "Nation",
    "Имя": "Name",
    "Язык": "Language",
    "Возраст": "Age"
}


def migrate_character_info(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    for old_dn, new_type in __old_new_relation.items():
        DBTrait(
            dn=new_type,
            game_object=db_game_object,
            data={
                "dn": new_type,
                "type": new_type,
                "value": db_character.get_text(old_dn, "")
            }
        )
