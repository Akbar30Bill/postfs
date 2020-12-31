def postfs_init(cursor, config):
  cursor.execute('''
    create table entity(
      name text not null,
      path text not null,
      is_folder boolean default false not null,
      binary_data bytea default null,
      PRIMARY KEY (name, path, is_folder)
    )''')
  cursor.execute('''
    create table env(
      pwd text default '/'
    )''')
  cursor.execute('''
    insert into env (pwd) values ('/')
  ''')
