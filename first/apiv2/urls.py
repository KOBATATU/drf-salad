from django.urls import path, include
from . import views
app_name = 'api_model_class'
urlpatterns = [
    path('', views.ItemModelView.as_view(), name='item_model'),
    path('<int:pk>/', views.ItemModelDetailView.as_view(), name='item_model_detail'),
]