from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.conf.settings import MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)