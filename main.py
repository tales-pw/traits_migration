from typing import Callable, List

from pony.orm import db_session

import configuration
from database.new_db import db as new_db, DBGameObject
from database.old_db import db as old_db, DBCharacter

migrations: List[Callable[[DBGameObject, DBCharacter], None]] = [

]


@db_session
def migrate():
    for db_character in DBCharacter.select():
        db_character: DBCharacter
        db_game_object = DBGameObject(
            dn=db_character.name,
            version=db_character.updated
        )

        for migration in migrations:
            migration(db_game_object, db_character)


def main():
    old_db.bind(**configuration.OLD_DB_CONF)
    old_db.generate_mapping(create_tables=True)

    new_db.bind(**configuration.NEW_DB_CONF)
    new_db.generate_mapping(create_tables=True)

    migrate()


if __name__ == '__main__':
    main()
