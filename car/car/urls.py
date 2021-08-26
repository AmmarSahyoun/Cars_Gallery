from django.contrib import admin
from django.urls import path, include
from website.views import welcome
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('cars/', include('cars.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





