import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main
import requests
from unittest.mock import patch

def test_fetch_data_from_api_success():
    """Test for fetching data from the API successfully."""
    response = {
        "items": [
            {"title": "Sample Title", "subjects": ["Subject1", "Subject2"], "field_offices": ["Office1"]}
        ]
    }
    with patch('main.requests.get') as get:
        get.return_value.status_code = 200
        get.return_value.json.return_value = response
        result = main.fetch_data_from_api(1)
        assert result == response

def test_fetch_data_from_api_failure():
    """Test for fetching data from the API with a failure response."""
    with patch('main.requests.get') as get:
        get.return_value.status_code = 404
        get.side_effect = requests.exceptions.HTTPError
        try:
            main.fetch_data_from_api(1)
        except requests.exceptions.HTTPError:
            assert True
        else:
            assert False
