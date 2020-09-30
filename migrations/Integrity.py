from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def __parse_text_instance(dn: str, db_character: DBCharacter) -> int:
    try:
        return int(db_character.get_text(dn, ""))
    except ValueError:
        return 0


def migrate_integrity(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    Integrity = __parse_text_instance("Целостность", db_character)

    DBTrait(
        dn="Опыт",
        game_object=db_game_object,
        data={
            "dn": "Целостность",
            "type": "Целостность",
            "points": Integrity
        })
