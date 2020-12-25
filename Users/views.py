from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import User_role
# Create your views here.
from .serializers import *
from enum import Enum


class Role(Enum):
    staff = 1
    customer = 2


@api_view(['GET', 'POST'])
def user_signup(request):

    response = {
        'success': False,
        'message': 'Sorry Something went wrong',
        'data': []
    }
    if request.method == 'GET':

        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        response["message"] = "Successully fetched"
        response['success'] = True
        response["data"] = serializer.data
        return Response(response, status=200)

    if request.method == 'POST':
        role = request.data.get('role')
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            User_role.objects.create(user_id=user, user_role=role)
            for r in Role:
                if r == int(role):
                    response['role'] = r.name
            response["message"] = "Successully Added"
            response['success'] = True
            response["data"] = serializer.data
            return Response(response, status=200)
        else:
            response['data'] = serializer.errors
            return Response(response, status=400)
