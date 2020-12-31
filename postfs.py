import sys
import psycopg2
from postfs_init import *
from postfs_cd import *
from postfs_mkdir import *
from postfs_touch import *
from postfs_ls import * 

class command:
  def __init__(self, sysargs):
    self.connection = psycopg2.connect(user="alishahverdi",
                                  password="pynative@#29",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postfs")

    self.cmd = sysargs
    self.name = sysargs[0]
    self.op = sysargs[1]
  def run(self):
    cursor = self.connection.cursor()
    if self.op == 'init':
      postfs_init(cursor, None)
    elif self.op == 'cd':
      postfs_cd(cursor, self.cmd[2])
    elif self.op == 'mkdir':
      postfs_mkdir(cursor, self.cmd[2])
    elif self.op == 'touch':
      postfs_touch(cursor, self.cmd[2])
    elif self.op == 'ls':
      print(postfs_ls(cursor))

    self.connection.commit()
    cursor.close()

cmd = command(sys.argv)
cmd.run()
