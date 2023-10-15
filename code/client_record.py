class Client_record:
    def __init__(self):
        self.init()

    def init(self):
        history_list = {
            "Ming": {'name': 'Ming', 'data': '2023/9/13'},
            "Ruijia": {'name': 'Ruijia', 'data': '2023/10/13'},
        }
        self.list = history_list

    def get_client_records(self):
        return self.list

    def add_client_records(self, client_record):
        self.list[client_record['name']] = client_record

    def delete_client_records(self,client_record):
        self.list = self.list.pop(client_record['name'])



