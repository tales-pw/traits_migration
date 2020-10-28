from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter

trait_old_new_relation = {
    "Эрудиция": "Эрудиция",
    "Эмпатия": "Эмпатия",
    "Холодное оружие": "Холодное оружие",
    "Хладнокровие": "Хладнокровие",
    "Харизма": "Харизма",
    "Убеждение": "Убеждение",
    "Стрельба": "Стрельба",
    "Смекалка": "Смекалка",
    "Скрытность": "Скрытность",
    "Сила": "Сила",
    "Самовыражение": "Самовыражение",
    "Ремесло": "Ремесло",
    "Расследование": "Расследование",
    "Политика": "Политика",
    "Оккультизм": "Оккультизм",
    "Обман": "Обман",
    "Наука": "Наука",
    "Медицина": "Медицина",
    "Манипулирование": "Манипулирование",
    "Ловкость": "Ловкость",
    "Кража": "Кража",
    "Концентрация": "Концентрация",
    "Интеллект": "Интеллект",
    "Знание животных": "Знание_животных",
    "Знание улиц": "Знание улиц",
    "Запугивание": "Запугивание",
    "Загадки": "Загадки",
    "Выносливость": "Выносливость",
    "Выживание": "Выживание",
    "Верховая езда": "Верховая езда",
    "Борьба": "Борьба",
    "Атлетика": "Атлетика",
    "Социализация": "Социализация"
}

ATTRIBUTES = {"Интеллект", "Концентрация", "Смекалка", "Выносливость", "Ловкость", "Сила", "Манипулирование", "Харизма",
              "Хладнокровие"}


def migrate_attributes_and_skills(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    for old_dn, new_type in trait_old_new_relation.items():
        DBTrait(
            dn=new_type,
            game_object=db_game_object,
            data={
                "dn": new_type,
                "type": new_type,
                "value": db_character.get_number(old_dn, 1 if old_dn in ATTRIBUTES else 0)
            }
        )
