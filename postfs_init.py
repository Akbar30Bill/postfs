def postfs_init(connection, config):
  cursor = connection.cursor()
  cursor.execute('''
    create table entity(
      path text primary key,
      is_folder boolean default false not null,
      binary_data bytea default null,
    )''')
  cursor.execute('''
    create table env(
      pwd text default '/'
    )''')
  cursor.commit()
  cursor.close()
