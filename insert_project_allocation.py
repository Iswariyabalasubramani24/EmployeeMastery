#!/Python27/python.exe
print ("Content-type:text/html\r\n\r\n")
import cgi
import MySQLdb
form=cgi.FieldStorage()
projectmanager=form.getvalue('projectmanager')
projectname=form.getvalue('projectname')
projectleaderid=form.getvalue('plid')
duration=form.getvalue('duration')
members=form.getvalue('members')
codinglanguage=form.getvalue('code')
plid=projectleaderid.split('-')
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    try:
        cursor=db.cursor()
        selectQuery="select ifnull(max(tlallocationid),1000) from tbl_teamleader_allocation"
        cursor.execute(selectQuery)
        result=cursor.fetchone()
        postfix=int(result[0])+1
        tlallocationid=postfix
        existsQuery="select * from tbl_teamleader_allocation where projectmanager=%d and projectleader=%d and projectname='%s'"%(int(projectmanager),int(plid[0]),projectname)
        if(cursor.execute(existsQuery)>0):
             print "<script>alert('Already Allocated');location.href='project_allocation.py';</script>"
        else:
            query="insert into tbl_teamleader_allocation(tlallocationid,projectmanager,projectleader,projectname,code,teamsize,duration) values(%d,%d,%d,'%s','%s',%d,'%s')"%(int(tlallocationid),int(projectmanager),int(plid[0]),projectname,codinglanguage,int(members),duration)
            cursor.execute(query)
            db.commit()
            print "<script>alert('Inserted Successfully');location.href='project_allocation.py';</script>"
    except:
        db.rollback()
        print "<script>alert('Error in Inserting');</script>"
else:
    print "Not Connected to Database"
