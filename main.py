# Запускайте меня
from typing import Callable, List

from pony.orm import db_session, select

import configuration
from database.new_db import db as new_db, DBGameObject
from database.old_db import db as old_db, DBCharacter
from migrations.Integrity import migrate_integrity
from migrations.attributes_and_skills import migrate_attributes_and_skills
from migrations.character_info import migrate_character_info
from migrations.experience import migrate_experience
from migrations.health import migrate_health
from migrations.human_template import migrate_human_template
from migrations.merits import migrate_merits
from migrations.merits_custom import migrate_custom_merits

migrations: List[Callable[[DBCharacter, DBGameObject], None]] = [
    # Сюда пишите ваши функции, которые принимают DBCharacter и DBGameObject как аргументы
    migrate_attributes_and_skills,
    migrate_character_info,
    migrate_experience,
    migrate_health,
    migrate_merits,
    migrate_custom_merits,
    migrate_human_template,
    migrate_integrity
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
