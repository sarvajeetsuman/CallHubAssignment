from rest_framework import serializers

class FibonacciSerializer(serializers.Serializer):
    """
    Serializes a number input to find fibonacci number
    """

    num = serializers.IntegerField()