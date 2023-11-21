from event_plan import EventPlan

def test_event_plan():
    Test_event_plan={
        "service_subteam_task": "todo1",
        "production_subteam_task": "todo2",
        "service_subteam_plan": "plan1",
        "production_subteam_plan": "plan2",
        "recruitment_request": "3 staff more",
        "recruitment_reply": "approved",
        "extra_budget_negotiation_request": "5000$ more",
        "extra_budget_negotiation_reply": "empty"
    }
    return Test_event_plan

def workflow4():
    # upload recruitment request
    test = test_event_plan()

    print("I'm production manager")
    EventPlan["extra_budget_negotiation_request"] = test["extra_budget_negotiation_request"]
    print("extra budget negotiation request uploaded")
    print("---------------------------------------------------------------")

    if EventPlan["extra_budget_negotiation_request"] != 'empty':
        print("I'm financial manager")
        print(EventPlan["extra_budget_negotiation_request"])
        EventPlan["extra_budget_negotiation_reply"] = test["extra_budget_negotiation_reply"]
        print("extra budget negotiation reply uploaded")
        print("-----------------------------------------------------------")
    else:
        print("no more request")

    if EventPlan["extra_budget_negotiation_reply"] != 'empty':
        print("I'm production manager")
        print(EventPlan["extra_budget_negotiation_reply"])
    else:
        print("no more reply")

if __name__ == '__main__':
    workflow4()
