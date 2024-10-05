from src.Models.Statuces import *

class StatusController():
    def get(self):
        return Status.select()

if __name__ == "__main__":
    status = StatusController()

    for row in status.get():
        print(row.name)
