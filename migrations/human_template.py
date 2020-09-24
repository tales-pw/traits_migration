from database.new_db import DBGameObject, DBTrait
from database.old_db import DBCharacter


def migrate_human_template(db_character: DBCharacter, db_game_object: DBGameObject) -> None:
    DBTrait(
        dn="human",
        game_object=db_game_object,
        data={"dn": "human", "type": "human",
              "createdTraits": ["Интеллект", "Смекалка", "Концентрация", "Сила", "Ловкость", "Выносливость",
                                "Харизма", "Манипулирование", "Хладнокровие", "Эрудиция", "Загадки", "Ремесло",
                                "Расследование", "Медицина", "Оккультизм", "Политика", "Наука", "Атлетика",
                                "Борьба", "Верховая езда", "Стрельба", "Кража", "Скрытность", "Выживание",
                                "Холодное оружие", "Знание_животных", "Эмпатия", "Самовыражение", "Запугивание",
                                "Убеждение", "Социализация", "Знание улиц", "Обман", "Защита", "Здоровье",
                                "Модификатор_Инициативы", "Целостность", "Размер", "Скорость", "Сила_воли",
                                "Богатство", "weapon", "armor", "position", "Name", "Age", "Player", "Race",
                                "Nation", "Language", "Добродетель", "Порок", "Концепт"]}
    )
