from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)
from main import main as main_blueprint
from auth import auth as auth_blueprint
from models import User

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()
app.run()


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
