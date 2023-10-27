from upload_client_request import Client, Client_request
from staff import Staff
from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QPushButton,
                             QLabel,
                             QLineEdit)
from staff import (CustomerService,
                   SeniorCustomerService,
                   FinancialManager,
                   AdminastrationManager)

from event_plan import EventPlan
from client_record import client_records

customerService = CustomerService()
seniorCustomerService = SeniorCustomerService()
financialManager = FinancialManager()
administrationManager = AdminastrationManager()
class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 400, 200)

        self.username_label = QLabel('username')
        self.username_label.setGeometry(50, 50, 100, 20)
        self.username_input = QLineEdit()
        self.username_input.setGeometry(150, 80, 100, 20)

        self.password_label = QLabel('password')
        self.password_label.setGeometry(50, 80, 100, 20)
        self.password_input = QLineEdit()
        self.password_input.setGeometry(150, 80, 200, 20)
        self.password_input.setEchoMode(QLineEdit.Password)  # hide password

        self.login_button = QPushButton('Login')
        self.login_button.setGeometry(150, 120, 100, 30)
        self.login_button.clicked.connect(self.login)

        self.client_button = QPushButton('Client')
        self.client_button.setGeometry(150, 150, 100, 30)
        self.client_button.clicked.connect(self.client)

        self.invalid_label = QLabel('')
        self.invalid_label.setGeometry(50, 200, 300, 20)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.client_button)
        layout.addWidget(self.invalid_label)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'customer service':
            self.open_customer_service_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'senior customer service':
            self.open_senior_customer_service_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'financial manager':
            self.open_financial_manager_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'administration manager':
            self.open_administration_manager_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'production manager':
            self.open_production_manager_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'service manager':
            self.open_service_manager_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'HR manager':
            self.open_HR_manager_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'service sub team':
            self.open_Service_Sub_team_window()
        elif username in Staff and Staff[username]['password'] == password and Staff[username]['position'] == 'production sub team':
            self.open_Production_Sub_team_window()
        else:
            self.invalid_label.setText('Invalid!')

    def client(self):
        self.close()
        self.new_window = Client_GUI()
        self.new_window.show()

    def open_customer_service_window(self):
        self.close()
        self.new_window = CustomerService_GUI()
        self.new_window.show()

    def open_senior_customer_service_window(self):
        self.close()
        self.new_window = SeniorCustomerService_GUI()
        self.new_window.show()

    def open_financial_manager_window(self):
        self.close()
        self.new_window = FinancialManager_GUI()
        self.new_window.show()

    def open_administration_manager_window(self):
        self.close()
        self.new_window = AdministrationManager_GUI()
        self.new_window.show()

    def open_production_manager_window(self):
        self.close()
        self.new_window = ProductionManager_GUI()
        self.new_window.show()

    def open_service_manager_window(self):
        self.close()
        self.new_window = ServiceManager_GUI()
        self.new_window.show()

    def open_HR_manager_window(self):
        self.close()
        self.new_window = HRManager_GUI()
        self.new_window.show()

    def open_Service_Sub_team_window(self):
        self.close()
        self.new_window = ServiceSubTeam_GUI()
        self.new_window.show()

    def open_Production_Sub_team_window(self):
        self.close()
        self.new_window = ProductionSubTeam_GUI()
        self.new_window.show()


class CustomerService_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CustomerService GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('request_decision')
        self.text1_input = QLineEdit()

        self.Todo1_button = QPushButton('view_client_request')
        self.Todo1_button.clicked.connect(self.view_client_request)

        self.Todo2_button = QPushButton('submit')
        self.Todo2_button.clicked.connect(self.submit)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_client_request(self):
        self.output_label.setText(Client_request["name"]+'\n'
                                  +Client_request["email"]+'\n'
                                  +Client_request["budget"]+'\n'
                                  +Client_request["preferences"]+'\n'
                                  +Client_request["discount"])

    def submit(self):
        if self.text1_input.text() == 'approved':
            customerService.decision = 'approved'
            self.output_label.setText("approved")
        elif self.text1_input.text() == 'reject':
            self.output_label.setText("reject")
        else:
            self.output_label.setText("invalid")
class SeniorCustomerService_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SeniorCustomerService GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('request_decision')
        self.text1_input = QLineEdit()

        self.Todo1_button = QPushButton('view_client_request')
        self.Todo1_button.clicked.connect(self.view_client_request)

        self.Todo2_button = QPushButton('manage_client_records')
        self.Todo2_button.clicked.connect(self.manage_client_records)

        self.Todo3_button = QPushButton('submit')
        self.Todo3_button.clicked.connect(self.submit)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.Todo3_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_client_request(self):
        self.output_label.setText(Client_request["name"] + '\n'
                                  + Client_request["email"] + '\n'
                                  + Client_request["budget"] + '\n'
                                  + Client_request["preferences"] + '\n'
                                  + Client_request["discount"])

    def manage_client_records(self):
        if Client_request["name"] in client_records:
            self.output_label.setText("old customer")
        else:
            self.output_label.setText("new customer")


    def submit(self):
        if customerService.decision == 'approved':
            if self.text1_input.text() == 'approved':
                # # view record
                # seniorCustomerService.manage_client_record()
                seniorCustomerService.decision = 'approved'
                self.output_label.setText("approved")
            elif self.text1_input.text() == 'reject':
                self.output_label.setText("reject")
            else:
                self.output_label.setText("invalid")
        else:
            self.output_label.setText("reject")


class FinancialManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FinancialManager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('request_decision')
        self.text1_input = QLineEdit()

        self.Todo1_button = QPushButton('view_client_request')
        self.Todo1_button.clicked.connect(self.view_client_request)

        self.Todo2_button = QPushButton('check_discount')
        self.Todo2_button.clicked.connect(self.check_discount)

        self.Todo3_button = QPushButton('submit')
        self.Todo3_button.clicked.connect(self.submit)

        self.Todo4_button = QPushButton('view_extra_negotiation')
        self.Todo4_button.clicked.connect(self.view_extra_negotiation)

        self.text2_label = QLabel('ex_budget_negotiation_reply')
        self.text2_input = QLineEdit()

        self.Todo5_button = QPushButton('upload_extra_budget_negotiation')
        self.Todo5_button.clicked.connect(self.upload_extra_budget_negotiation)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo3_button)
        layout.addWidget(self.Todo4_button)
        layout.addWidget(self.text2_label)
        layout.addWidget(self.text2_input)
        layout.addWidget(self.Todo5_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def check_discount(self):
        if Client_request["name"] in client_records:
            Client_request["discount"] = "discount"
            self.output_label.setText("discount")

    def view_client_request(self):
        self.output_label.setText(Client_request["name"] + '\n'
                                  + Client_request["email"] + '\n'
                                  + Client_request["budget"] + '\n'
                                  + Client_request["preferences"] + '\n'
                                  + Client_request["discount"])
    def submit(self):
        if seniorCustomerService.decision == 'approved':
            if self.text1_input.text() == 'approved':
                financialManager.decision = 'approved'
                self.output_label.setText("approved")
            elif self.text1_input.text() == 'reject':
                self.output_label.setText("reject")
            else:
                self.output_label.setText("invalid")
        else:
            self.output_label.setText("invalid")

    def view_extra_negotiation(self):
        self.output_label.setText(EventPlan["extra_budget_negotiation_request"])

    def upload_extra_budget_negotiation(self):
        extra_budget_negotiation = self.text2_input.text()
        EventPlan["extra_budget_negotiation_reply"] = extra_budget_negotiation
        self.output_label.setText("extra budget negotiation reply uploaded")



class AdministrationManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AdministrationManager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('request_decision')
        self.text1_input = QLineEdit()

        self.Todo1_button = QPushButton('view_client_request')
        self.Todo1_button.clicked.connect(self.view_client_request)

        self.Todo2_button = QPushButton('submit')
        self.Todo2_button.clicked.connect(self.submit)


        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_client_request(self):
        self.output_label.setText(Client_request["name"] + '\n'
                                  + Client_request["email"] + '\n'
                                  + Client_request["budget"] + '\n'
                                  + Client_request["preferences"] + '\n'
                                  + Client_request["discount"])

    def submit(self):
        if financialManager.decision == 'approved':
            if self.text1_input.text() == 'approved':
                administrationManager.decision = 'approved'
                self.output_label.setText("approved")
            elif self.text1_input.text() == 'reject':
                self.output_label.setText("reject")
            else:
                self.output_label.setText("invalid")
        else:
            self.output_label.setText("invalid")

class ProductionManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ProductionManager GUI')
        self.setGeometry(100, 100, 400, 400)

        self.Todo1_button = QPushButton('view_sub_plan')
        self.Todo1_button.clicked.connect(self.view_sub_plan)

        self.text1_label = QLabel('sub_task')
        self.text1_input = QLineEdit()

        self.Todo2_button = QPushButton('upload_sub_task')
        self.Todo2_button.clicked.connect(self.upload_sub_task)

        self.Todo3_button = QPushButton('view_recruitment_reply')
        self.Todo3_button.clicked.connect(self.view_recruitment_reply)

        self.text2_label = QLabel('recruitment_request')
        self.text2_input = QLineEdit()

        self.Todo4_button = QPushButton('upload_recruitment_request')
        self.Todo4_button.clicked.connect(self.upload_recruitment_request)

        self.Todo5_button = QPushButton('view_ex_budget_request')
        self.Todo5_button.clicked.connect(self.view_ex_budget_reply)

        self.text3_label = QLabel('ex_budget_request')
        self.text3_input = QLineEdit()

        self.Todo6_button = QPushButton('upload_ex_budget_request')
        self.Todo6_button.clicked.connect(self.upload_ex_budget_request)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.Todo3_button)
        layout.addWidget(self.text2_label)
        layout.addWidget(self.text2_input)
        layout.addWidget(self.Todo4_button)
        layout.addWidget(self.Todo5_button)
        layout.addWidget(self.text3_label)
        layout.addWidget(self.text3_input)
        layout.addWidget(self.Todo6_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_sub_plan(self):
        self.output_label.setText(EventPlan["production_subteam_plan"])

    def upload_sub_task(self):
        sub_plan = self.text1_input.text()
        EventPlan["production_subteam_task"] = sub_plan
        self.output_label.setText("sub_task_uploaded!")

    def view_recruitment_reply(self):
        self.output_label.setText(EventPlan["recruitment_reply"])

    def upload_recruitment_request(self):
        recruitment_request = self.text2_input.text()
        EventPlan["recruitment_request"] = recruitment_request
        self.output_label.setText("recruitment_request_uploaded!")

    def view_ex_budget_reply(self):
        self.output_label.setText(EventPlan["extra_budget_negotiation_reply"])

    def upload_ex_budget_request(self):
        ex_budget_request = self.text3_input.text()
        EventPlan["extra_budget_negotiation_request"] = ex_budget_request
        self.output_label.setText("ex_budget_request_updated")

class ServiceManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ServiceManager GUI')
        self.setGeometry(100, 100, 400, 400)

        self.Todo1_button = QPushButton('view_sub_plan')
        self.Todo1_button.clicked.connect(self.view_sub_plan)

        self.text1_label = QLabel('sub_task')
        self.text1_input = QLineEdit()

        self.Todo2_button = QPushButton('upload_sub_task')
        self.Todo2_button.clicked.connect(self.upload_sub_task)

        self.Todo3_button = QPushButton('view_recruitment_reply')
        self.Todo3_button.clicked.connect(self.view_recruitment_reply)

        self.text2_label = QLabel('recruitment_request')
        self.text2_input = QLineEdit()

        self.Todo4_button = QPushButton('upload_recruitment_request')
        self.Todo4_button.clicked.connect(self.upload_recruitment_request)

        self.Todo5_button = QPushButton('view_ex_budget_request')
        self.Todo5_button.clicked.connect(self.view_ex_budget_reply)

        self.text3_label = QLabel('ex_budget_request')
        self.text3_input = QLineEdit()

        self.Todo6_button = QPushButton('upload_ex_budget_request')
        self.Todo6_button.clicked.connect(self.upload_ex_budget_request)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.Todo3_button)
        layout.addWidget(self.text2_label)
        layout.addWidget(self.text2_input)
        layout.addWidget(self.Todo4_button)
        layout.addWidget(self.Todo5_button)
        layout.addWidget(self.text3_label)
        layout.addWidget(self.text3_input)
        layout.addWidget(self.Todo6_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_sub_plan(self):
        self.output_label.setText(EventPlan["service_subteam_plan"])

    def upload_sub_task(self):
        sub_plan = self.text1_input.text()
        EventPlan["service_subteam_task"] = sub_plan
        self.output_label.setText("sub_task_uploaded!")

    def view_recruitment_reply(self):
        self.output_label.setText(EventPlan["recruitment_reply"])

    def upload_recruitment_request(self):
        recruitment_request = self.text2_input.text()
        EventPlan["recruitment_request"] = recruitment_request
        self.output_label.setText("recruitment_request_uploaded!")

    def view_ex_budget_reply(self):
        self.output_label.setText(EventPlan["extra_budget_negotiation_reply"])

    def upload_ex_budget_request(self):
        ex_budget_request = self.text3_input.text()
        EventPlan["extra_budget_negotiation_request"] = ex_budget_request
        self.output_label.setText("ex_budget_request_updated")


class ServiceSubTeam_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ServiceSubteam GUI')
        self.setGeometry(100, 100, 400, 200)

        self.Todo1_button = QPushButton('view_sub_task')
        self.Todo1_button.clicked.connect(self.view_sub_task)

        self.text1_label = QLabel('sub_plan')
        self.text1_input = QLineEdit()

        self.Todo2_button = QPushButton('upload_sub_plan')
        self.Todo2_button.clicked.connect(self.upload_sub_plan)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_sub_task(self):
        self.output_label.setText(EventPlan["service_subteam_task"])

    def upload_sub_plan(self):
        sub_plan = self.text1_input.text()
        EventPlan["service_subteam_plan"] = sub_plan
        self.output_label.setText("sub plan uploaded")

class ProductionSubTeam_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ProductionSubteam GUI')
        self.setGeometry(100, 100, 400, 200)

        self.Todo1_button = QPushButton('view_sub_task')
        self.Todo1_button.clicked.connect(self.view_sub_task)

        self.text1_label = QLabel('sub_plan')
        self.text1_input = QLineEdit()

        self.Todo2_button = QPushButton('upload_sub_plan')
        self.Todo2_button.clicked.connect(self.upload_sub_plan)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_sub_task(self):
        self.output_label.setText(EventPlan["production_subteam_task"])

    def upload_sub_plan(self):
        sub_plan = self.text1_input.text()
        EventPlan["production_subteam_plan"] = sub_plan
        self.output_label.setText("sub plan uploaded")

class HRManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HR Manager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.Todo1_button = QPushButton('view_recruitment_request')
        self.Todo1_button.clicked.connect(self.view_recruitment_request)

        self.text1_label = QLabel('sub_plan')
        self.text1_input = QLineEdit()

        self.Todo2_button = QPushButton('upload_recruitment_reply')
        self.Todo2_button.clicked.connect(self.upload_recruitment_reply)

        self.home_button = QPushButton('home')
        self.home_button.clicked.connect(self.home)

        self.output_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo2_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def view_recruitment_request(self):
        self.output_label.setText(EventPlan["recruitment_request"])

    def upload_recruitment_reply(self):
        recruitment_reply = self.text1_input.text()
        EventPlan["recruitment_reply"] = recruitment_reply
        self.output_label.setText("recruitment reply uploaded")

class Client_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Client GUI')
        self.setGeometry(100, 100, 400, 200)

        self.name_label = QLabel('name')
        self.name_input = QLineEdit()

        self.email_label = QLabel('email')
        self.email_input = QLineEdit()

        self.budget_label = QLabel('budget')
        self.budget_input = QLineEdit()

        self.preferences_label = QLabel('preferences')
        self.preferences_input = QLineEdit()

        self.Todo1_button = QPushButton('upload reqeust')
        self.Todo1_button.clicked.connect(self.todo1)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.home)

        self.result_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.budget_label)
        layout.addWidget(self.budget_input)
        layout.addWidget(self.preferences_label)
        layout.addWidget(self.preferences_input)
        layout.addWidget(self.Todo1_button)
        layout.addWidget(self.home_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def home(self):
        self.close()
        self.new_window = GUI()
        self.new_window.show()

    def todo1(self):
        name = self.name_input.text()
        email = self.email_input.text()
        budget = self.budget_input.text()
        preferences = self.preferences_input.text()
        self.result_label.setText('uploaded!')
        Client_request["name"] = name
        Client_request["email"] = email
        Client_request["budget"] = budget
        Client_request["preferences"] = preferences
