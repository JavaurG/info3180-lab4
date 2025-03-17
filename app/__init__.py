from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize database instance first
db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

# Initialize db with the app
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views, models  # Ensure models are imported to define tables

# from flask import Flask
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
# from .config import Config
# # import flask migrate here
# from flask_migrate import Migrate



# app = Flask(__name__)
# app.config.from_object(Config)
# migrate = Migrate(app, db)
# db = SQLAlchemy(app)
# # Instantiate Flask-Migrate library here

# # Flask-Login login manager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# from app import views

