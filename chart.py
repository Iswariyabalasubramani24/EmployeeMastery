import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
cursor=db.cursor()
username=[]
numeracy=[]
comm=[]
inftech=[]
pskill=[]
marksec=[]
select="select userid from tbl_feedback"
if(cursor.execute(select)>0):
    results=cursor.fetchall()
    for row in results:
        uid=row[0]
        select="select username,numeracy,communication,informationtechnology,personalskill,marksecured from tbl_feedback where userid=%d"%(int(uid))
        if(cursor.execute(select)>0):
            results=cursor.fetchone()
            uname=results[0]
            num=results[1]
            com=results[2]
            inf=results[3]
            perskill=results[4]
            msec=results[5]
            username.append(uname)
            numeracy.append(int(num))
            comm.append(int(com))
            inftech.append(int(inf))
            pskill.append(int(perskill))
            marksec.append(int(msec))
            
            
            
import pygal
from pygal.style import Style
for i in range(len(username)):
    custom_style = Style(colors=('#E80080', '#404040','#9BC850','#7af442','#415cf4'))
    b_chart = pygal.Bar(style=custom_style)
    b_chart.title = "Employee Performance"
    b_chart.y_labels = 0,10,20,30,40,50,60,70,80,90,100
    b_chart.add("Numeracy",numeracy[i])
    b_chart.add("Communication",comm[i])
    b_chart.add("Information Technology",inftech[i])
    b_chart.add("Personal Skill",pskill[i])
    b_chart.add("Overall",marksec[i])
    chart=username[i]+".svg"
    b_chart.render_to_file(chart)
