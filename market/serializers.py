from rest_framework import serializers
from .models import market

class MarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = market
        fields = '__all__'