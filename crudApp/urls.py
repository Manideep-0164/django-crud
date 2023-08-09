from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_home, name='crud_home'),
    path('users/', views.display_items, name='display_items'),
    path('userform/', views.get_userdata, name='get_data'),
    path('edituser/<int:item_id>/', views.edit_user, name='edit_user'),
    path('deleteuser/<int:item_id>/', views.delete_user, name='delete_user')
]