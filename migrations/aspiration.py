import uuid

from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter

dns = ["aspiration_1", "aspiration_2", "aspiration_3", "aspiration_4", "aspiration_5"]


def migrate_aspiration(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    for dn in dns:
        aspiration = db_character.get_text(dn, "")

        if aspiration:
            dn = str(uuid.uuid4())
            DBTrait(
                dn=dn,
                game_object=db_game_object,
                data={
                    "dn": dn,
                    "type": "Стремление",
                    "value": aspiration
                })
