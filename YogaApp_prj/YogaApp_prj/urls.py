from django.conf.urls import include, url
from django.contrib import admin
from Yoga_app import views as Yoga_app_views
from accounts import views as accounts_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Yoga_app_views.say_yoga),
    url(r'^now$', Yoga_app_views.get_now),
    url(r'^timetable$', Yoga_app_views.timetable_page),
    url(r'^contacts/', Yoga_app_views.get_contacts),
    url(r'^poseblog/$', Yoga_app_views.post_list),
    url(r'^poseblog/(?P<id>\d+)/$', Yoga_app_views.post_detail),
    url(r'^poseblog/new/$', Yoga_app_views.new_post, name='new_post'),
    url(r'^poseblog/(?P<id>\d+)/edit$', Yoga_app_views.edit_post, name='edit'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
]
