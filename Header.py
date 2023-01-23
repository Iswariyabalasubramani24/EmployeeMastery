import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
print "<header class='header dark-bg'>"
print "<div class='toggle-nav'>"
print "<div class='icon-reorder tooltips' data-original-title='Toggle Navigation' data-placement='bottom'><i class='icon_menu'></i></div>"
print "</div>"
# <!--logo start-->
print "<a href='mainpage.html' class='logo'>Employee <span class='lite'>Mastery</span></a>"
# <!--logo end-->

print "<div class='nav search-row' id='top_menu'>"
# <!--  search form start -->

# <!--  search form end -->                
print "</div>"

print "<div class='top-nav notification-row'>"
# <!-- notificatoin dropdown start-->
print "<ul class='nav pull-right top-menu'>"
                    
# <!-- task notificatoin start -->






print "<li class='dropdown'>"
print "<a data-toggle='dropdown' class='dropdown-toggle' href='#'>"
print "<span class='profile-ava'>"
print "<img alt='' src='img/.jpg'>"
print "</span>"
if db:
    cursor=db.cursor()
    sql="select sessionid from tbl_session"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        sessionid=row[0]
print "<span class='username'>%s</span>"%(sessionid)
print "<b class='caret'></b>"
print "</a>"
print "<ul class='dropdown-menu extended logout'>"
print "<div class='log-arrow-up'></div>"
print "<li class='eborder-top'>"
print "<a href='#'><i class='icon_profile'></i> My Profile</a>"
print "</li>"
print "<li>"
print "<a href='logout.py'><i class='icon_key_alt'></i> Log Out</a>"
print "</li>"
print "</ul>"
print "</li>"
# <!-- user login dropdown end -->
print "</ul>"
# <!-- notificatoin dropdown end-->
print "</div>"
print "</header>"

