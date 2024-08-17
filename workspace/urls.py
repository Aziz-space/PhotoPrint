from django.urls import path
from . import views

urlpatterns = [   
    path('add_service/', views.add_service, name='add_service'),
    path('update_service/<int:pk>/', views.update_service, name='update_service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('ChangeProfileForm/', views. ChangeProfileForm, name='update_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('workspace/', views.workspace_view, name='workspace'),
    path('upload/', views.upload_image, name='upload_image'),
    path('create-oi/', views.create_oi, name='create_oi'),
    path('upload/', views.upload_view, name='upload'),
    path('', views.index, name='index'),   
]
