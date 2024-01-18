from django.urls import path, include
from . import views
app_name = 'api_class'
urlpatterns = [
    path('', views.ItemView.as_view(), name='item'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),

]