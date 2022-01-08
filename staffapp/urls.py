from . import views
from django.urls import path
urlpatterns = [
path('',views.aboutus,name='aboutus'),
path('home',views.index,name='index'),

]