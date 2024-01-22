import requests
from flask import Flask, render_template, request, redirect, flash
from flask_migrate import Migrate, upgrade
from flask_security import (
    Security,
    hash_password,
    roles_accepted,
    auth_required,
    SQLAlchemyUserDatastore,
    logout_user,
)
from flask_security.models import fsqla_v3 as fsqla

app = Flask(__name__)
app.config.from_object("config.ConfigDebug")

db.app = app
db.init_app(app)
migrate = Migrate(app, db)
fsqla.FsModels.set_db_info(db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)


@app.route("/", methods=["GET"])
def startPage():
    return render_template("baseTemplate.html")








if __name__ == '__main__':
    app.run(debug=True)