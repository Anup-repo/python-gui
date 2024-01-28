import json


class Database:
    def __init__(self):
        pass

    def regsiter(self, name, email, password):
        with open("mydb.json", "r") as rf:
            data = json.load(rf)
        if email in data:
            return 0
        else:
            data[email] = [name, password]
            with open("mydb.json", "w") as wf:
                json.dump(data, wf)
            return 1

    def login(self, email, password):
        with open("mydb.json", "r") as f:
            data = json.load(f)
            if email in data:
                if data[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
