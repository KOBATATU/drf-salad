from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model, authenticate
from api_class.models import Item, Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model()
        return user.objects.create_user(
            validated_data["username"], email=validated_data["email"],
            password=validated_data["password"]
        )

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
        if value % 10 !=0:
            raise serializers.ValidationError("1桁は0にしてください")
        return value

    def validate(self, data):
        price = data.get("price", self.instance.price if self.instance is not None else None)
        discounted_price = data.get("discounted_price",self.instance.discounted_price if self.instance is not None else None)
        if price < discounted_price:
            raise serializers.ValidationError("割引価格は本来の価格以下にしてください")
        return  data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self,data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            #dbに存在するかチェック
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('ログインができません')
        else:
            raise serializers.ValidationError('ユーザ名とパスワードを入力してください')
        data['user'] = user
        return data