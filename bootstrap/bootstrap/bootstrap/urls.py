from django.contrib import admin
from django.urls import path
from bootapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                          # url의 name space를 지정해준다.
    path('about/', views.about, name='about')                     # /about 이렇게 하면 못알아들음 앞에 자동으로 /가 붙는다고 생각해라
]
