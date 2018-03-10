from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import market
from .serializers import MarketSerializer

class MarketList(APIView):
    def get(self, request):
        markets = market.objects.all()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data)

    def post(self):
        pass