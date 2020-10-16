import psycopg2
import os

def getpwd():
    return open('./POSTFSPWD', 'r').read()
def whoami():
    return os.popen('whoami').read()[:-1]

def runq(query, result_type=0, user=whoami()):
    print(query)
    try:
        connection = psycopg2.connect(user = user,
                                      password = "",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "postfs")
        cursor = connection.cursor()
        cursor.execute(query)
        record = []
        if(connection):
            if result_type > 0:
                record = cursor.fetchall()
            cursor.close()
            connection.commit()
            connection.close()
            return record
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
def grant(user):
    runq(f'GRANT ALL PRIVILEGES ON DATABASE postfs TO {user};', user='postgres')
