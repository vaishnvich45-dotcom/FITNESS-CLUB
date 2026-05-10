from django.contrib import admin
from django.urls import path
from gymapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),   # 👈 THIS LINE MUST BE THERE
]
