from django.contrib import admin
from django.urls import path, include
from website.views import welcome , about #date


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    #path('date', date),
    path('about',about),
    path('cars/', include('cars.urls')),

]
