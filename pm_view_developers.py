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
    print "<li><a class='' href='PMpage.py' active>PL Allocation</a></li>"                          
    print "<li><a class='' href='project_allocation.py'>Project Allocation</a></li>"
    print "</ul></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>View</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='pm_view_developers.py'>View Developers</a></li>"                          
    print "<li><a class='' href='pm_view_tl.py'>View Team Leaders</a></li>"
    print "<li><a class='' href='pm_view_project.py'>View Project</a></li>"
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
    print "<h3 class='page-header'><i class='fa fa-table'></i> VIEW DEVELOPERS</h3>"
    print "<ol class='breadcrumb'>"
    print "<li><i class='fa fa-home'></i><a href='mainpage.py'>Home</a></li>"
    print "<li><i class='fa fa-table'></i>VIEW</li>"
    print "<li><i class='fa fa-th-list'></i>VIEW DEVELOPERS</li></ol></div></div>"
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
    print "<th><i class='icon_mobile'></i> EmpType</th></tr>"
    if db:
        cursor=db.cursor()
        sql="select userid,username,mailid,mobilenumber,keyskill,status,emptype from tbl_employee where emptype='%s'"%("PD")
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
            
            print "</tr>"
    print "</tbody></table></section></div></div>"
    print "</section></section>"
    print "<div class='text-right'>"
    print "<div class='credits'></div></div></section>"
    print "</body>"
    print "</html>"
