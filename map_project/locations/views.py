from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from collections import Counter

@api_view(['GET'])
def geojson_locations(request):
    data = {
        "type": "FeatureCollection",
        "features": []
    }
    for loc in Location.objects.all():
        data["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [loc.longitude, loc.latitude],
            },
            "properties": {
                "name": loc.name,
                "category": loc.category
            }
        })
    return Response(data)

@api_view(['GET'])
def location_stats(request):
    locations = Location.objects.all()
    categories = [loc.category for loc in locations]
    most_common = Counter(categories).most_common(1)[0] if categories else ("None", 0)

    data = {
        "total_locations": locations.count(),
        "most_common_category": most_common[0]
    }
    return Response(data)
from django.shortcuts import render 
def map_page(request):
    return render(request,'map.html')