from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowAllProducts, name='showProducts'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('product/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('product/<int:pk>/delete-comment', views.delete_comment, name='delete-comment'),
]