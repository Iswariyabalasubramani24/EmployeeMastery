#!/Python27/python.exe
print ("Content-type:text/html\r\n\r\n")
import cgi
import MySQLdb
form=cgi.FieldStorage()
projectname=form.getvalue('projectname')
codinglanguage=form.getvalue('codinglanguage')
databasename=form.getvalue('databasename')
duration=form.getvalue('duration')
registerdate=form.getvalue('registerdate')
desc=form.getvalue('desc')
desc=desc.replace("'","")
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    try:
        cursor=db.cursor()
        selectQuery="select * from tbl_projectregister where projectname='%s' and codinglanguage='%s' and databasename='%s'"%(projectname,codinglanguage,databasename)
        if(cursor.execute(selectQuery)>0):
            print "<script>alert('Already Exists');location.href='view_project.py';</script>"
        else:
            select="select ifnull(max(projectid),0) from tbl_projectregister"
            cursor.execute(select)
            results=cursor.fetchall()
            for row in results:
                projectid=row[0]+1
            query="insert into tbl_projectregister(projectid,projectname,codinglanguage,databasename,duration,registerdate,description) values(%d,'%s','%s','%s','%s','%s','%s')"%(projectid,projectname,codinglanguage,databasename,duration,registerdate,desc)
            cursor.execute(query)
            db.commit()
            print "<script>alert('Inserted Successfully');location.href='view_project.py';</script>"
    except:
        db.rollback()
        print "<script>alert('Error in Inserting');location.href='add_project.py';</script>"
else:
    print "Not Connected to Database" 
