#!/Python27/python.exe
print ("Content-type:text/html\r\n\r\n")
import cgi
import MySQLdb
form=cgi.FieldStorage()
emailid=form.getvalue('q')

db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    try:
        cursor=db.cursor()
        select="delete from tbl_employee where mailid='%s'"%(emailid)
        cursor.execute(select)
        db.commit()
        print "<script>alert('Deleted Successfully');location.href='view_employee.py';</script>"
    except:
        db.rollback()
        print "<script>alert('Error in Deleting');location.href='view_employee.py';</script>"
else:
    print "Not Connected to Database" 
