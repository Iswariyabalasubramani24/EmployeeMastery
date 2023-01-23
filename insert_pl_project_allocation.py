#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    cursor=db.cursor()
    sql="select sessionid from tbl_session"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        sessionid=row[0]
if sessionid=="":
    print "<script>alert('session is expired');location.href='index.py';</script>"
else:
    form=cgi.FieldStorage()
    tlid=form.getvalue('tlid')
    empid=form.getvalue('empid')
    cursor=db.cursor()
##    print tlid,empid
    tlidQuery="select * from tbl_teamleader_allocation where tlallocationid=%d"%(int(tlid))
##    print tlidQuery
    cursor.execute(tlidQuery)
    result=cursor.fetchall()
    for row in result:
        alid=row[0]
        pm=row[1]
        pl=row[2]
        pn=row[3]
        code=row[4]
        teamsize=row[5]
        duration=row[6]
##        print alid,pm,pl,pn,code,teamsize,duration
    empcount=0
    for i in empid:
        select="select userid,username,keyskill from tbl_employee where userid=%d"%(int(i))
        if(cursor.execute(select)>0):
            results=cursor.fetchall()
            for row in results:
                empid=row[0]
                empname=row[1]
                keyskill=row[2]
                select="select * from tbl_employee_allocation where projectname='%s' and code='%s' and projectdeveloper=%d and developername='%s'"%(pn,code,int(empid),empname)
                if(cursor.execute(select)>0):
                    print "<script>alert('already alocated to %s')</script>"%(empid)
                else:
                    insert="insert into tbl_employee_allocation values(%d,%d,'%s','%s',%d,'%s','%s',%d,'%s')"%(int(pm),int(pl),pn,code,int(empid),empname,keyskill,int(teamsize),duration)
                    if(cursor.execute(insert)>0):
                        empcount=empcount+1
                        db.commit()
    if(empcount!=0):
        print "<script>alert('allocated successfully');location.href='pl_project_allocation.py';</script>"
    else:
        print "<script>alert('allocation failed');location.href='pl_project_allocation.py';</script>"
        #empid,empname,keyskill
        
       
    
        
    
