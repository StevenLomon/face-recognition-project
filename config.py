import os


class ConfigDebug:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://steven:Killzone1@python22steven.mysql.database.azure.com/bank2.0"  # File-based SQL database
    SECRET_KEY = "SDFA11#"
    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT", "996196728467290652074888210601662039592"
    )
    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"

    # Flask-Mail SMTP server settings
    MAIL_SERVER = "127.0.0.1"
    MAIL_PORT = 1025
    MAIL_USE_SSL = False
    MAIL_USE_TLS = False
    MAIL_USERNAME = "email@example.com"
    MAIL_PASSWORD = "password"
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settingsa
    USER_APP_NAME = (
        "Flask-User Basic App"  # Shown in and email templates and page footers
    )
    USER_ENABLE_EMAIL = True  # Enable email aution
    USER_ENABLE_USERNAME = False  # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
