#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
if db:
    cursor=db.cursor()
    sql="select * from tbl_session"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        sessionid=row[0]
        sessiontype=row[1]
print "<html lang='en'>"
print "<head>"
print "<meta charset='utf-8'>"
print "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
print "<link rel='shortcut icon' href='img/favicon.png'>"
print "<title></title>"
import JcLink
print "</head>"
print "<body>"
print "<!-- container section start -->"
print "<section id='container' class=''>"
import Header
# <!--sidebar start-->
print "<aside>"
print "<div id='sidebar'  class='nav-collapse '>"
# <!-- sidebar menu start-->
print "<ul class='sidebar-menu'>"
print "<li class='active'>"
print "<a class='' href='PMpage.py'>"
print "<i class='icon_house_alt'></i>"
print "<span>Dashboard</span>"
print "</a>"
print "</li>"
print "<li class='sub-menu'>"
print "<a href='javascript:;' class=''>"
print "<i class='icon_document_alt'></i>"
print "<span>Allocation</span>"
print "<span class='menu-arrow arrow_carrot-right'></span>"
print "</a>"
print "<ul class='sub'>"
print "<li><a class='' href='PMpage.py'>PL Allocation</a></li>                          "
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
print "</ul>"
# <!-- sidebar menu end-->
print "</div>"
print "</aside>"
print "<!--sidebar end-->"

# <!--main content start-->
print "<section id='main-content'>"
print "<section class='wrapper'>"
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<h3 class='page-header'><i class='fa fa-files-o'></i> Project Allocation</h3>"
print "<ol class='breadcrumb'>"
print "<li><i class='fa fa-home'></i><a href='mainpage.py'>Home</a></li>"
print "<li><i class='icon_document_alt'></i>Allocation</li>"
print "<li><i class='fa fa-files-o'></i>Project Allocation</li>"
print "</ol></div></div>"
# <!-- Form validations -->              
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<section class='panel'>"
print "<header class='panel-heading'>"
print "Add Projects"
print "</header>"
print "<div class='panel-body'>"
print "<div class='form'>"
print "<form class='form-validate form-horizontal' id='feedback_form' method='post' action='insert_project_allocation.py'>"
print "<div class='form-group '>"
print "<label for='cname' class='control-label col-lg-2'>Project Manager:<span class='required'></span></label>"
print "<div class='col-lg-10'>"
if db:
    cursor=db.cursor()
    sql="select userid from tbl_employee where username='%s' and emptype='%s'"%(sessionid,sessiontype)
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        userid=row[0]
print "<input type=text class='form-control' id='projectmanager' name='projectmanager' value='%s' maxlength='25' required readonly/>"%(userid)
print "</div></div>"
print "<div class='form-group '>"
print "<label for='cname' class='control-label col-lg-2'>Select Project:<span class='required'>*</span></label>"
print "<div class='col-lg-10'>"
print "<select class='form-control' id='projectname' name='projectname' maxlength='25' required />"
print "<option value='0'>----select----</option>"
if db:
    cursor=db.cursor()
    sql="select projectid,projectname from tbl_projectregister"
    flagid=0
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        projectid=row[0]
        projectname=row[1]
        print "<option value='%s-%s'>%s"'-'"%s</option>"%(projectid,projectname,projectid,projectname)
print "</select>"
print "</div></div>"
print "<div class='form-group '>"
print "<label for='cemail' class='control-label col-lg-2'>Select TL:<span class='required'>*</span></label>"
print "<div class='col-lg-10'>"
print "<select class='form-control ' id='plid'  name='plid' required />"
print "<option value='0'>----select----</option>"
if db:
    cursor=db.cursor()
    sql="select userid,username from tbl_employee where emptype='%s'"%("PL")
    flagid=0
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        userid=row[0]
        username=row[1]
        print "<option value='%s-%s'>%s"'-'"%s</option>"%(userid,username,userid,username)


print "</select>"
print "</div></div>"

print "<div class='form-group '>"
print "<label for='cemail' class='control-label col-lg-2'>Duration:<span class='required'>*</span></label>"
print "<div class='col-lg-10'>"
print "<input class='form-control ' id='duration' type='text' name='duration' required />"
print "</div></div>"

print "<div class='form-group '>"
print "<label for='cemail' class='control-label col-lg-2'>Team Size:<span class='required'>*</span></label>"
print "<div class='col-lg-10'>"
print "<input class='form-control ' id='members' type='text' name='members' required />"
print "</div></div>"
print "<div class='form-group '>"
print "<label for='curl' class='control-label col-lg-2'>Code in(Programming Language):<span class='required'>*</span></label>"
print "<div class='col-lg-10'>"
print "<input class='form-control ' id='code' type='text' name='code' />"
print "</div></div>"

print "<div class='form-group'>"
print "<div class='col-lg-offset-2 col-lg-10'>"
print "<button class='btn btn-primary' type='submit'>Save</button>"
print "<button class='btn btn-default' type='button'>Cancel</button>"
print "</div></div></form></div></div></section></div></div></section></section>"
# <!--main content end-->
print "<div class='text-right'>"
print "<div class='credits'>"
print "</div></div></section>"
# <!-- container section end -->

print "</body>"
print "</html>" 
