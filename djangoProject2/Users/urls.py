from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.user, name='user-home'),
    path('login/', views.loginpage, name='login-page'),
    path('client_home/', views.client_home, name='client-home-page'),
    path('client_upload/', views.client_upload, name='client-upload-page'),
    path('consultant_home/', views.consultant_home, name='consultant-home-page'),
    path('consultant_upload/', views.consultant_upload, name='consultant-upload-page'),
    path('about/', views.about, name='user-about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

