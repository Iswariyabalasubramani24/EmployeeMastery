#!/Python27/python.exe
print ("Content-type:text/html\r\n\r\n")
import cgi
import MySQLdb
form=cgi.FieldStorage()
emailid=form.getvalue('q')
status=form.getvalue('r')

db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    try:
        cursor=db.cursor()
        select="update tbl_employee set status='%s' where mailid='%s'"%(status,emailid)
        cursor.execute(select)
        db.commit()
        print "<script>alert('Updated Successfully');location.href='view_projectmanager.py';</script>"
    except:
        db.rollback()
        print "<script>alert('Error in Updating');location.href='view_projectmanager.py';</script>"
else:
    print "Not Connected to Database" 
