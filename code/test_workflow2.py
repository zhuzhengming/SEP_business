# This is the test code testing the expected behavior of user stories in workflow 2
# 4 functions whose names begin with test_ are used to test 4 user stories in workflow 2
# To use this test program, delete the main program in the upper directory and use this program as main program instead

from event_plan import EventPlan
from GUI import GUI
from PyQt5.QtWidgets import QApplication
import sys

def test_upload_sub_task (Login_window):
    Login_window.open_production_manager_window()
    Login_window.new_window.text1_input.setText("sub_task_example")
    Login_window.new_window.upload_sub_task()
    print("test name: test_upload_sub_task")
    print("sub_task:")
    print(EventPlan["production_subteam_task"])

def test_review_sub_task (Login_window):
    Login_window.open_Production_Sub_team_window()
    Login_window.new_window.view_sub_task()
    print("test name: test_review_sub_task")
    print("sub_task: ")
    print(EventPlan["production_subteam_task"])

def test_upload_sub_plan (Login_window):
    Login_window.open_Production_Sub_team_window()
    Login_window.new_window.text1_input.setText("sub_plan_example")
    Login_window.new_window.upload_sub_plan()
    print("test name: test_upload_sub_plan")
    print("sub_plan: ")
    print(EventPlan["production_subteam_plan"])

def test_review_sub_plan (Login_window):
    Login_window.open_production_manager_window()
    Login_window.new_window.view_sub_plan()
    print("test name: test_review_sub_plan")
    print("sub_plan: ")
    print(EventPlan["production_subteam_plan"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login_window = GUI()
    Login_window.show()
    print("---------------------Workflow2 Test Begin--------------------------\n")
    # test functions to be executed begin
    test_upload_sub_task(Login_window)
    test_review_sub_task(Login_window)
    test_upload_sub_plan(Login_window)
    test_review_sub_plan(Login_window)
    # test functions to be executed end
    print("---------------------Workflow2 Test End----------------------------\n")

    sys.exit(app.exec_())