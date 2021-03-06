from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appstudent import views

app_name = "appstudent"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('application', views.application, name='application'),
    path('registration', views.registration, name = 'registration'),
    path('candidatelist', views.candidatelist, name='candidatelist'),
    path('departments', views.departments, name='departments'),
    path('department/department_wise', views.department_wise, name='department_wise'),
    path('<int:application_id>/student_info', views.student_info, name='student_info'),
    path('status', views.status, name='status'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
