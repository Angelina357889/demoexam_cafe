
from src.Models.Statements import *

class StatementController():
    @classmethod
    def get(cls):
        return Statements.select().execute()

    @classmethod
    def add(cls, name, sample, document_type):
        Statements.create(name=name, sample=sample, document_type=document_type)

    @classmethod
    def select_s(cls):
        if Statements.document_type == 1:
            return Statements.select().where(Statements.document_type ==1).execute()
        else:
            return Statements.select().where(Statements.document_type == 2).execute()



if __name__ == "__main__":
    stcl = StatementController()
    # stcl.add('Заявляю', "Хочу спать!", "1")
    print(stcl.select_s())
