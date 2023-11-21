from client_record import Client_record

Staff = {
    "Sam": {'name': 'Sam', 'password': '123456', 'position': 'customer service'},
    "Janet": {'name': 'Janet', 'password': '123456', 'position': 'senior customer service'},
    "Mike": {'name': 'Mike', 'password': '123456', 'position': 'administration manager'},
    "Alice": {'name': 'Alice', 'password': '123456', 'position': 'financial manager'},
    "Jack": {'name': 'Jack', 'password': '123456', 'position': 'production manager'},
    "Simon": {'name': 'Simon', 'password': '123456', 'position': 'HR manager'},
    "Natalie": {'name': 'Natalie', 'password': '123456', 'position': 'service manager'},
    "Helen": {'name': 'Helen', 'password': '123456', 'position': 'service sub team'},
    "Julia": {'name': 'Julia', 'password': '123456', 'position': 'production sub team'}
}

class Manager:
    def __init__(self):
        self.decision = None
        self.client_record = Client_record()

    def view_client_reqeust(self, Client_request):
        self.client_reqeust = Client_request
        print(self.client_reqeust)

    def feedback(self):
        return self.decision

class SubTeam:
    def __init__(self, event_plan):
        self.event_plan = event_plan

    def upload_sub_plan(self):
        sub_plan = {
            'food': 'rice'
        }
        return sub_plan

    def budget_application(self):
        application = {
            'extra budget': 120
        }
        return application

class CustomerService(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Sam'
        self.position = 'customer service'

class SeniorCustomerService(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Janet'
        self.position = 'senior customer service'

    def manage_client_record(self):

        # if new customer, add to records
        if self.client_reqeust['name'] not in self.client_record.get_client_records():
            self.client_record.add_client_records(self.client_reqeust)
            print(self.client_record.list)

    def informCustomer(self):
        return self.decision


class FinancialManager(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Alice'
        self.position = 'financial manager'

    def isDiscount(self):

        if self.client_reqeust['name']['name'] in self.client_record.get_client_records():
            self.client_record.add_client_records(self.client_reqeust)
            self.client_record['discount'] = 'discount'
            print("discount")
        else:
            print("can't get discount")

class AdminastrationManager(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Mike'
        self.position = 'administration manager'

class ProductionManager(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Jack'
        self.position = 'production manager'

class ServiceManager(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Natalie'
        self.position = 'service manager'

class HRManager(Manager):
    def __init__(self):
        super().__init__()

        self.name = 'Simon'
        self.position = 'HR manager'

class ServiceSubTeam(SubTeam):
    def __init__(self):
        super().__init__()

        self.name = 'Halen'
        self.position = 'service sub team'

class ProductionSubTeam(SubTeam):
    def __init__(self):
        super().__init__()

        self.name = 'Julia'
        self.position = 'production sub team'

