import sys
import psycopg2
from postfs_init import *

class command:
  def __init__(self, sysargs):
    self.connection = psycopg2.connect(user="postgres",
                                  password="pynative@#29",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    self.cmd = sysargs
    self.name = sysargs[0]
    self.op = sysargs[1]
  def run(self):
    if self.op == 'init':
      postfs_init(self.connection, None)
      
