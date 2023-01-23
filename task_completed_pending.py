#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
import datetime
today=datetime.datetime.now()
dt=today.strftime("%d")
mn=today.strftime("%m")
yr=today.strftime("%Y")
fulldate="%s-%s-%s"%(dt,mn,yr)
form=cgi.FieldStorage()
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    cursor=db.cursor()
    sql="select sessionid from tbl_session"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        sessionid=row[0]
if(sessionid==""):
    print "<script>location.href='index.py';</script>"
else:
    username=form.getvalue("username")
    projectname=form.getvalue("projectname")
    tokennumber=form.getvalue("tokennumber")
    getpendingcode=form.getvalue("getpendingcode")
    continuependingcode=form.getvalue("continuependingcode")
    cbutton=form.getvalue("completedbutton")
    if cbutton=="Task Completed":
        try:
            updateQuery="update tbl_task set completedtask='%s',result='%s',completiondate='%s',status='%s' where projectname='%s' and tokenno=%d and empname='%s'"%(continuependingcode,'Completed',fulldate,'1',projectname,int(tokennumber),username)
            cursor.execute(updateQuery)
            db.commit()
            print "<script>alert('Updated Successfully');location.href='PDpage.py';</script>"
        except:
            db.rollback()
            print "<script>alert('Error in Updating');location.href='PDpage.py';</script>"
    if cbutton=="Task Pending":
        try:
            updateQuery="update tbl_task set completedtask='%s',result='%s',completiondate='%s',status='%s' where projectname='%s' and tokenno=%d and empname='%s'"%(continuependingcode,'Pending',fulldate,'0',projectname,int(tokennumber),username)
            cursor.execute(updateQuery)
            db.commit()
            print "<script>alert('Updated Successfully');location.href='PDpage.py';</script>"
        except:
            db.rollback()
            print "<script>alert('Error in Updating');location.href='PDpage.py';</script>"
