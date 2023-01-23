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
    print "<form action='insert_pl_project_allocation.py' method='post'>"
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
    print "<li><i class='fa fa-th-list'></i>Task Allocated</li></ol></div></div>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody >"
    print "<tr><th  style='backGround-color:teal'><font color='white'><i class='icon_profile'></i>#</th>"
    print "<th  style='backGround-color:teal'><font color='white'>Project Manager</th>"
    print "<th  style='backGround-color:teal'><font color='white'>Team Leader Id</th>"
    print "<th  style='backGround-color:teal'><font color='white'>Project Name</th>"
    print "<th  style='backGround-color:teal'><font color='white'>Developer Id</th>"
    print "<th  style='backGround-color:teal'><font color='white'>Developer Name</th></tr>"
    if db:
        cursor=db.cursor()
        sql="select projectmanager,projectleader,projectname,projectdeveloper,developername from tbl_employee_allocation"
        flagid=0
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            flagid=flagid+1
            
            projectmanager=row[0]
            projectleader=row[1]
            projectname=row[2]
            developerid=row[3]
            developername=row[4]
            
            print "<tr><td>%d</td><td>%d</td>"%(flagid,projectmanager)
            print "<td>%s</td><td>%s</td><td>%d</td>"%(projectleader,projectname,developerid)
            print "<td>%s</td>"%(developername)
            print "</tr>"
    print "</tbody></table></section></div></div>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody>"
    print "<tr><th colspan=6 style='backGround-color:teal'><font color=white>Task Allocated and Pending</font></th></tr>"
    print "<tr><th><i class='icon_profile'></i>#</th><th>Token No</th>"
    print "<th>Employee Id</th>"
    print "<th>Employee Name</th>"
    print "<th>Task</th><th>Task Date</th></tr>"
    if db:
        cursor=db.cursor()
        sql="select tokenno,empid,empname,task,taskdate from tbl_task where status=0"
        flagid=0
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            flagid=flagid+1
            tokenno=row[0]
            empid=row[1]
            employeename=row[2]
            task=row[3]
            taskdate=row[4]
            print "<tr><td>%d</td><td>%d</td><td>%d</td>"%(flagid,tokenno,empid)
            print "<td>%s</td><td>%s</td>"%(employeename,task)
            print "<td>%s</td></tr>"%(taskdate)
    

            
    print "</tbody></table></section></div></div>"

    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody>"
    print "<tr><th colspan=7 style='backGround-color:teal'><font color=#fffff>Task Allocated and Completed</font></th></tr>"
    print "<tr><th><i class='icon_profile'></i>#</th><th>Token No</th>"
    print "<th>Employee Id</th>"
    print "<th>Employee Name</th>"
    print "<th>Task</th><th>Task Date</th><th>Completion Date</tr>"
    if db:
        cursor=db.cursor()
        sql="select tokenno,empid,empname,task,taskdate,completiondate from tbl_task where status=1"
        flagid=0
        if(cursor.execute(sql)>0):
            results=cursor.fetchall()
            for row in results:
                flagid=flagid+1
                tokenno=row[0]
                empid=row[1]
                employeename=row[2]
                task=row[3]
                taskdate=row[4]
                completiondate=row[5]
                print "<tr><td>%d</td><td>%d</td><td>%d</td>"%(flagid,tokenno,empid)
                print "<td>%s</td><td>%s</td>"%(employeename,task)
                print "<td>%s</td><td>%s</td></tr>"%(taskdate,completiondate)
        else:
            print "<tr><th colspan=7><center>No Allocated Task Completed Yet</center></th></tr>"
            

            
    print "</tbody></table></section></div></div>"
    
    print "</section></section>"
    print "<div class='text-right'>"
    print "<div class='credits'></div></div></section>"
    print "</form>"
    print "</body>"
    print "</html>"
