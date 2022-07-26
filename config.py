import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__)) #grab root directory path. Resistant to directory changes providing this config file stays in root

class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') #pulling secret key from .env file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'todo.db') #grab database url, or create sqlite database if one doesnt exist
    SQLALCHEMY_TRACK_MODIFICATIONS = False #stop track modifications on database (think streaming in snowflake)