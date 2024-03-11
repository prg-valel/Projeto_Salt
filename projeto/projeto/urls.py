from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('plataform/', views.plataform_page),
    path('cad_admin/', views.cad_admin_page),
    path('login_user/', views.login_user_page),
    path('cadastro/', views.cadastro_page),
    path('vision_user', views.vision_user_page),
    path('vision_admin', views.vision_admin_page), 
]
