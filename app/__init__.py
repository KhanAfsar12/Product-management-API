from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    global app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'afsaracademy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/poc" 

    db.init_app(app)

    from app.auth.controllers import auth_blueprint

    app.register_blueprint(auth_blueprint,url_prefix=f"/api/{auth_blueprint.url_prefix}")


    return app