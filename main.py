# Запускайте меня
from typing import Callable, List

from pony.orm import db_session, select

import configuration
from database.new_db import db as new_db, DBGameObject
from database.old_db import db as old_db, DBCharacter
from migrations.armor import migrate_armor
from migrations.aspiration import migrate_aspiration
from migrations.attributes_and_skills import migrate_attributes_and_skills
from migrations.character_info import migrate_character_info
from migrations.defence import migrate_defence
from migrations.experience import migrate_experience
from migrations.generation_advancement import migrate_generation_advancement
from migrations.health import migrate_health
from migrations.human_template import migrate_human_template
from migrations.initiative_mod import migrate_initiative_mod
from migrations.integrity import migrate_integrity
from migrations.merits import migrate_merits
from migrations.merits_custom import migrate_custom_merits
from migrations.player_character import migrate_player_character
from migrations.position import migrate_position
from migrations.size import migrate_size
from migrations.speciality import migrate_specialities
from migrations.speed import migrate_speed
from migrations.wealth import migrate_wealth
from migrations.weapon import migrate_weapon
from migrations.willpower import migrate_willpower

migrations: List[Callable[[DBCharacter, DBGameObject], None]] = [
    # Сюда пишите ваши функции, которые принимают DBCharacter и DBGameObject как аргументы
    migrate_attributes_and_skills,
    migrate_character_info,
    migrate_experience,
    migrate_health,
    migrate_merits,
    migrate_custom_merits,
    migrate_human_template,
    migrate_integrity,
    migrate_aspiration,
    migrate_initiative_mod,
    migrate_defence,
    migrate_wealth,
    migrate_weapon,
    migrate_position,
    migrate_player_character,
    migrate_armor,
    migrate_willpower,
    migrate_speed,
    migrate_size,
    migrate_specialities,
    migrate_generation_advancement
]


@db_session
def migrate():
    for db_character in select(a for a in DBCharacter):
        db_character: DBCharacter
        db_game_object = DBGameObject(
            dn=db_character.name,
            version=db_character.updated
        )

        for migration in migrations:
            migration(db_character, db_game_object)


def main():
    old_db.bind(**configuration.OLD_DB_CONF)
    old_db.generate_mapping(create_tables=True)

    new_db.bind(**configuration.NEW_DB_CONF)
    new_db.generate_mapping(create_tables=True)

    migrate()


if __name__ == '__main__':
    main()
