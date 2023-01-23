#!/Python27/python.exe
print ("Content-type:text/html\r\n\r\n")
import cgi
import MySQLdb
form=cgi.FieldStorage()
username=form.getvalue('username')
password=form.getvalue('password')
email=form.getvalue('email')
dob=form.getvalue('dob')
gender=form.getvalue('gender')
address=form.getvalue('address')
city=form.getvalue('city')
pcode=form.getvalue('pcode')
mobile=form.getvalue('mobile')
keyskill=form.getvalue('keyskills')
qualification=form.getvalue('qualification')
doj=form.getvalue('doj')
employeetype=form.getvalue('employeetype')
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    try:
        cursor=db.cursor()
        selectQuery="select * from tbl_employee where mailid='%s' and mobilenumber='%s'"%(email,mobile)
        if(cursor.execute(selectQuery)>0):
            print "<script>alert('Already Exists');location.href='view_employee.py';</script>"
        else:
            select="select ifnull(max(userid),0) from tbl_employee"
            cursor.execute(select)
            results=cursor.fetchall()
            for row in results:
                userid=row[0]+1
            status="nothing"
            query="insert into tbl_employee(userid,username,password,mailid,dateofbirth,gender,address,city,pincode,mobilenumber,keyskill,qualification,dateofjoin,status,emptype) values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(userid,username,password,email,dob,gender,address,city,pcode,mobile,keyskill,qualification,doj,status,employeetype)
            cursor.execute(query)
            db.commit()
            print "<script>alert('Inserted Successfully');location.href='view_employee.py';</script>"
    except:
        db.rollback()
        print "<script>alert('Error in Inserting');location.href='add_employee.py';</script>"
else:
    print "Not Connected to Database" 
