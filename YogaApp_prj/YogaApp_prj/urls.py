from django.conf.urls import url
from django.contrib import admin
from Yoga_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.say_yoga),
    url(r'^now$', views.get_now),
    url(r'^inherits$', views.inheritance_test),
    url(r'^timetable$', views.timetable_page),
    url(r'^tips$', views.tips_page)
]
