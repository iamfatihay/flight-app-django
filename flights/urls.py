from django.urls import path, include
from rest_framework import routers
from .views import FlightView

router = routers.DefaultRouter()
router.register("", FlightView)

urlpatterns = [
    path('', include(router.urls)),
    # path('flights/', include('flights.urls')),
]
