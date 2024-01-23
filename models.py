from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, hash_password
from datetime import datetime
import random, barnum  # To generate random realistic data
from faker import Faker
from datetime import datetime
from datetime import timedelta

db = SQLAlchemy()


def seedData(app, db):
    app.security.datastore.db.create_all()
    if not app.security.datastore.find_role("Admin"):
        app.security.datastore.create_role(name="Admin")
    if not app.security.datastore.find_role("Staff"):
        app.security.datastore.create_role(name="Staff")
    if not app.security.datastore.find_user(email="admin@canarybank.com"):
        app.security.datastore.create_user(
            email="admin@canarybank.com",
            password=hash_password("password"),
            roles=["Admin"],
            GivenName="Admin",
            Surname="Adminson",
        )
    if not app.security.datastore.find_user(email="staff1@canarybank.com"):
        app.security.datastore.create_user(
            email="staff1@canarybank.com",
            password=hash_password("password"),
            roles=["Staff"],
            GivenName=createNameAsString(1),
            Surname=createNameAsString(2),
        )
    if not app.security.datastore.find_user(email="staff2@canarybank.com"):
        app.security.datastore.create_user(
            email="staff2@canarybank.com",
            password=hash_password("password"),
            roles=["Staff", "Admin"],
            GivenName=createNameAsString(1),
            Surname=createNameAsString(2),
        )
    app.security.datastore.db.session.commit()
