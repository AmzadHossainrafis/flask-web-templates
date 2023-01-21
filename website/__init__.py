import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import Config 
from flask_login import LoginManager 





db = SQLAlchemy()

def create_app():
    '''
    summary : 

    Create and configure an instance of the Flask application. The instance folder -
    is located outside the flaskr package and can hold local data that shouldn't be -
    committed to version control, such as configuration secrets and the database file. 
    You'll use the instance folder to store the SQLite database file later in the -
    tutorial.test_config can be passed in to configure the app in test mode.
    When testing, you'll pass in a different configuration than when running the app normally.
    The tests need to be configured to use a different database, so that they don't clobber -
    the development database when the tests are running.


    :param test_config:  
    
    :return: Flask app instance 

    '''
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config['SECRET_KEY'] 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{Config["DATABASE_NAME"]}' 
    db.init_app(app) 



   



    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth , url_prefix='/')



    from . import models 
    from .models import User
    with app.app_context():
        db.create_all()



    login_Manager=LoginManager()
    login_Manager.login_view='views.login'
    login_Manager.init_app(app)

    @login_Manager.user_loader 
    def load_user(id): 
        return User.query.get(int(id))





    return app


