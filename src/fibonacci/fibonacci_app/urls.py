from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from fibonacci_app import views

app_name = 'fibonacci_app'

router = DefaultRouter()
router.register('fibonacci-viewset', views.FibonacciViewSet, base_name='fibonacci-viewset')

urlpatterns = [
    url(r'', include(router.urls))
]