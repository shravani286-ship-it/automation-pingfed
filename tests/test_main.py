from unittest.mock import patch
from src.main import post_request

def test_post_request_success():
    # Mock requests.post inside src.main
    with patch("src.main.requests.post") as mock_post:
        # Configure the mock to return a response with status_code 201
        mock_post.return_value.status_code = 201
        
        status = post_request()
        assert status == 201

def test_post_request_failure():
    with patch("src.main.requests.post") as mock_post:
        mock_post.return_value.status_code = 400
        
        status = post_request()
        assert status == 400