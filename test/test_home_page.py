import pytest
import requests

def test_home_page():
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    assert "Welcome to the home page" in response.content.decode()


if __name__ == '__main__':
    pytest.test_home_page() 