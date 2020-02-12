import MySQLdb
db = MySQLdb.connect("localhost","kaung","hello","sensor_data" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s " % data
db.close()
