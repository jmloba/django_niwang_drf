from django.contrib import admin
from django.urls import path

from django.contrib import admin

from django.urls import include,  path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name ='home' ),  
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('app_booking/', include('app_booking.urls')),
    path('app_product/', include('app_product.urls')),
    path('app_articles/', include('app_articles.urls')),
]


if settings.DEBUG:
    # urlpatterns+=  debug_toolbar_urls()
    urlpatterns+= staticfiles_urlpatterns()
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    