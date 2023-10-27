client_records = {
            "Ming": {'name': 'Ming', 'data': '2023/9/13'},
            "Ruijia": {'name': 'Ruijia', 'data': '2023/10/13'},
            "Axel": {'name': 'Axel', 'data': '2023/1/13'},
            "Parker": {'name': 'Parker', 'data': '2022/10/17'},
            "John": {'name': 'John', 'data': '2021/11/16'},
            "Yang": {'name': 'Yang', 'data': '2020/5/19'},
        }

class Client_record:
    def __init__(self):
        self.init()

    def init(self):
        history_list = {
            "Ming": {'name': 'Ming', 'data': '2023/9/13'},
            "Ruijia": {'name': 'Ruijia', 'data': '2023/10/13'},
            "Axel": {'name': 'Axel', 'data': '2023/1/13'},
            "Parker": {'name': 'Parker', 'data': '2022/10/17'},
            "John": {'name': 'John', 'data': '2021/11/16'},
            "Yang": {'name': 'Yang', 'data': '2020/5/19'},
        }
        self.list = history_list

    def get_client_records(self):
        return self.list

    def add_client_records(self, client_record):
        self.list[client_record['name']] = client_record

    def delete_client_records(self, client_record):
        self.list = self.list.pop(client_record['name'])



