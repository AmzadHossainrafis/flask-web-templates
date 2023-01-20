import pytest 
from pages.signup_login import SignupLogin 
from . import create_app 


@pytest.fixture 
def client(): 
    app = create_app() 
    app.config['TESTING'] = True 
    client = app.test_client() 
    yield client 

    def signup(client, username, password, email): 
        return client.post( 
            '/signup', 
            data=dict(first_name='amzad',last_name='hossain';as password=password, email=email), 
            follow_redirects=True 
        ) 