import psycopg2
import getpass
import sys

sql = """insert query here"""

pa = getpass.getpass()


conn_string = "host='' dbname='' user='' password='{0}'".format(pa)

print "Connecting to database\n	->%s" % (conn_string)

try:
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()

    print row

    cursor.close()
    conn.close()

except Exception as e: print(e)

#once the connection works, you can write your statement to insert the data


raw_input()

