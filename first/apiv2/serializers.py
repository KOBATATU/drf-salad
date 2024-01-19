from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from api_class.models import Item

def check_divide_by_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError("10で割り切れる値にしてください")

class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        # read_only_fields = ["price"]
        extra_kwargs = {
            'name': {'write_only': True, 'required': False}
        }
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=['name', 'price'],
                message='nameとpriceの組み合わせに同じ値を入れないでください'
            )
        ]
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
        return  data