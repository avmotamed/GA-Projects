from sys import argv
import psycopg2
import csv
import sys

# sets argv with filename to be imported
script, source = argv


# Column names for page_views table
column_names = ['uuid', 'document_id', 'tstamp', 'platform', 'geo_location',\
'traffic_source']


#Define connection string
conn_string = "host='localhost' dbname='outbrain' user='postgres'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cur = conn.cursor()

# creates table it it does not already exsit
cur.execute("""CREATE TABLE IF NOT EXISTS page_views
(uuid varchar, document_id bigint, tstamp integer, platform integer,
 geo_location varchar, traffic_source integer)""")

print "page_views table created"

f = None

try:
    f = open(source, 'r')
    cur.copy_from(f, 'page_views', sep=",")
    conn.commit()

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error db %s' % e
    sys.exit(1)

except IOError, e:
    if conn:
        conn.rollback()
    print 'Error io %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
    if f:
        f.close()



# commit to database changes
# conn.commit()

#close cursor and connection
cur.close()
# conn.close()
