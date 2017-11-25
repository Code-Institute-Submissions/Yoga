from django.conf.urls import include, url
from django.contrib import admin
from Yoga_app import views as Yoga_app_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^timetable$', Yoga_app_views.timetable_page),
    url(r'^blog/', Yoga_app_views.post_list),
    url(r'^poseblog/(?P<id>\d+)/$', Yoga_app_views.post_detail),
    url(r'^poseblog/new/$', Yoga_app_views.new_post, name='new_post'),
    url(r'^poseblog/(?P<id>\d+)/edit$', Yoga_app_views.edit_post, name='edit'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
]