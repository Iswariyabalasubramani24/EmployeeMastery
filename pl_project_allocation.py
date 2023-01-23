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
    print "<li><i class='fa fa-th-list'></i>PD Allocation</li></ol></div></div>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody>"
    print "<tr><th><i class='icon_profile'></i>#</th><th>TL Allocation Id</th><th>Project Manager</th>"
    print "<th>Team Leader Id</th>"
    print "<th>Project Name</th>"
    print "<th>Coding Language</th>"
    print "<th>Team Size</th>"
    print "<th>Duration</th></tr>"
    if db:
        cursor=db.cursor()
        sql="select tlallocationid,projectmanager,projectleader,projectname,code,teamsize,duration from tbl_teamleader_allocation"
        flagid=0
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            flagid=flagid+1
            tlallocationid=row[0]
            projectmanager=row[1]
            projectleader=row[2]
            projectname=row[3]
            code=row[4]
            teamsize=row[5]
            duration=row[6]
            print "<tr><td>%d</td><td><input type='checkbox' name='tlid' value=%d>%d</td><td>%d</td>"%(flagid,tlallocationid,tlallocationid,projectmanager)
            print "<td>%s</td><td>%s</td><td>%s</td>"%(projectleader,projectname,code)
            print "<td>%s</td>"%(teamsize)
            print "<td>%s</td>"%(duration)
            print "</tr>"
    print "</tbody></table></section></div></div>"


    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody>"
    print "<tr><th><i class='icon_profile'></i>#</th><th>Employee Id</th>"
    print "<th>Employee Name</th>"
    print "<th>Key Skill</th></tr>"
    if db:
        cursor=db.cursor()
        sql="select userid,username,keyskill from tbl_employee where emptype='PD'"
        flagid=0
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            flagid=flagid+1
            userid=row[0]
            username=row[1]
            keyskill=row[2]
            print "<tr><td>%d</td><td><input type='checkbox' name='empid' value=%d>%d</td>"%(flagid,userid,userid)
            print "<td>%s</td><td>%s</td>"%(username,keyskill)
            print "</tr>"
    print "<tr><td colspan='4'><center><input type='submit' value='AllocateEmployee'></center></td></tr>"

            
    print "</tbody></table></section></div></div>"
    print "</section></section>"
    print "<div class='text-right'>"
    print "<div class='credits'></div></div></section>"
    print "</form>"
    print "</body>"
    print "</html>"
