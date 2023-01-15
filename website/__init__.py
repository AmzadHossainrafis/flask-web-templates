import os
from flask import Flask
from config import Config 


def create_app(test_config=None):
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
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=Config['SECRET_KEY'],
        DATABASE=os.path.join(app.instance_path, Config['DATABASE_NAME']),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass




    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth , url_prefix='/')


    return app
