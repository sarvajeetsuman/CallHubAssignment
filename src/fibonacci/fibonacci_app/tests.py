# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.core.urlresolvers import reverse
# from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from fibonacci_app import views
from fibonacci_app import models

class HistoryDataTest(APIRequestFactory):
    """
    To test FibonacciViewSet
    """
    def setUp(self):
        self.fibonacci_number = models.HistoryData.objects.create(input_number=6, fibonacci_result=8)
        # URL for testing apis

    def test_list_fibonacci_number(self):
        request = APIRequestFactory().get("")
        view = views.FibonacciViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        self.assertEqual(len(response), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_fibonacci_number(self):    
        data = {
            "input_number" : 10,
            "fibonacci_result" : ""
        }
        response = self.client.post(self.create_url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response), 1)
        self.assertEqual(response.fibonacci_result, '55')
    

