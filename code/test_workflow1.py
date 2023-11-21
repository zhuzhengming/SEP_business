from staff import Staff, CustomerService, SeniorCustomerService, FinancialManager, AdminastrationManager
from client_record import client_records

def test_client_request():
    Client_request = {
        'name': 'Ming',
        'email': 'zhzhu@kth.se',
        'budget': '200000',
        'preferences': 'chicken',
        'decision': 'None',
        'discount': 'None'
    }
    return Client_request

def workflow1():
    Client_request = test_client_request()
    print("client request uploaded! ")
    customerService = CustomerService()
    seniorCustomerService = SeniorCustomerService()
    financialManager = FinancialManager()
    administrationManager = AdminastrationManager()

#     login
    if customerService.name == Staff['Sam']['name']:
        print("I'm customer Service ")
        customerService.view_client_reqeust(Client_request)
        customerService.decision = 'approved'
        print("approved by customer service ")
        print("--------------------------------------------"
              "--------------------------------------------")

    if seniorCustomerService.name == Staff['Janet']['name']:
        print("I'm senior customer Service ")
        if customerService.decision == 'approved':
            seniorCustomerService.view_client_reqeust(Client_request)
            # manage client request
            if Client_request['name'] in client_records:
                print('old customer')
            else:
                print('new customer')

            seniorCustomerService.decision = 'approved'
            print("approved by senior customer service")
        else:
            seniorCustomerService.decision = 'reject'
            print("rejected by senior customer service")
        print("--------------------------------------------"
              "--------------------------------------------")

    if financialManager.name == Staff['Alice']['name']:
        print("I'm financial manager")
        if seniorCustomerService.decision == 'approved':
            financialManager.view_client_reqeust(Client_request)
            # is discount?
            if Client_request['name'] in client_records:
                Client_request['discount'] = 'discount'
                print("discount")
            else:
                print("no discount")
            financialManager.decision = 'approved'
            print("approved by financial manager ")
        else:
            seniorCustomerService.decision = 'reject'
            print("rejected by financial manager ")
        print("--------------------------------------------"
              "--------------------------------------------")

    if administrationManager.name == Staff['Mike']['name']:
        print("I'm administration manager")
        if financialManager.decision == 'approved':
            administrationManager.view_client_reqeust(Client_request)
            administrationManager.decision = 'approved'
            print("approved by administration manager ")
        else:
            administrationManager.decision = 'reject'
            print("rejected by administration manager ")
        print("--------------------------------------------"
              "--------------------------------------------")

if __name__ == '__main__':
    workflow1()


