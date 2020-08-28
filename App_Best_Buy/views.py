from django.contrib.auth.models import User
from django.shortcuts import render
import random
import re
import string
# import requests
from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMessage
from rest_framework.utils import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status, viewsets, mixins, generics, response

# Generate Jwt-Token
from rest_framework_jwt.settings import api_settings

from App_Best_Buy.custom_pagination import Pagination, Filter_Pagination
from App_Best_Buy.serializers import Best_Buy_Serializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from .models import Best_Buy,Category

# Create your views here.
class Best_Buy_view(viewsets.ViewSet):#User class
    @action(detail=False,methods=['get','post'])
    def All_Best_Buy(self, request):
        if request.method =="GET":

            p1 = Pagination(request,Best_Buy , 'modified_date', 10, Best_Buy_Serializer)
            res = p1.split_instances_into_pagination()
            return Response(res,status=status.HTTP_200_OK)

        elif request.method=="POST":
            category_data=request.data
            category=category_data['category']
            try:
                class_object = Category.objects.get(category_name=category)
                # print(class_object.id)
            except:
                return Response({"msg":"Not Exist"},status=status.HTTP_404_NOT_FOUND)
            filter_data=Best_Buy.objects.filter(category=class_object.id)
            print("HERE")
            p1 = Filter_Pagination(request, filter_data, 'modified_date', 10, Best_Buy_Serializer)
            res = p1.split_instances_into_pagination()
            return Response(res, status=status.HTTP_200_OK)
        # {
        #     "category": "pcmcat209400050001"
        #
        # }

# http://127.0.0.1:8000/bb/bestbuy/All_Best_Buy/