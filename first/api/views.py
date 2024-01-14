import http

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from datetime import datetime

def index(request):
    return HttpResponse('<h1>Hello</h1>')

# 時間を返す
@api_view(http_method_names=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def country_datetime(request: Request):

    if request.method == 'POST':
        try:
            return Response(request.data)
        except Exception as  e:
            return Response({'error': 'error'}, status=http.HTTPStatus.BAD_REQUEST)

    return Response({
        "Datetime": datetime.now(),
        "queryparams": request.query_params
    })