import http

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import ItemSerializer

class ItemView(APIView):

    def get(self, request: Request):
        return Response({'method': 'GET'})

    def post(self, request: Request):
        print(request.data)
        serializer = ItemSerializer(data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # if not serializer.is_valid():
        #     return Response({"errors": serializer.errors}, status=http.HTTPStatus.BAD_REQUEST)

        return Response({'method': 'POST'})


