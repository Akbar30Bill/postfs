def postfs_touch (cursor, filename):
  cursor.execute('''
    insert into entity (
      name, path, is_folder, binary_data
    ) values (
      %s,
      (select pwd from env),
      false,
      ''
    )
  ''', [filename])