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


@app.route("/upload", methods=["POST"])
def upload_image():
    # Handle image upload here (your teammate's responsibility)
    # ...

    return "Image uploaded successfully"


@app.route("/predict", methods=["POST"])
def predict():
    # Get the user's choice from the request
    choice = request.json.get(
        "choice"
    )  # Adjust based on how the data is sent from the frontend

    # Use the choice to load the corresponding model and make predictions
    # ...

    # Return prediction results (you may want to use jsonify for a more structured response)
    return f"Predicted result for {choice}"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        upgrade()
        seedData(app, db)
    app.run(debug=True)
