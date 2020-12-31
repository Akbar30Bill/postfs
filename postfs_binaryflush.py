def postfs_binaryflush(cursor, pathtofile, filename = None):
  if not filename:
    filename = pathtofile[pathtofile.rindex('/') if pathtofile.rindex('/') else 0:]
  fileb = open(pathtofile, 'rb').read()
  cursor.execute('''
    insert into entity (
      name, path, is_folder, binary_data
    ) values (
      %s,
      (select pwd from env),
      false,
      %s
    )
  ''', [pathtofile, fileb])