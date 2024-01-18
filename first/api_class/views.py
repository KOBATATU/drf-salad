import http

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import ItemSerializer
from .models import Item
class ItemView(APIView):

    serializer_class = ItemSerializer

    def get(self, request: Request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        # serializer = ItemSerializer(data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # if not serializer.is_valid():
        #     return Response({"errors": serializer.errors}, status=http.HTTPStatus.BAD_REQUEST)
        serializer.save() #保存(create)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ItemDetailView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, pk):
        item = Item.objects.get(pk = pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = Item.objects.get(pk = pk)
        serializer = self.serializer_class(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)

    def delete(self, request, pk):
        item = Item.objects.get(pk = pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        item = Item.objects.get(pk = pk)
        serializer = self.serializer_class(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)