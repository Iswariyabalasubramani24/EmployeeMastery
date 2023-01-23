#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
form=cgi.FieldStorage()
empid=form.getvalue('q')
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
print "<link rel='shortcut icon' href='img/favicon.png'>"
print "<title> </title>"
import JcLink
print "</head>"
print "<body>"
print "<section id='container' class=''>"
import Header     
print "<aside>"
print "<div id='sidebar'  class='nav-collapse '>"
print "<ul class='sidebar-menu'>"
print "<li class=''>"
print "<a class='' href='mainpage.py '>"
print "<i class='icon_house_alt'></i>"
print "<span>Dashboard</span></a></li>"
print "<li class='sub-menu'>"
print "<a href='javascript:;' class=''>"
print "<i class='icon_document_alt'></i>"
print "<span>Employees</span>"
print "<span class='menu-arrow arrow_carrot-right'></span></a>"
print "<ul class='sub'>"
print "<li><a class='' href='add_employee.py'>Add Employee</a></li>"                          
print "<li><a class='' href='view_employee.py'>View Employee</a></li>"
print "<li><a class='' href='view_projectmanager.py'>View Project Manager</a></li>"
print "</ul></li>"
print "<li class='sub-menu'>"
print "<a href='javascript:;' class=''>"
print "<i class='icon_document_alt'></i>"
print "<span>Project Register</span>"
print "<span class='menu-arrow arrow_carrot-right'></span>"
print "</a>"
print "<ul class='sub'>"
print "<li><a class='' href='add_project.py'>Add Project</a></li>"
print "<li><a class='' href='view_project.py'>View Project</a></li>"
print "</ul></li>"
print "<li class='sub-menu'>"
print "<a href='javascript:;' class=''>"
print "<i class='icon_document_alt'></i>"
print "<span>Project Report</span>"
print "<span class='menu-arrow arrow_carrot-right'></span>"
print "</a>"
print "<ul class='sub'>"
print "<li><a class='' href='project_employee_report.py'>Employee Report</a></li>" # pending completed report
print "<li><a class='' href='project_leader_report.py'>Team Leader</a></li>" # empid,empname,keyskill,teamsize,duration
print "</ul></li>"
print "</ul></li></ul>"
# <!-- sidebar menu end-->
print "</div>"
print "</aside>"
print "<section id='main-content'>"
print "<section class='wrapper'>"
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<h3 class='page-header'><i class='fa fa-table'></i>Employees Report</h3>"
print "<ol class='breadcrumb'>"
print "<li><i class='fa fa-home'></i><a href='mainpage.py'>Home</a></li>"
print "<li><i class='fa fa-table'></i>Project Report</li>"
print "<li><i class='fa fa-th-list'></i>Employee Report</li></ol></div></div>"
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
    sql="select tokenno,empid,empname,task,taskdate from tbl_task where empid=%d and status=0"%(int(empid))
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
    sql="select tokenno,empid,empname,task,taskdate,completiondate from tbl_task where empid=%d and status=1"%(int(empid))
    
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
print "</body>"
print "</html>"
