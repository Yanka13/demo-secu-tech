"""
This module provides tests for the dice rolling game module.

The tests cover the functionality of the '/roll_dice' endpoint.

"""

import pytest
from dice import app


@pytest.fixture
def client():
    """
    Fixture to create a test client for the Flask application.
    """
    app.testing = True
    client = app.test_client()
    yield client


def test_roll_dice(client):
    """
    Test the '/roll_dice' endpoint.
    """
    response = client.get("/roll_dice")
    assert response.status_code == 200
    assert "result" in response.json
    assert isinstance(response.json["result"], int)
