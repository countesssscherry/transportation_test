# DB_CONNECTION='mongodb://root:rootpassword@127.0.0.1:27017/transport?authSource=admin'
import os
DB_CONNECTION = os.environ["DB_CONNECTION"]