#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
import datetime
today=datetime.datetime.now()
dt=today.strftime("%d")
mn=today.strftime("%m")
yr=today.strftime("%Y")
fulldate="%s-%s-%s"%(dt,mn,yr)
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
    print "<body onLoad='disablepending();'>"
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
    print "<li><i class='fa fa-table'></i>Task</li>"
    print "<li><i class='fa fa-th-list'></i>Task Today</li></ol></div></div>"
    print "<div class='row'>"
    print "<div class='col-lg-12'>"
    print "<section class='panel'>"
    print "<header class='panel-heading'>"
    print "Todo Today "
    print "</header>"
    print "<div class='panel-body'>"
    print "<div class='form'>"
    print "<form class='form-validate form-horizontal' id='PDpage' name='PDpage' method='post' action='task_completed_pending.py'>"
    print "<div class='form-group '>"
    print "<label for='cname' class='control-label col-lg-2'>User Name:</label>"
    print "<div class='col-lg-10'>"
    print "<input class='form-control' id='username' name='username' type='text' required readonly value='%s'/>"%(sessionid)
    print "</div></div>"
    cursor=db.cursor()
    selectQuery="select projectname,tokenno,task,completedtask,result from tbl_task where empname='%s' and taskdate='%s' and status=%d"%(sessionid,fulldate,0)
    if(cursor.execute(selectQuery)>0):
        result=cursor.fetchone()
        projectname=result[0]
        tokenno=result[1]
        task=result[2]
        completedtask=result[3]
        result=result[4]
        
        print "<div class='form-group '>"
        print "<label for='cemail' class='control-label col-lg-2'>Project Name:</label>"
        print "<div class='col-lg-10'>"
        print "<input class='form-control ' id='projectname' type='text' name='projectname' value='%s' required readonly/>"%(projectname)
        print "</div></div>"
        print "<div class='form-group '>"
        print "<label for='cemail' class='control-label col-lg-2'>Token Number is:</label>"
        print "<div class='col-lg-10'>"
        print "<input class='form-control ' id='tokennumber' value='%s' type='text' name='tokennumber' required readonly/>"%(tokenno)
        print "</div></div>"
        print "<div class='form-group'>"
        print "<div class='col-lg-10' style='float:left;width:50%'>"
        print "<textarea class='form-control' rows=5 cols=20 id='getpendingcode' name='getpendingcode' readonly>"
        print task
        print "</textarea></div>"
        print "<div class='col-lg-10' style='float:right;width:50%'>"
        print "<textarea  class='form-control' rows=5 cols=20 id='continuependingcode' name='continuependingcode'>"
        print completedtask
        print "</textarea>"
        print "</div></div>"
        print "<div class='form-group'>"
        print "<div class='col-lg-offset-2 col-lg-10'>"
        print "<center><button class='btn btn-primary' style='width:23%' type='submit' name='completedbutton' value='Task Completed'>Task Completed</button>"
        print "<button class='btn btn-primary' style='width:23%' type='submit' name='completedbutton' value='Task Pending'>Task Pending</button></center>"
        print "</div></div>"
    else:
        print "<div class='form-group '>"
        
        print "<div class='col-lg-10'>"
        print "No Task is Allocated"
        print "</div></div>"
        
    print "</form></div></div></section></div></div></section></section>"
    print "<div class='text-right'>"
    print "<div class='credits'>"
    print "</div></div></section>"
    print "</body>"
    print "</html>"
