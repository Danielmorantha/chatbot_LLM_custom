import psycopg2
from contextlib import contextmanager
from sshtunnel import SSHTunnelForwarder
from app.config import Config

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.ssh_config = Config.SSH_CONFIG

    @contextmanager
    def get_connection(self):
        tunnel = SSHTunnelForwarder(
            (self.ssh_config['host'], self.ssh_config['port']),
            ssh_username=self.ssh_config['user'],
            ssh_password=self.ssh_config['password'],
            remote_bind_address=(self.db_config['host'], self.db_config['port'])
        )
        tunnel.start()

        conn = psycopg2.connect(
            dbname=self.db_config['dbname'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            host=self.db_config['host'],
            port=tunnel.local_bind_port
        )
        try:
            yield conn
        finally:
            conn.close()
            tunnel.stop()
