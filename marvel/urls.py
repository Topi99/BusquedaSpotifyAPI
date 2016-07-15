from django.conf.urls import url
from django.contrib import admin
from main import views
from spotify import views as sv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Welcome.as_view()),
    url(r'^spotify/$', sv.Main.as_view()),
]
