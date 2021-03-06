from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login),
    url(r'^stuMain/$', views.stuMain),
    url(r'^instructorMain/$', views.instructorMain),
    url(r'^managerMain/$', views.managerMain),
    url(r'^setPassword/$', views.setPassword),
    url(r'^changeInfo/$', views.changeInfo),
    url(r'^uploadPic/$', views.uploadPic),
    url(r'^addStudent/$', views.addStudent),
    url(r'^addInstructor/$', views.addInstructor),
    url(r'^stuGradeQuery/$', views.stuGradeQuery),
    url(r'^stuGradeAnalysis/$', views.stuGradeAnalysis),
    url(r'^addCourse/$', views.addCourse),
    url(r'^queryCourse/$', views.queryCourse),
    url(r'^gradeInput/$', views.gradeInput),
    url(r'^gradeInputDetails/$', views.gradeInputDetails),
    url(r'^gradeModify/$', views.gradeModify),
    url(r'^gradeModifyDetails/$', views.gradeInputDetails),
    url(r'^gradeQuery/$', views.gradeQuery),
    url(r'^gradeQueryDetails/$', views.gradeQueryDetails),
    url(r'^changeCourse/$', views.changeCourse),
    url(r'^dropCourse/$', views.dropCourse),
    url(r'^modifyUser/$', views.modifyUser),
    url(r'^addUser/$', views.addUser),
    url(r'^deleteUser/$', views.deleteUser),
]

urlpatterns += static('media/images/', document_root='../jwsys/basicInfo/media/images')