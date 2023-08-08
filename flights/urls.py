from django.urls import path, include
from rest_framework import routers
from .views import FlightView,ReservationView,PassengerView

router = routers.DefaultRouter()
router.register("flights", FlightView)
router.register("resv", ReservationView)
# router.register("", FlightView)

urlpatterns = [
    path('', include(router.urls)),
    # path('resv', include(router.urls)),
]
