from flask import Blueprint

from flask import render_template
from flask_login import login_required,logout_user,current_user

views = Blueprint('views', __name__) 

@views.route('/') 
def home(): 
    return render_template('home.html')  
    

@views.route('/dashboard')
@login_required 
def dashboard(): 
    return render_template('user_dash/user_dash.html', user=current_user)

