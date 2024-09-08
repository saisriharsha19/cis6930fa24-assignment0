import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main

def test_process_data_empty():
    """Test processing data when no items are present."""
    data = {"items": []}
    result = main.process_data(data)
    assert result == ""

def test_process_data_non_empty():
    """Test processing non-empty data."""
    data = {
        "items": [
            {"title": "Sample Title", "subjects": ["Subject1", "Subject2"], "field_offices": ["Office1", "Office2"]},
            {"title": "Another Title", "subjects": ["Subject3"], "field_offices": ["Office3"]}
        ]
    }
    result = main.process_data(data)
    expected = "Sample TitleþSubject1, Subject2þOffice1, Office2\nAnother TitleþSubject3þOffice3"
    assert result == expected
