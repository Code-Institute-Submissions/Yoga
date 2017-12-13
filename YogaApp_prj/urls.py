from django.conf.urls import include, url
from django.contrib import admin
from Yoga_app import views as Yoga_app_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', Yoga_app_views.get_index, name='index'),
    url(r'^home/$', Yoga_app_views.go_home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^timetable/$', Yoga_app_views.timetable_page, name='timetable'),
    url(r'^prices/$', Yoga_app_views.price_list, name='prices'),
    url(r'^blog/$', Yoga_app_views.post_list, name='blog'),
    url(r'^blog/(?P<id>\d+)/$', Yoga_app_views.post_detail),
    url(r'^blog/new/$', Yoga_app_views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', Yoga_app_views.edit_post, name='edit'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)