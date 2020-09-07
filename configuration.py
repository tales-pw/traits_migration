import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

OLD_DB_CONF = {'provider': 'sqlite', 'filename': os.path.join(ROOT_DIR, "old_database.sqlite"), 'create_db': True}
NEW_DB_CONF = {'provider': 'sqlite', 'filename': os.path.join(ROOT_DIR, "new_database.sqlite"), 'create_db': True}
