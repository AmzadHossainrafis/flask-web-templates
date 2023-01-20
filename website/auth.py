from flask import Blueprint 


auth = Blueprint('auth', __name__) 


#create a route decorator 
@auth.route('/login') 
def login(): 
    return 'Login' 


@auth.route('/logout') 
def logout(): 
    return 'Logout' 


@auth.route('/signup') 
def signup(): 
    return 'Signup' 
