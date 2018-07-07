from django.urls import path,include
from mainCensus import views as mc_views
urlpatterns = [
    path('home/',mc_views.home,name='home'),
    path('mainc/',mc_views.maincensus,name='mainc'),
]
