#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
form=cgi.FieldStorage();
username=form.getvalue("username")
password=form.getvalue("password")
usertype=form.getvalue("usertype")
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    cursor=db.cursor()
    if usertype=="Admin":
        sql="select * from tbl_admin where  username='%s' and password='%s'"%(username,password)
        if(cursor.execute(sql)>0):
            try:
                insert="insert into tbl_session values('%s','%s')"%(username,usertype)
                cursor.execute(insert)
                db.commit()
                print "<script>alert('Login is Success');location.href='mainpage.py';</script>"    
            except:
                db.rollback()
        else:
            print "<script>alert('Login is Failed');location.href='index.py';</script>"
    elif usertype=="PM":
        sql="select * from tbl_employee where  username='%s' and password='%s' and emptype='%s'"%(username,password,usertype)
        if(cursor.execute(sql)>0):
            try:
                insert="insert into tbl_session values('%s','%s')"%(username,usertype)
                cursor.execute(insert)
                db.commit()
                print "<script>alert('Login is Success');location.href='PMpage.py';</script>"
            except:
                db.rollback()
        else:
            print "<script>alert('Login is Failed');location.href='index.py';</script>"
          
    elif usertype=="PL":
        sql="select * from tbl_employee where  username='%s' and password='%s' and emptype='%s'"%(username,password,usertype)
        if(cursor.execute(sql)>0):
            try:
                insert="insert into tbl_session values('%s','%s')"%(username,usertype)
                cursor.execute(insert)
                db.commit()
                print "<script>alert('Login is Success');location.href='PLpage.py';</script>"
            except:
                db.rollback()
        else:
            print "<script>alert('Login is Failed');location.href='index.py';</script>"            
    elif usertype=="PD":
        sql="select * from tbl_employee where  username='%s' and password='%s' and emptype='%s'"%(username,password,usertype)
        if(cursor.execute(sql)>0):
            try:
                insert="insert into tbl_session values('%s','%s')"%(username,usertype)
                cursor.execute(insert)
                db.commit()
                print "<script>alert('Login is Success');location.href='PDpage.py';</script>"
            except:
                db.rollback()
        else:
            print "<script>alert('Login is Failed');location.href='index.py';</script>"        
    else:
        print "<script>alert('Login is Failed');location.href='index.py';</script>"        
        
else:
    print "Error in Db Connection"
