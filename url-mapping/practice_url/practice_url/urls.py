"""practice_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include: 계층적인 url을 효율적으로 관리하기 위한 방법
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls'))
]



    # product/ 로 들어오는 코드는 product.urls 이 담당해줄 것이다. = product/ 하에 생기는 모든 url은 product라는 어플리케이션 안에있는 urls.py 파일에서 관리할 것이다
