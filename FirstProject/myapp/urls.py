from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('readdate',views.read_index_data),

    path('home',views.home,name='home'),
]