def postfs_rm(cursor, pathtofile):
  if pathtofile[0] == '/':  
    cursor.execute('''
      delete from entity where path || name = %s
    ''', [pathtofile])
  else:
    cursor.execute('''
      delete from entity where path || name = (select pwd from env) || %s
    ''', [pathtofile])
