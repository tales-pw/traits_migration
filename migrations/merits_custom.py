from pony.orm import select

from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter, DBMeritInstance


def migrate_custom_merits(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    for merit in select(m for m in DBMeritInstance if m.merit_dn is None and m.character == db_character):
        merit: DBMeritInstance

        DBTrait(
            dn=merit.dn,
            game_object=db_game_object,
            data={
                "dn": merit.dn,
                "type": "Custom_Merit",
                "customName": merit.title,
                "value": merit.value
            }
        )
