#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    cursor=db.cursor()
    try:
        sql="delete from tbl_session"
        cursor.execute(sql)
        db.commit()
        print "<script>location.href='index.py';</script>"
        
    except:
        db.rollback()
else:
    print "Error in Db Connection"
