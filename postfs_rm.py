def postfs_rm(cursor, pathtofile):
  if pathtofile[0] == '/':
    cursor.execute('''
      delete from entity where path || name like %s || '/%%'
                                or path || name = %s
    ''', [pathtofile, pathtofile])
  else:
    cursor.execute('''
      delete from entity where path || name like (select pwd from env) || %s || '/%%'
                                or path || name = (select pwd from env) || %s 
    ''', [pathtofile, pathtofile])
