#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
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
print "<h3 class='page-header'><i class='fa fa-table'></i> View Employees</h3>"
print "<ol class='breadcrumb'>"
print "<li><i class='fa fa-home'></i><a href='mainpage.py'>Home</a></li>"
print "<li><i class='fa fa-table'></i>Employee</li>"
print "<li><i class='fa fa-th-list'></i>View Employee</li></ol></div></div>"
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<section class='panel'>"
print "<table class='table table-striped table-advance table-hover'>"
print "<tbody>"
print "<tr><th><i class='icon_profile'></i>#</th><th><i class='icon_profile'></i>User Id</th>"
print "<th><i class='icon_calendar'></i> User Name</th>"
print "<th><i class='icon_mail_alt'></i>Email id</th>"
print "<th><i class='icon_pin_alt'></i> Mobile </th>"
print "<th><i class='icon_mobile'></i> Key Skill</th>"
print "<th><i class='icon_mobile'></i> EmpType</th>"
print "<th><i class='icon_cogs'></i> Action</th></tr>"
if db:
    cursor=db.cursor()
    sql="select userid,username,mailid,mobilenumber,keyskill,status,emptype from tbl_employee where emptype='PM'"
    flagid=0
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        flagid=flagid+1
        userid=row[0]
        username=row[1]
        mailid=row[2]
        mobilenumber=row[3]
        keyskill=row[4]
        status=row[5]
        emptype=row[6]
        print "<tr><td>%d</td><td>%d</td>"%(flagid,userid)
        print "<td>%s</td><td>%s</td><td>%s</td>"%(username,mailid,mobilenumber)
        print "<td>%s</td>"%(keyskill)
        print "<td>%s</td>"%(emptype)
        if status=="Allow":
            print "<td><div class='btn-group'>"
            #print "<a class='btn btn-success' href='allowpm.py?q=%s&r%s'><i class='icon_check_alt2'></i></a>"%(mailid,"Allow")
            print "Allowed<i class='icon_check_alt2'></i>"
            print "</div></td>"
        elif status=="nothing":
            print "<td><div class='btn-group'>"
            print "<a class='btn btn-success' href='allowpm.py?q=%s&r=%s'><i class='icon_check_alt2'></i></a>"%(mailid,"Allow")
            print "<a class='btn btn-danger' href='denypm.py?q=%s&r=%s'><i class='icon_close_alt2'></i></a>"%(mailid,"Deny")
            print "</div></td>"
        else:
            print "<td><div class='btn-group'>"
            print "Denied<i class='icon_close_alt2'></i>"
            print "</div></td>"
        print "</tr>"
print "</tbody></table></section></div></div>"
print "</section></section>"
print "<div class='text-right'>"
print "<div class='credits'></div></div></section>"
print "</body>"
print "</html>"
