from event_plan import EventPlan

def test_event_plan():
    Test_event_plan={
        "service_subteam_task": "todo1",
        "production_subteam_task": "todo2",
        "service_subteam_plan": "plan1",
        "production_subteam_plan": "plan2",
        "recruitment_request": "3 staff more",
        "recruitment_reply": "approved",
        "extra_budget_negotiation_request": "5000",
        "extra_budget_negotiation_reply": "approved"
    }
    return Test_event_plan

def workflow3():
    # upload recruitment request
    test = test_event_plan()

    print("I'm production manager")
    EventPlan["recruitment_request"] = test["recruitment_request"]
    print("recruitment request uploaded")
    print("---------------------------------------------------------------")

    if EventPlan["recruitment_request"] != 'empty':
        print("I'm HR manager")
        print(EventPlan["recruitment_request"])
        EventPlan["recruitment_reply"] = test["recruitment_reply"]
        print("recruitment reply uploaded")
        print("-----------------------------------------------------------")
    else:
        print("no more request")

    if EventPlan["recruitment_reply"] != 'empty':
        print("I'm production manager")
        print(EventPlan["recruitment_reply"])
    else:
        print("no more reply")

if __name__ == '__main__':
    workflow3()