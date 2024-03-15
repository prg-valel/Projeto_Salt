from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("plataform/", views.plataform_page),
    path("table/", views.table_page),
    path("cad_admin/", views.cad_admin_page),
    path("login_user/", views.login_user_page),
    path("login_admin/", views.login_admin_page),
    path("cadastro/", views.cadastro_page),
    path("vision_user/", views.vision_user_page),
    path("vision_admin/", views.vision_admin_page),
    path("logout/", views.logout_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
