from datetime import datetime

from pony.orm import Database, PrimaryKey, Required, Set, Json

db = Database()


class DBGameObject(db.Entity):
    dn: str = PrimaryKey(str)
    version: datetime = Required(datetime, default=datetime.utcnow())

    traits = Set(lambda: DBTrait)


class DBTrait(db.Entity):
    dn: str = Required(str)
    data = Required(Json)

    game_object: DBGameObject = Required(DBGameObject)

    PrimaryKey(dn, game_object)
