"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from calculation.views import home,add,sub,mul,div,get_add,get_sub,get_mul,get_div

urlpatterns = [
    path('calhome/',home,name="page"),
    path('addition/',add,name="sum"),
    path('subtraction/',sub,name="diff"),
    path('multiplication/',mul,name="times"),
    path('division/',div,name="divs"),
    path('getadd/',get_add,name="getadd"),
    path('getsub/',get_sub,name="getsub"),
    path('getmul/',get_mul,name="getmul"),
    path('getdiv/',get_div,name="getdiv")

]
