from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DATABASE_CLIENT = {
        'host': os.getenv('DATABASE_HOST'),
        'port': int(os.getenv('DATABASE_PORT')),
        'dbname': os.getenv('DATABASE_NAME'),
        'user': os.getenv('DATABASE_USERNAME'),
        'password': os.getenv('DATABASE_PASSWORD')
    }
    DATABASE_COMPETITOR = {
        'host': os.getenv('DATABASE_HOST'),
        'port': int(os.getenv('DATABASE_PORT')),
        'dbname': os.getenv('DATABASE_NAME_SECOND'),
        'user': os.getenv('DATABASE_USERNAME'),
        'password': os.getenv('DATABASE_PASSWORD')
    }
    SSH_CONFIG = {
        'host': os.getenv('SSH_HOST'),
        'port': int(os.getenv('SSH_PORT')),
        'user': os.getenv('SSH_USER'),
        'password': os.getenv('SSH_PASSWORD')
    }
    GURUFOKUS_API_KEY = os.getenv("GURUFOKUS_API_KEY")
    GURUFOKUS_API_HOST = os.getenv("GURUFOKUS_API_HOST")
    token = os.getenv("token")
    JWT_PRIVATE_KEY = os.getenv("JWT_PRIVATE_KEY").replace('\\n', '\n')
    JWT_PUBLIC_KEY = os.getenv("JWT_PUBLIC_KEY").replace('\\n', '\n')
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
