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
from .views import UserLoginView
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    
    path('auth',obtain_auth_token),

    path('admin/', admin.site.urls),
    path('', views.home , name ='home' ),  
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('app_booking/', include('app_booking.urls')),
    path('app_product/', include('app_product.urls')),
    path('app_articles/', include('app_articles.urls')),
    
    path('app_mail/', include('app_mail.urls')),
    path('app_blog/', include('app_blog.urls')),
    path('app_auth/', include('app_auth.urls')),
    path('app_members/', include('app_members.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
     

    path('login/', views.login , name='login'),       
    path('signup/', views.signup , name='signup'),       
    path('test_token/', views.test_token , name='test_token'),       
    path('loginview/', UserLoginView.as_view() , name='loginview'),       


]


if settings.DEBUG:
    # urlpatterns+=  debug_toolbar_urls()
    urlpatterns+= staticfiles_urlpatterns()
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

  