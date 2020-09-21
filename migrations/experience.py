from pony.orm import ObjectNotFound

from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter, DBTextInstance


def __parse_text_instance(dn: str, db_character: DBCharacter) -> int:
    try:
        value = DBTextInstance[dn, db_character].value
        return int(value)
    except ObjectNotFound:
        return 0
    except ValueError:
        return 0


def migrate_experience(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="Опыт",
        game_object=db_game_object,
        data={
            "dn": "Опыт",
            "type": "Опыт",
            "beats": __parse_text_instance("Биты", db_character),
            "spent": __parse_text_instance("Опыт", db_character)
        })
