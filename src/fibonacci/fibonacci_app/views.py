# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fibonacci_app import serializers

def index(request):
    """
    Serves the index page
    """
    return render(request, 'fibonacci_app/index.html', context={})


class FibonacciViewSet(viewsets.ViewSet):
    """
    Handles all the operations related to fibonnaci Number
    """

    serializer_class = serializers.FibonacciSerializer

    def list(self, request):
        """
        list query history
        """
        return Response({'message':'No History'})

    def create(self, request):
        """
        Saves the query trail and returns a fibonacci number
        """
        serializer = serializers.FibonacciSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message':'hello', 'number':10}) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)