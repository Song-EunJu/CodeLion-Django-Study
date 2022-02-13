from django.urls import path
from product import views

urlpatterns = [
    path('', views.productList),
    path('first/', views.productFirst)
]

# 아무것도 입력하지 않았을 때 실행되는 함수는 곧 127.0.0.1:8000/boards 로 들어왔을 때 실행되는 함수와 같다.
