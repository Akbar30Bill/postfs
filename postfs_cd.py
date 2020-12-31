def postfs_cd(cursor, directory):
  if not directory:
    directory = '/'
  if directory[0] == '/':
    cursor.execute('''
      update env set pwd = %s
    ''', [directory])
  else:
    if directory[-1] != '/':
      directory += '/'
    cursor.execute('''
      update env set pwd = pwd || %s
    ''', [directory])
