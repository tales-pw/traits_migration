from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter

def migrate_aspiration(db_character: DBCharacter, db_game_object: DBGameObject) -> None:

dnArray = ["aspiration_1", "aspiration_2", "aspiration_3", "aspiration_4", "aspiration_5"]

for dn in dnArray:    
    
    aspiration = db_character.get_text(dn, "")

    if aspiration: 
        DBTrait(
            dn="Стремление",
            game_object=db_game_object,
            data={
                "dn": uuid.uuid4(),
                "type": "Стремление",
                "value  ": aspiration
            })