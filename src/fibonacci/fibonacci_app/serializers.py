from rest_framework import serializers
from fibonacci_app import models
class FibonacciSerializer(serializers.ModelSerializer):
    """
    Serializes a number input to find fibonacci number
    """

    class Meta:
        model = models.HistoryData
        fields = ('input_number', 'fibonacci_result')