from src.Models.Document import *

class DocumentController():
    def get(self):
        return Document.select().execute()

    def add(self, date, user_id, statement_id):
        Document.create(date=date, user_id=user_id, statement_id=statement_id)


if __name__ == "__main__":
    dt = DocumentController()
    dt.add('21.12.2112', '1','1')