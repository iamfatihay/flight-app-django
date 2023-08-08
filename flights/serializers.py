from rest_framework import serializers
from .models import *

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model=Flight
        fields=("__all__")

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Passenger
        fields=("__all__")

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Kullanıcı adını string olarak göstermek için
    flight = FlightSerializer()  # Flight modeli için bir serializer kullanılıyor
    passenger = PassengerSerializer(many=True)  # Birden çok yolcu için PassengerSerializer kullanılıyor

    class Meta:
        model = Reservation
        fields = "__all__"


