from pony.orm import ObjectNotFound

from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter, DBTextInstance


def __parse_text_instance(dn: str, db_character: DBCharacter) -> int:
    try:
        return int(db_character.get_text(dn, ""))
    except ValueError:
        return 0


def migrate_experience(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    beats = __parse_text_instance("Биты", db_character)
    experience = __parse_text_instance("Опыт", db_character)

    DBTrait(
        dn="Опыт",
        game_object=db_game_object,
        data={
            "dn": "Опыт",
            "type": "Опыт",
            "beats": beats + 5 * experience,
            "spent": 0
        })
