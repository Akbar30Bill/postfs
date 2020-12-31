def postfs_ls(cursor):
  cursor.execute('''
    select name from entity where path = (select pwd from env)
  ''')
  ls = cursor.fetchall()
  return ls
