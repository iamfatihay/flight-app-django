from django.shortcuts import render
from .models import *
from .serializers import FlightSerializer,ReservationSerializer,PassengerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .permissions import IsAdminOrReadOnly
from datetime import datetime

# Create your views here.
class FlightView(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    # permission_classes= [IsAdminUser]  
    permission_classes= [IsAdminOrReadOnly]  


class ReservationView(viewsets.ModelViewSet):

    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)

class PassengerView(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer