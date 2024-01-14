from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(max_value=100, min_value=0)
