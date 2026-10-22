from agent.offer_policy import ready_for_publication

def test_demo_merchant():
    assert not ready_for_publication({'merchant': 'DEMO'})
