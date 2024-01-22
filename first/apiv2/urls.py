from django.urls import path, include
from . import views
app_name = 'api_model_class'
urlpatterns = [
    path('', views.ItemModelView.as_view(), name='item_model'),
    path('<int:pk>/', views.ItemModelDetailView.as_view(), name='item_model_detail'),

    path('user', views.UserModelView.as_view(), name='user_model'),
    path('user/<int:pk>/', views.UserModelDetailView.as_view(), name='user_model_detail'),

    path('product', views.ProductModelView.as_view(), name='product_model'),
    path('product/<int:pk>/', views.ProductModelDetailView.as_view(), name='product_model_detail'),

    path('login/', views.LoginView.as_view(), name='login')
]