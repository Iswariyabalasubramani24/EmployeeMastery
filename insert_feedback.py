#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
form=cgi.FieldStorage()
userid=form.getvalue('developerid')
username=form.getvalue('developername')
numeracy1=form.getvalue('r1')
numeracy2=form.getvalue('r2')
numeracy3=form.getvalue('r3')
numeracy4=form.getvalue('r4')
numeracy5=form.getvalue('r5')
numeracy6=form.getvalue('r6')
totalnumeracy=int(numeracy1)+int(numeracy2)+int(numeracy3)+int(numeracy4)+int(numeracy5)+int(numeracy6)
averagenumeracy=100*totalnumeracy/30


communication1=form.getvalue('r7')
communication2=form.getvalue('r8')
communication3=form.getvalue('r9')
communication4=form.getvalue('r10')
communication5=form.getvalue('r11')
communication6=form.getvalue('r12')

totalcomminucation=int(communication1)+int(communication2)+int(communication3)+int(communication4)+int(communication5)+int(communication6)
averagecommunication=100*totalcomminucation/30

informationtechnology1=form.getvalue('r13')
informationtechnology2=form.getvalue('r14')
informationtechnology3=form.getvalue('r15')
informationtechnology4=form.getvalue('r16')
informationtechnology5=form.getvalue('r17')
informationtechnology6=form.getvalue('r18')
informationtechnology7=form.getvalue('r19')
totalit=int(informationtechnology1)+int(informationtechnology2)+int(informationtechnology3)+int(informationtechnology4)+int(informationtechnology5)+int(informationtechnology6)+int(informationtechnology7)
averageit=100*totalit/35

personalskill1=form.getvalue('r20')
personalskill2=form.getvalue('r21')
personalskill3=form.getvalue('r22')
personalskill4=form.getvalue('r23')
personalskill5=form.getvalue('r24')
personalskill6=form.getvalue('r25')
personalskill7=form.getvalue('r26')
totalpskill=int(personalskill1)+int(personalskill2)+int(personalskill3)+int(personalskill4)+int(personalskill5)+int(personalskill6)+int(personalskill7)
averageskill=100*totalpskill/35

error1=form.getvalue('r27')
error2=form.getvalue('r28')
error3=form.getvalue('r29')
error4=form.getvalue('r30')
error5=form.getvalue('r31')
totalEskill=int(error1)+int(error2)+int(error3)+int(error4)+int(error5)
averageEskill=100*totalEskill/25


totalskill=averagenumeracy+averagecommunication+averageit+averageskill+averageEskill
averagetotalskill=totalskill/5



if db:
    cursor=db.cursor()
    sql="select sessionid from tbl_session"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        sessionid=row[0]
else:
    print "<script>alert('Database is not connected');location.href='pm_give_feedback.py.py';</script>"

if sessionid=="":
    print "<script>alert('session is expired');location.href='index.py';</script>"
else:
    select="select ifnull(max(fid),0) from tbl_feedback"
    cursor.execute(select)
    results=cursor.fetchall()
    for row in results:
        fid=row[0]+1
    existsquery="select * from tbl_feedback where userid=%d"%(int(userid))
    if(cursor.execute(existsquery)>0):
        print "<script>alert('Already feedback is given');location.href='pm_give_feedback.py';</script>"
    else:
        try:
            insertquery="insert into tbl_feedback values(%d,%d,'%s',%d,%d,%d,%d,%d,%d)"%(int(fid),int(userid),username,int(averagenumeracy),int(averagecommunication),int(averageit),int(averageskill),int(averageEskill),int(averagetotalskill))
            cursor.execute(insertquery)
            db.commit()
            print "<script>alert('feedback is inserted');location.href='pm_give_feedback.py';</script>"
        except:
            db.rollback()
            print "<script>alert('error in inserting feedback');location.href='pm_give_feedback.py';</script>"
