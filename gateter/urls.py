from django.contrib import admin
from django.urls import path, include
from maullidos import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # User registration and authentication paths
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="home"), name='logout'),

    # Maullido related paths
    path('post_maullido/', views.post_maullido, name='post_maullido'),
    path('user/<str:username>/', views.user_page, name='user_page'),

]
