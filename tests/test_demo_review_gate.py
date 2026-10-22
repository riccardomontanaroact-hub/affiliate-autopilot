from datetime import date
from agent.offer_policy import ready_for_publication

def test_demo_rejected():
    p = dict(merchant="DEMO", publication_approved=True, affiliate_status="approved", approval_source="awin_dashboard", approval_verified_at="2026-10-21", affiliate_url="https://github.com")
    assert ready_for_publication(p, date(2026, 10, 21)) is False
