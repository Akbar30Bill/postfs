def postfs_binarypull(cursor, filename, pathtodest):
  path_is_absolute = filename[0] == '/'
  if path_is_absolute:
    cursor.execute('''
      select binary_data from entity where path || name = %s
    ''', [filename])
  else:
    cursor.execute('''
      select binary_data from entity where path || name = (select pwd from env) || %s
    ''', [filename])

  bdata = cursor.fetchone()[0].tobytes()
  f = open(pathtodest, 'wb')
  f.write(bdata)
  f.close()
