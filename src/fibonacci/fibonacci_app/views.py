# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fibonacci_app import models
from fibonacci_app import serializers

def fib(n) :
    # Base cases
    f = [0]*1000
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])
 
    # If fib(n) is already computed
    if (f[n]) :
        return f[n]
 
    if( n & 1) :
        k = (n + 1) // 2
    else : 
        k = n // 2
 
    # Applyting above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    else :
        f[n] = (2*fib(k-1) + fib(k))*fib(k)
 
    return f[n]


class FibonacciViewSet(viewsets.ViewSet):
    """
    Handles all the operations related to fibonnaci Number
    """

    serializer_class = serializers.FibonacciSerializer

    def list(self, request):
        """
        list query history
        """
        history_data = models.HistoryData.objects.all().order_by('-created_date')
        serializer = serializers.FibonacciSerializer(history_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Saves the query trail and returns a fibonacci number
        """
        serializer = serializers.FibonacciSerializer(data=request.data)
        print serializer
        status_q = False
        if serializer.is_valid():
            num = serializer.data.get('input_number')
            print serializer.data.get('input_number')
            res = str(fib(num))
            data, status_q = models.HistoryData.objects.get_or_create(
                input_number=num,
                fibonacci_result=res)
            serializer = serializers.FibonacciSerializer(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)