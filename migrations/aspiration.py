from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter

def __parse_text_instance(dn: str, db_character: DBCharacter) -> str:
    try:
        return db_character.get_text(dn, "")
    except ValueError:
        return 0

def migrate_aspiration(db_character: DBCharacter, db_game_object: DBGameObject) -> None:

aspiration = __parse_text_instance("Стремление", db_character)

if aspiration: 
    DBTrait(
        dn="Стремление",
        game_object=db_game_object,
        data={
            "dn": uuid.uuid4(),
            "type": "Стремление",
            "value  ": aspiration
        })