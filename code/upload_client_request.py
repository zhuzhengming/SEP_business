Client_request = {
            'name': 'None',
            'email': 'None',
            'budget': 'None',
            'preferences': 'None',
            'decision': 'None',
            'discount': 'None'
        }
class Client:
    def __init__(self):
        self.init_data()

    def init_data(self):
        self.name = None
        self.email = None
        self.budget = None
        self.preferences = None
        self.decision = 'Pending'
        self.discount = None

    def propose_init_budget_preferences(self, budget, preferences):
        self.budget = budget
        self.preferences = preferences

    def update_decision(self, new_decision):
        self.decision = new_decision
        return self.decision

    def upload_basic_info(self, name, email):
        self.name = name
        self.email = email

    def return_client_request_to_dict(self):
        dict = {
            'name': self.name,
            'email': self.email,
            'budget': self.budget,
            'preferences': self.preferences,
            'decision': self.decision,
            'discount': self.discount
        }
        return dict

