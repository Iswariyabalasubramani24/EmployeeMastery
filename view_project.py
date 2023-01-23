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
print "<a class='' href='index.py '>"
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



print "</ul>"
print "</div>"
print "</aside>"
print "<section id='main-content'>"
print "<section class='wrapper'>"
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<h3 class='page-header'><i class='fa fa-table'></i> View Peojects</h3>"
print "<ol class='breadcrumb'>"
print "<li><i class='fa fa-home'></i><a href='mainpage.py'>Home</a></li>"
print "<li><i class='fa fa-table'></i>Project</li>"
print "<li><i class='fa fa-th-list'></i>View Project</li></ol></div></div>"
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<section class='panel'>"
print "<table class='table table-striped table-advance table-hover'>"
print "<tbody>"
print "<tr><th><i class='icon_profile'></i>#</th><th><i class='icon_profile'></i> Id</th>"
print "<th><i class='icon_calendar'></i> Name</th>"
print "<th><i class='icon_mail_alt'></i>Coding Lang</th>"
print "<th><i class='icon_pin_alt'></i> DB Name</th>"
print "<th><i class='icon_mobile'></i> Duration</th>"
print "<th><i class='icon_mobile'></i> Register Date</th>"
print "<th><i class='icon_cogs'></i> Action</th></tr>"
if db:
    cursor=db.cursor()
    sql="select * from tbl_projectregister"
    flagid=0
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        flagid=flagid+1
        projectid=row[0]
        projectname=row[1]
        codinglanguage=row[2]
        databasename=row[3]
        duration=row[4]
        registerdate=row[5]
        print "<tr><td>%d</td><td>%d</td>"%(flagid,projectid)
        print "<td>%s</td><td>%s</td><td>%s</td>"%(projectname,codinglanguage,databasename)
        print "<td>%s</td>"%(duration)
        print "<td>%s</td>"%(registerdate)
        print "<td><div class='btn-group'>"
        print "<a class='btn btn-danger' href='delete_project.py?q=%d'><i class='icon_close_alt2'></i></a>"%(int(projectid))
        print "</div></td></tr>"
print "</tbody></table></section></div></div>"
print "</section></section>"
print "<div class='text-right'>"
print "<div class='credits'></div></div></section>"
print "</body>"
print "</html>"
