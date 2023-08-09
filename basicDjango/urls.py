from django.urls import path
from . import views

urlpatterns = [
    path('',views.basic_home,name='basic_home'),
    path('greet/<str:username>/', views.greet_user, name='greet_user'),
    path('farewell/<str:username>/', views.farewell_user, name='farewell_user')
]