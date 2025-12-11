from unittest.mock import patch
from src.main import post_request

def test_post_request_success():
    # Mock requests.post to simulate a successful API call
    with patch("src.main.requests.post") as mock_post:
        mock_post.return_value.status_code = 201  # Simulate HTTP 201 Created
        status = post_request()
        assert status == 201

def test_post_request_failure():
    # Mock requests.post to simulate a failed API call
    with patch("src.main.requests.post") as mock_post:
        mock_post.return_value.status_code = 400  # Simulate HTTP 400 Bad Request
        status = post_request()
        assert status == 400
