from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.detail, name="detail_name"),
    path('owners', views.owner_list, name="owners"),
    path('new', views.new, name="new"),
    path('about',views.about, name='about'),
    #path('owner/<int:id>', views.owner_cars, name='o_cars'),

]