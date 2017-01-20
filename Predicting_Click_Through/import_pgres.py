#
from sys import argv
import psycopg2
import csv

# sets argv with filename to be imported
script, load = argv


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
(uuid varchar, document_id bigint, tstamp bigint, platform integer,
 geo_location varchar, traffic_source integer)""")


# expression to pass row of csv file to db
passData = """INSERT INTO page_views (uuid, document_id, tstamp, platform,
geo_location,traffic_source)
VALUES (%s, %s, %s, %s, %s, %s);"""

# Opens tsv file (specified in argv) to be read into database
with open (load,'r') as f:
    count = 0
    reader = csv.reader(f, delimiter=',')
    reader.next() # skips header row
    for row in reader:
        count += 1
        csvline = row
        for item in range(len(csvline)): #change '' to None
            if csvline[item] == "":
                csvline[item] = None
        try:
            cur.execute(passData, csvline)
        except:
            print(count)

print(count)
# commit to database changes
conn.commit()

#close cursor and connection
cur.close()
conn.close()
