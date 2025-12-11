from unittest.mock import patch
from src.main import post_request

def test_post_request_success():
    with patch("src.main.requests.post") as mock_post:
        # Simulate a successful response
        mock_post.return_value.status_code = 201
        
        status = post_request()
        assert status == 201

def test_post_request_failure():
    with patch("src.main.requests.post") as mock_post:
        # Simulate a failed response
        mock_post.return_value.status_code = 400
        
        status = post_request()
        assert status == 400
