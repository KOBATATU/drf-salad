from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import get_user_model,login
from .serializers import ItemModelSerializer, ProductModelSerializer, UserModelSerializer, LoginSerializer
from .permissions import CustomPermission
from api_class.models import Item,Product


class BaseListView(APIView):

    def get(self, request: Request):
        objects = self.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        # serializer = ItemSerializer(data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # if not serializer.is_valid():
        #     return Response({"errors": serializer.errors}, status=http.HTTPStatus.BAD_REQUEST)
        serializer.save() #保存(create)

        return Response(request.data, status=status.HTTP_201_CREATED)


class ItemModelView(BaseListView):

    serializer_class = ItemModelSerializer
    model = Item
    # 指定したユーザしかアクセスできないようにする
    # permission_classes = [permissions.IsAuthenticated,]

class ProductModelView(BaseListView):
    serializer_class = ProductModelSerializer
    model = Product

class UserModelView(BaseListView):
    serializer_class = UserModelSerializer
    model = get_user_model()

class BaseDetailView(APIView):

    def get(self, request, pk):
        object = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.model.objects.get(pk = pk)
        serializer = self.serializer_class(object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)

    def delete(self, request, pk):
        object = self.model.objects.get(pk = pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        object = self.model.objects.get(pk = pk)
        serializer = self.serializer_class(object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)

class ItemModelDetailView(BaseDetailView):
    serializer_class = ItemModelSerializer
    permission_classes = [CustomPermission,]
    model = Item

class ProductModelDetailView(BaseDetailView):
    serializer_class = ProductModelSerializer
    permission_classes = [CustomPermission,]
    model = Product

class UserModelDetailView(BaseDetailView):
    serializer_class = UserModelSerializer
    permission_classes = [CustomPermission,]
    model = get_user_model()

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

