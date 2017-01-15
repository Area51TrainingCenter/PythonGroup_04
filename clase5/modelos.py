from pony.orm import *

db = Database()


class Tarea(db.Entity):
    nombre = Required(str)


sql_debug(True)
db.bind('sqlite', 'db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
