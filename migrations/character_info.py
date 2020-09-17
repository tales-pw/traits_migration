from pony.orm import ObjectNotFound

from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter, DBTextInstance

__old_new_relation = {
    "Порок": "Порок",
    "Концепт": "Концепт",
    "Добродетель": "Добродетель",
    "Race": "Раса",
    "Player": "Игрок",
    "Nation": "Народ",
    "Name": "Имя",
    "Language": "Язык",
    "Age": "Возраст"
}


def migrate_character_info(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    for old_dn, new_type in __old_new_relation.items():
        try:
            value = DBTextInstance[old_dn, db_character].value
        except ObjectNotFound:
            value = ""

        DBTrait(
            dn=new_type,
            game_object=db_game_object,
            data={
                "dn": new_type,
                "type": new_type,
                "value": value
            }
        )
