#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
form=cgi.FieldStorage()
userid=form.getvalue('a')

if db:
    cursor=db.cursor()
    sql="select sessionid from tbl_session"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        sessionid=row[0]
if sessionid=="":
    print "<script>location.href='index.py';</script>"
else:   
    print "<html>"
    print "<head>"
    print "<meta charset='utf-8'>"
    print "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    print "<link rel='shortcut icon' href='img/favicon.png'>"
    print "<title> </title>"
    import JcLink
    print "</head>"
    print "<body>"
    print "<form action='insert_feedback.py' name='feedback' method='post'>"
    print "<section id='container' class=''>"
    import Header     
    print "<aside>"
    print "<div id='sidebar'  class='nav-collapse '>"
    print "<ul class='sidebar-menu'>"
    print "<li class=''>"
    print "<a class='' href='index.py '>"
    print "<i class='icon_house_alt'></i>"
    print "<span>Dashboard</span></a></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>Allocation</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='PLpage.py' active>Developer Allocation</a></li>"                          
    print "<li><a class='' href='pl_project_allocation.py'>Project Allocation</a></li>"
    print "<li><a class='' href='pl_token_allocation.py'>Token Allocation</a></li>"
    print "</ul></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>View</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='pl_view_token_allocation.py'>View Token Allocated</a></li>"                          
    print "</ul></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>FeedBack</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='pm_give_feedback.py'>Feed Back Analysis</a></li>"                          
    print "</ul></li></ul>"
    print "</div>"
    print "</aside>"
    print "<section id='main-content'>"
    print "<section class='wrapper'>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<h3 class='page-header'><i class='fa fa-table'></i> PROJECT DEVELOPER</h3>"
    print "<ol class='breadcrumb'>"
    print "<li><i class='fa fa-home'></i><a href='PLpage.py'>Home</a></li>"
    print "<li><i class='fa fa-table'></i>Allocation</li>"
    print "<li><i class='fa fa-th-list'></i>PD Allocation</li></ol></div></div>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody>"
    print "<tr><th><i class='icon_profile'></i>#</th>"
    print "<th><i class='icon_calendar'></i> Developer Id</th>"
    print "<th><i class='icon_mail_alt'></i>Developer Name</th>"
    print "<th><i class='icon_mobile'></i> Mail Id</th>"
    print "<th><i class='icon_cogs'></i> Mobile</th>"
    print "<th><i class='icon_cogs'></i> Key Skill</th>"
    print "<th><i class='icon_cogs'></i> Qualification</th></tr>"
    if db:
        
        cursor=db.cursor()
        flagid=0
        
        sql2="select userid,username,mailid,mobilenumber,keyskill,qualification from tbl_employee where userid=%d"%(int(userid))
        
        cursor.execute(sql2)
        results=cursor.fetchall()
        for row in results:
            projectdeveloper=row[0]
            developername=row[1]
            mailid=row[2]
            mobile=row[3]
            keyskill=row[4]
            qualification=row[5]
            flagid=flagid+1
           
            print "<tr><td>%d</td><td><input type='text' name='developerid' value=%d readonly></td>"%(flagid,int(projectdeveloper))
            print "<td><input type='text' name='developername' value='%s' readonly></td><td>%s</td>"%(developername,mailid)
            print "<td>%s</td><td>%s</td>"%(mobile,keyskill)
            print "<td>%s</td>"%(qualification)
            print "</td></tr>"
    print "</tbody></table></section></div></div>"
    print """
<table border style="width:100%; height:30%">
<tr><td><b>NUMERACY</b></td><td>Very Good</td><td>Good</td><td>Adequate</td></tr>
 <tr><td>Simple calculations</td><td><input type="radio" name=r1 value="5"></td><td><input type="radio" name=r1 value="4"" ></td><td><input type="radio" name=r1 value="3" ></td></tr>
<tr><td>More complex calculations</td><td><input type="radio" name=r2 value="5"></td><td><input type="radio" name=r2 value="4"" ></td><td><input type="radio" name=r2 value="3" ></td></tr>
<tr><td>Interpret graphs,Charts and Tables</td><td><input type="radio" name=r3 value="5"></td><td><input type="radio" name=r3 value="4"" ></td><td><input type="radio" name=r3 value="3" ></td></tr>
<tr><td>Prepare Graphs, charts and tables to convey information</td><td><input type="radio" name=r4 value="5"></td><td><input type="radio" name=r4 value="4"" ></td><td><input type="radio" name=r4 value="3" ></td></tr>
<tr><td>Presentations</td><td><input type="radio" name=r5 value="5"></td><td><input type="radio" name=r5 value="4"" ></td><td><input type="radio" name=r5 value="3" ></td></tr>
<tr><td>Problem solving capability</td><td><input type="radio" name=r6 value="5"></td><td><input type="radio" name=r6 value="4"" ></td><td><input type="radio" name=r6 value="3" ></td></tr>
</table>
<br><br>
<table border style="width:100%; height:30%">
<tr><td><b>COMMUNICATION SKILLS</b></td><td>Very Good</td><td>Good</td><td>Adequate</td></tr>
 <tr><td>composing own letter</td><td><input type="radio" name=r7 value="5"></td><td><input type="radio" name=r7 value="4"" ></td><td><input type="radio" name=r7 value="3" ></td></tr>
<tr><td>Taking notes in meetings and minutes</td><td><input type="radio" name=r8 value="5"></td><td><input type="radio" name=r8 value="4"" ></td><td><input type="radio" name=r8 value="3" ></td></tr>
<tr><td>Explain complex things</td><td><input type="radio" name=r9 value="5"></td><td><input type="radio" name=r9 value="4"" ></td><td><input type="radio" name=r9 value="3" ></td></tr>
<tr><td>Lead a group discussion</td><td><input type="radio" name=r10 value="5"></td><td><input type="radio" name=r10 value="4"" ></td><td><input type="radio" name=r10 value="3" ></td></tr>
<tr><td>Creatively explaining the Presentations</td><td><input type="radio" name=r11 value="5"></td><td><input type="radio" name=r11 value="4"" ></td><td><input type="radio" name=r11 value="3" ></td></tr>
<tr><td>Gesture while explaining the project details</td><td><input type="radio" name=r12 value="5"></td><td><input type="radio" name=r12 value="4"" ></td><td><input type="radio" name=r12 value="3" ></td></tr>
</table>
<br><br>
<table border style="width:100%; height:30%">
<tr><td><b>INFORMATION TECHNOLOGY</b></td><td>Very Good</td><td>Good</td><td>Adequate</td></tr>
 <tr><td>Microsoft office Word Usage</td><td><input type="radio" name=r13 value="5"></td><td><input type="radio" name=r13 value="4"" ></td><td><input type="radio" name=r13 value="3" ></td></tr>
<tr><td>Excel Spreadsheet Usage</td><td><input type="radio" name=r14 value="5"></td><td><input type="radio" name=r14 value="4"" ></td><td><input type="radio" name=r14 value="3" ></td></tr>
<tr><td>Database Usage</td><td><input type="radio" name=r15 value="5"></td><td><input type="radio" name=r15 value="4"" ></td><td><input type="radio" name=r15 value="3" ></td></tr>
<tr><td>Desktop publishing</td><td><input type="radio" name=r16 value="5"></td><td><input type="radio" name=r16 value="4"" ></td><td><input type="radio" name=r16 value="3" ></td></tr>
<tr><td>Update Intranet and internet pages</td><td><input type="radio" name=r17 value="5"></td><td><input type="radio" name=r17 value="4"" ></td><td><input type="radio" name=r17 value="3" ></td></tr>
<tr><td>E-mail Usage</td><td><input type="radio" name=r18 value="5"></td><td><input type="radio" name=r18 value="4"" ></td><td><input type="radio" name=r18 value="3" ></td></tr>
<tr><td>Internet Usage</td><td><input type="radio" name=r19 value="5"></td><td><input type="radio" name=r19 value="4"" ></td><td><input type="radio" name=r19 value="3" ></td></tr>
</table>
<br><br>
<table border style="width:100%; height:30%">
<tr><td><b>Personal skills</b></td><td>Very Good</td><td>Good</td><td>Adequate</td></tr>
 <tr><td>Positive Attitude</td><td><input type="radio" name=r20 value="5"></td><td><input type="radio" name=r20 value="4"" ></td><td><input type="radio" name=r20 value="3" ></td></tr>
<tr><td>Ressilence</td><td><input type="radio" name=r21 value="5"></td><td><input type="radio" name=r21 value="4"" ></td><td><input type="radio" name=r21 value="3" ></td></tr>
<tr><td>Team work</td><td><input type="radio" name=r22 value="5"></td><td><input type="radio" name=r22 value="4"" ></td><td><input type="radio" name=r22 value="3" ></td></tr>
<tr><td>Thinking skills</td><td><input type="radio" name=r23 value="5"></td><td><input type="radio" name=r23 value="4"" ></td><td><input type="radio" name=r23 value="3" ></td></tr>
<tr><td>Self management</td><td><input type="radio" name=r24 value="5"></td><td><input type="radio" name=r24 value="4"" ></td><td><input type="radio" name=r24 value="3" ></td></tr>
<tr><td>Volunteering thought</td><td><input type="radio" name=r25 value="5"></td><td><input type="radio" name=r25 value="4"" ></td><td><input type="radio" name=r25 value="3" ></td></tr>
<tr><td>Willingness to learn new things</td><td><input type="radio" name=r26 value="5"></td><td><input type="radio" name=r26 value="4"" ></td><td><input type="radio" name=r26 value="3" ></td></tr>
</table>
<br><br>
<table border style="width:100%; height:30%">
<tr><td><b>Error Occurences in Task</b></td><td>Very Good</td><td>Good</td><td>Adequate</td></tr>
<tr><td>Compile Error</td><td><input type="radio" name=r27 value="5"></td><td><input type="radio" name=r27 value="4"" ></td><td><input type="radio" name=r27 value="3" ></td></tr>
<tr><td>Runtime Error</td><td><input type="radio" name=r28 value="5"></td><td><input type="radio" name=r28 value="4"" ></td><td><input type="radio" name=r28 value="3" ></td></tr>
<tr><td>Capability of Solving Error</td><td><input type="radio" name=r29 value="5"></td><td><input type="radio" name=r29 value="4"" ></td><td><input type="radio" name=r29 value="3" ></td></tr>
<tr><td>Logical Error</td><td><input type="radio" name=r30 value="5"></td><td><input type="radio" name=r30 value="4"" ></td><td><input type="radio" name=r30 value="3" ></td></tr>
<tr><td>Abstract Thinking to Solve Error</td><td><input type="radio" name=r31 value="5"></td><td><input type="radio" name=r31 value="4"" ></td><td><input type="radio" name=r31 value="3" ></td></tr>
</table>

    """
    print "</section></section>"
    print "<p align=center><input type='submit' name='submit' value='Give FeedBack'></p>"
    print "<br><br>"
    print "</section>"
    print "</form>"
    print "</body>"
    print "</html>"
