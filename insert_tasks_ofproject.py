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
    
    empid=form.getvalue('empid')
    tno=form.getvalue('tno')
    task=form.getvalue('task')
    tdate=form.getvalue('tdate')


    
    cursor=db.cursor()
    
    
    empcount=0
    for i in empid:
        select="select projectname,projectdeveloper,developername from tbl_employee_allocation where projectdeveloper=%d"%(int(i))
        
        if(cursor.execute(select)>0):
            results=cursor.fetchall()
            for row in results:
                projectname=row[0]
                developerid=row[1]
                developername=row[2]
                x,y=projectname.split("-")
                
                existsQuery="select * from tbl_task where projectid=%d and projectname='%s' and empid=%d and empname='%s' and taskdate='%s'"%(int(x),y,int(developerid),developername,tdate)
                
                if(cursor.execute(existsQuery)>0):
                    print "<script>alert('Task Already allocated');location.href='pl_token_allocation.py';</script>"
                else:
                    
                    try:
                        insertQuery="insert into tbl_task(projectid,projectname,tokenno,empid,empname,task,taskdate) values(%d,'%s',%d,%d,'%s','%s','%s')"%(int(x),y,int(tno),int(developerid),developername,task,tdate)
                        
                        if(cursor.execute(insertQuery)>0):
                            empcount=empcount+1
                            db.commit()
                        else:
                            db.rollback()
                    except:
                        print "Error"
                        
                           
    if(empcount!=0):
        print "<script>alert('Task allocated successfully');location.href='pl_token_allocation.py';</script>"
    else:
        print "<script>alert('Error in allocating task');location.href='pl_token_allocation.py';</script>"
        
       
    
        
    
