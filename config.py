# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'webapp.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

class Config:
    MYSQLDBName = "Avengers"
    MYSQL_user_name = "tonystart"
    MYSQL_password = "jarvis"
    SQLALCHEMY_DATABASE_URI =  "postgres://postgres:postgres@127.0.0.1:5432/temp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    secret_key_for_access_tokens = "HulkTheStrongestAvenger"


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 8081

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    # Local server uses default config
    'default': DevelopmentConfig
}
