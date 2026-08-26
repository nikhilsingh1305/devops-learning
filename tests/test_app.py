from app.app import health_check


def test_health_check():
    result = health_check()

    assert result["status"] == "healthy"
    assert result["service"] == "devops-learning"