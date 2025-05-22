from django.urls import path
from . import views

urlpatterns = [
    path('api/geojson/', views.geojson_locations),
    path('api/stats/', views.location_stats),
    path ('map/', views.map_page),
]
