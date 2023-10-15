class Client_request:
    def __init__(self, name, budget, preferences, decision):
        self.name = name
        self.budget = budget
        self.preferences = preferences
        self.decision = decision

    def get_client_name(self):
        return self.name

    def get_client_budget(self):
        return self.budget

    def get_client_preference(self):
        return self.preferences

    def get_client_decision(self):
        return self.decision

    def update_decision(self, new_decision):
        self.decision = new_decision
        return self.decision