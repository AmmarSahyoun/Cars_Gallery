from django.contrib import admin
from django.urls import path
from website.views import welcome, date, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('date', date),
    path('about',about),
]
