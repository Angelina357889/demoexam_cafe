from src.Models.Shifts import *
from src.Models.Drinks import *
from src.Models.Foods import *
from src.Models.Statuces import *
from src.Models.Tables import *
from src.Models.Base import *


class Orders(Base):
    id = PrimaryKeyField()
    count_cliens = IntegerField()
    table_id = ForeignKeyField(Tables)
    drink_id = ForeignKeyField(Drinks)
    food_id = ForeignKeyField(Foods)
    shift_id = ForeignKeyField(Shifts)
    status_id = ForeignKeyField(Status)

