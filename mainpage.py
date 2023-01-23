#!/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
print "<link rel='shortcut icon' href='img/favicon.png'>"
print "<title>Employee Mastery</title>"
import JcLink
print "</head>"
print "<body>"
# <!-- container section start -->
print "<section id='container' class=''>"
import Header  
# <!--sidebar start-->
print "<aside>"
print "<div id='sidebar'  class='nav-collapse '>"
#<!-- sidebar menu start-->
print "<ul class='sidebar-menu'>"
print "<li class='active'>"
print "<a class='' href='mainpage.py'>"
print "<i class='icon_house_alt'></i>"
print "<span>Dashboard</span>"
print "</a></li>"
print "<li class='sub-menu'>"
print "<a href='javascript:;' class=''>"
print "<i class='icon_document_alt'></i>"
print "<span>Employees</span>"
print "<span class='menu-arrow arrow_carrot-right'></span>"
print "</a>"
print "<ul class='sub'>"
print "<li><a class='' href='add_employee.py'>Add Employees</a></li>"
print "<li><a class='' href='view_employee.py'>View Employees</a></li>"
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
# <!--sidebar end-->

# <!--main content start-->
print "<section id='main-content'>"
print "<section class='wrapper'>"
# <!--overview start-->
print "<div class='row'>"
print "<div class='col-lg-12'>"
print "<h3 class='page-header'><i class='fa fa-laptop'></i> Dashboard</h3>"
print "<ol class='breadcrumb'>"
print "<li><i class='fa fa-home'></i><a href='mainpage.py'>Home</a></li>"
print "<li><i class='fa fa-laptop'></i>Dashboard</li>"		
print "</ol></div></div>"
# <!-- Today status end -->
##print "<div class='row'>"
##print "<div class='col-lg-9 col-md-12'>"
##print "<div class='panel panel-default'>"
##print "<div class='panel-heading'>"
##print "<h2><i class='fa fa-flag-o red'></i><strong>Registered Users</strong></h2>"
##print "<div class='panel-actions'>"
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","root","employeemaster")
cursor=db.cursor()
username=[]
numeracy=[]
comm=[]
inftech=[]
pskill=[]
eskill=[]
marksec=[]
select="select userid from tbl_feedback"
if(cursor.execute(select)>0):
    results=cursor.fetchall()
    for row in results:
        uid=row[0]
        select="select username,numeracy,communication,informationtechnology,personalskill,errorskill,marksecured from tbl_feedback where userid=%d"%(int(uid))
        if(cursor.execute(select)>0):
            results=cursor.fetchone()
            uname=results[0]
            num=results[1]
            com=results[2]
            inf=results[3]
            perskill=results[4]
            errorskill=results[5]
            msec=results[6]
            username.append(uname)
            numeracy.append(int(num))
            comm.append(int(com))
            inftech.append(int(inf))
            pskill.append(int(perskill))
            eskill.append(int(errorskill))
            marksec.append(int(msec))
           
import pygal
from pygal.style import Style
for i in range(len(username)):
    custom_style = Style(colors=('#E80080', '#404040','#9BC850','#7af442','#415cf4'))
    b_chart = pygal.Bar(style=custom_style)
    b_chart.title = "Skill Analysis of %s"%(username[i])
    b_chart.y_labels = 0,10,20,30,40,50,60,70,80,90,100
    b_chart.add("Numeracy",numeracy[i])
    b_chart.add("Communication",comm[i])
    b_chart.add("Information Technology",inftech[i])
    b_chart.add("Personal Skill",pskill[i])
    b_chart.add("Error Skill",eskill[i])
    b_chart.add("Overall",marksec[i])
    chart=username[i]+".svg"
    b_chart.render_to_file(chart)
print "<table width='100%' cellspacing=5 border=1><tr>"
count=0
for name in range(len(username)):
    count=count+1
    uname=username[name]+".svg"
    print"<td>"
    print "<a href='%s'><img src='%s'>"%(uname,uname)
    print "</a>"
    print "</td>"
    if(count==2):
        count=0
        print "</tr>"
        print "<tr>"
print "</tr></table>"
##print "</div>"
##print "</div>"
##print "</div>"
##print "</div>"
##print "</div>"

print """



</section>
</section>
</section>


<script>

//knob
$(function() {
$('.knob').knob({
'draw' : function () { 
$(this.i).val(this.cv + '%')
}
})
});

//carousel
$(document).ready(function() {
$('#owl-slider').owlCarousel({
navigation : true,
slideSpeed : 300,
paginationSpeed : 400,
singleItem : true

});
});

//custom select box

$(function(){
$('select.styled').customSelect();
});

/* ---------- Map ---------- */
$(function(){
$('#map').vectorMap({
map: 'world_mill_en',
series: {
regions: [{
values: gdpData,
scale: ['#000', '#000'],
normalizeFunction: 'polynomial'
}]
},
backgroundColor: '#eef3f7',
onLabelShow: function(e, el, code){
el.html(el.html()+' (GDP - '+gdpData[code]+')');
}
});
});

</script>

</body>
</html>
"""
