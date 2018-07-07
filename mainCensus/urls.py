from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('General', views.GeneralView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('generalapi', include(router.urls)),
]
