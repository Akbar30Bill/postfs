import sys
import psycopg2
from postfs_init import *
from postfs_cd import *
from postfs_mkdir import *
from postfs_touch import *
from postfs_ls import *
from postfs_rm import *
from postfs_binaryflush import *
from postfs_binarypull import *

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
  def run_in_transaction(self, cursor, op, cmd):
    print(op, cmd)
    if op == 'init':
      postfs_init(cursor, None)
    elif op == 'cd':
      postfs_cd(cursor, cmd[0])
    elif op == 'mkdir':
      postfs_mkdir(cursor, cmd[0])
    elif op == 'touch':
      postfs_touch(cursor, cmd[0])
    elif op == 'ls':
      print(postfs_ls(cursor))
    elif op == 'rm':
      postfs_rm(cursor, cmd[0])
    elif op == 'upload':
      postfs_binaryflush(cursor, cmd[0], cmd[1])
    elif op == 'download':
      postfs_binarypull(cursor, cmd[0], cmd[1])
  def run(self):
    cursor = self.connection.cursor()

    if self.op == 'start-transaction':
      while True:
        cmd = input('#> ').split()
        if cmd[0] == 'commit':
          self.connection.commit()
          cursor.close()
          return
        elif cmd[0] == 'abort':
          self.connection.rollback()
          cursor.close()
          return
        else:
          self.run_in_transaction(cursor, cmd[0], cmd[1:])
    else:
      self.run_in_transaction(cursor, self.op, self.cmd[2:])

    self.connection.commit()
    cursor.close()

cmd = command(sys.argv)
cmd.run()
