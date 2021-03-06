from pony.orm import select

from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter, DBSpecialityInstance
from migrations.attributes_and_skills import trait_old_new_relation


def migrate_specialities(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    for speciality in select(s for s in DBSpecialityInstance if s.character == db_character):
        speciality: DBSpecialityInstance

        DBTrait(
            dn=speciality.dn,
            game_object=db_game_object,
            data={
                "dn": speciality.dn,
                "type": "Специализация",
                "name": speciality.value,
                "skill": trait_old_new_relation.get(speciality.trait_dn)
            }
        )
