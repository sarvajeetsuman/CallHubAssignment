# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fibonacci_app import models
from fibonacci_app import serializers

def fib(n) :
    f = [0]*(n+1)
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
        try:
            history_data = models.HistoryData.objects.all().order_by('-created_date')
        except:
            return Response({"errors":"Could not fetch the data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = serializers.FibonacciSerializer(history_data, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"errors":"Could not serialize the data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """
        Saves the query trail and returns a fibonacci number
        """
        serializer = serializers.FibonacciSerializer(data=request.data)
        status_q = False
        res = None
        if serializer.is_valid():
            num = serializer.data.get('input_number')
            if num > 0 and num < 1000:
                res = models.HistoryData.objects.filter(input_number=num)
                if  res:
                    res = res.first().fibonacci_result
                else:
                    res = str(fib(num))
            else:
                return Response({"errors":"Invalid Input"}, status=status.HTTP_400_BAD_REQUEST)
            data, status_q = models.HistoryData.objects.get_or_create(
                input_number=num,
                fibonacci_result=res)
            data.save()
            serializer = serializers.FibonacciSerializer(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response({"errors":"Invalid Input"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors":"Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)