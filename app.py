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
from models import db, seedData

app = Flask(__name__)
app.config.from_object("config.ConfigDebug")

db.app = app
db.init_app(app)
migrate = Migrate(app, db)
fsqla.FsModels.set_db_info(db)


class Role(db.Model, fsqla.FsRoleMixin):
    pass  # Reasonable defaults!


class User(db.Model, fsqla.FsUserMixin):
    GivenName = db.Column(db.String(50), unique=False, nullable=False)
    Surname = db.Column(db.String(50), unique=False, nullable=False)
    pass


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)


@app.route("/", methods=["GET"])
def startPage():
    return render_template("baseTemplate.html")


@app.route("/predict", methods=["GET", "POST"])
def predictFromPicture():
    if request.method == "POST":
        # Retrieve the selected radio button value (user_choice)
        user_choice = request.form.get("user_choice")
        return render_template("result.html", user_choice=user_choice)

    # For the initial GET request, you might want to handle it differently
    # For example, redirect to the upload form or render a different template
    return render_template("baseTemplate.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        upgrade()
        seedData(app, db)
    app.run(debug=True)
