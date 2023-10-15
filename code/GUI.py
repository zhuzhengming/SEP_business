import sys
from staff import Staff
from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QApplication)

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.setGeometry(100,100,400,200)


        self.username_label = QLabel('username')
        self.username_label.setGeometry(50,50,100,20)
        self.username_input = QLineEdit()
        self.username_input.setGeometry(150,80,100,20)

        self.password_label = QLabel('password')
        self.password_label.setGeometry(50, 80, 100, 20)
        self.password_input = QLineEdit()
        self.password_input.setGeometry(150, 80, 200, 20)
        self.password_input.setEchoMode(QLineEdit.Password)  # hide password

        self.login_button = QPushButton('Login')
        self.login_button.setGeometry(150, 120, 100, 30)
        self.login_button.clicked.connect(self.login)

        self.invalid_label = QLabel('')
        self.invalid_label.setGeometry(50, 160, 300, 20)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
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
        elif username == 'client':
            self.open_client_window()
        else:
            self.invalid_label.setText('Invalid!')

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

    def open_client_window(self):
        self.close()
        self.new_window = Client_GUI()
        self.new_window.show()

class CustomerService_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CustomerService GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class SeniorCustomerService_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SeniorCustomerService GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class FinancialManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FinancialManager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class AdministrationManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AdministrationManager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class ProductionManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ProductionManager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class ServiceManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ServiceManager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class ServiceSubTeam_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ServiceSubteam GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class ProductionSubTeam_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ProductionSubTeam GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class HRManager_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HR Manager GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作

class Client_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Client GUI')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('text1')
        self.text1_label.setGeometry(50, 50, 100, 20)
        self.text1_input = QLineEdit()
        self.text1_input.setGeometry(150, 80, 100, 20)

        self.Todo1_button = QPushButton('Todo1')
        self.Todo1_button.setGeometry(50, 100, 100, 30)
        self.Todo1_button.clicked.connect(self.todo1)

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text1_input)
        layout.addWidget(self.Todo1_button)

        self.setLayout(layout)

    def todo1(self):
        # 在这里添加按钮点击事件的处理逻辑
        print("todo 1!")
         # 处理输入的文本，可以根据需要执行相关操作







