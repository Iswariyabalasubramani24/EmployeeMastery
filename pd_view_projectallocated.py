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
if(sessionid==""):
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
    print "<a class='' href='PDpage.py '>"
    print "<i class='icon_house_alt'></i>"
    print "<span>Dashboard</span></a></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>Project Allocated</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='pd_view_projectallocated.py'>View Project </a></li>"                          
    print "</ul></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>Task</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='PDpage.py' active>Get Today Task</a></li>"                          
    print "</ul></li>"
    print "<li class='sub-menu'>"
    print "<a href='javascript:;' class=''>"
    print "<i class='icon_document_alt'></i>"
    print "<span>View</span>"
    print "<span class='menu-arrow arrow_carrot-right'></span></a>"
    print "<ul class='sub'>"
    print "<li><a class='' href='pd_view_developers.py'>View Token </a></li>"                          
    print "</ul></li></ul>"
    print "</div>"
    print "</aside>"
    print "<section id='main-content'>"
    print "<section class='wrapper'>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<h3 class='page-header'><i class='fa fa-table'></i> PROJECT DEVELOPER</h3>"
    print "<ol class='breadcrumb'>"
    print "<li><i class='fa fa-home'></i><a href='PDpage.py'>Home</a></li>"
    print "<li><i class='fa fa-table'></i>Project </li>"
    print "<li><i class='fa fa-th-list'></i>Allocated Project</li></ol></div></div>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<table class='table table-striped table-advance table-hover'>"
    print "<tbody>"
    print "<tr><th><i class='icon_profile'></i>#</th><th>Project Manager</th><th>Project Leader</th><th>Project Name</th>"
    print "<th>Code</th><th>teamsize</th><th>Duration</th></tr>"
    cursor=db.cursor()
    flagid=0
    selectQuery="select projectmanager,projectleader,projectname,code,teamsize,duration from tbl_employee_allocation where developername='%s'"%(sessionid)
    
    if(cursor.execute(selectQuery)>0):
        rs=cursor.fetchall()
        for row in rs:
            flagid=flagid+1
            pm=row[0]
            pl=row[1]
            projectname=row[2]
            code=row[3]
            teamsize=row[4]
            duration=row[5]
            print "<tr><td>%d</td><td>%d</td><td>%d</td><td>%s</td><td>%s</td><td>%d</td><td>%s</td></tr>"%(int(flagid),int(pm),int(pl),projectname,code,int(teamsize),duration)
    else:
        print "<script>alert('No project allocated to you');location.href='PDpage.py';</script>"
    print "</table>"
    

    
   
    print "</form></div></div></section></div></div></section></section>"
    print "<div class='text-right'>"
    print "<div class='credits'>"
    print "</div></div></section>"
    print "</body>"
    print "</html>"
