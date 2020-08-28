# import Views as Views
from django.conf.urls import url, include
from django.urls import path,include
from rest_framework import routers

from . import views
from .views import *

# urlpatterns = [

# ]

router=routers.DefaultRouter()
router.register(r'bestbuy(?:/(?P<id>[0-9]+))?', Best_Buy_view, 'bestbuy')#User apis


urlpatterns=[
    path('', include(router.urls)),
]