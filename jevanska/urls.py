from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from listings import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)