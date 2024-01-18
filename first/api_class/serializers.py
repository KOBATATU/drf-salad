from rest_framework import serializers
from .models import Item
def check_divide_by_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError("10で割り切れる値にしてください")


class ItemSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(max_value=100, min_value=0)
    discounted_price = serializers.IntegerField(min_value=0, validators=[check_divide_by_ten])

    def validate_price(self, value):
        if self.partial and value is None:
            return value
        print(value)
        if value % 10 !=0:
            raise serializers.ValidationError("1桁は0にしてください")
        return value

    def validate(self, data):
        price = data.get("price", self.instance.price if self.instance is not None else None)
        discounted_price = data.get("discounted_price",self.instance.discounted_price if self.instance is not None else None)
        if price < discounted_price:
            raise serializers.ValidationError("割引価格は本来の価格以下にしてください")
        return data

    def create(self, validated_data):
        print("create: ", validated_data)
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("update: ", validated_data)
        print("update: ", instance.name)
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.discounted_price = validated_data.get("discounted_price", instance.discounted_price)
        instance.save()
        return instance

