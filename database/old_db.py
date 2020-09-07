import datetime

from pony.orm import Database, ObjectNotFound, Optional, PrimaryKey, Required, Set, db_session

db = Database()


class DBCharacter(db.Entity):
    name: str = PrimaryKey(str)
    updated: datetime.datetime = Required(datetime.datetime, default=datetime.datetime.utcnow)

    texts = Set(lambda: DBTextInstance)
    traits = Set(lambda: DBTraitInstance)
    specialities = Set(lambda: DBSpecialityInstance)


class DBTraitInstance(db.Entity):
    dn: str = Required(str)
    value: int = Required(int)

    character: DBCharacter = Required(DBCharacter)

    PrimaryKey(dn, character)


class DBSpecialityInstance(db.Entity):
    dn: str = Required(str)
    value: str = Optional(str, default="")

    trait_dn: str = Required(str)
    character: DBCharacter = Required(DBCharacter)

    PrimaryKey(dn, trait_dn, character)


class DBMeritInstance(DBTraitInstance):
    merit_dn: str = Optional(str)
    title: str = Optional(str)


class DBTextInstance(db.Entity):
    dn: str = Required(str)
    value: str = Required(str)

    character: DBCharacter = Required(DBCharacter)

    PrimaryKey(dn, character)
