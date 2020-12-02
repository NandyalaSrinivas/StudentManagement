from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appstudent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('application', views.application, name='application'),
    path('candidatelist', views.candidatelist, name='candidatelist'),
    path('status', views.status, name='status'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
