def postfs_mkdir(cursor, directory):
  cursor.execute('''
    insert into entity (
      name, path, is_folder, binary_data
    ) values (
      %s,
      (select pwd from env),
      true,
      null
    )
  ''', [directory])
