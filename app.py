#import ceate_app function from the __init__.py file 
from website import create_app

app = create_app()


if __name__ == '__main__': 
    app.run(debug=True)

# Path: config.py
# This file is not used by the application, but you can use it to store configuration -
# variables that are specific to your deployment, such as API keys.