from django.shortcuts import render

# Create your views here.
from .models import *
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import renderer_classes, api_view
from .serializers import *
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def function(request):
    """This is a function based view for coffee_store list
    Returns:
        json: a json of the coffee_store list
    """
    template_name = 'template'
    context = None
    response = {
        'success': False,
        'message': 'something went wrong ',
        'data': []
    }
    if request.method == 'GET':
        # coffee_store_list = list(coffee_store.objects.all())
        menu = Menu.objects.all()
        total_count = len(menu)
        serializers = MenuSerializer(menu, many=True)
        response['success'] = True
        response['message'] = 'successfull'
        response['total_count'] = total_count
        response['data'] = serializers.data
        return Response(response, status=200)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['success'] = True
            response['message'] = 'successfull'
            response['data'] = serializer.data
            return Response(response, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def coffee_list(request):
    """This function is related to coffe_store table data

    Returns:
        [json]: returns the json response of list of coffee_store data
    """
    response = {
        'success': False,
        'message': 'something went wrong ',
        'data': []
    }
    if request.method == 'GET':
        coffee_store_list = coffee_store.objects.prefetch_related('amenities')
        total_count = len(coffee_store_list)
        serializer = CoffeeSerializer(coffee_store_list, many=True)
        response['success'] = True
        response['message'] = 'successfull'
        response['total_count'] = total_count
        response['data'] = serializer.data
        return Response(response, status=200)

    if request.method == 'POST':
        serializer = CoffeeSerializer(data=request.data)
        amenities_list = request.data.pop('amenities')
        if serializer.is_valid():
            coffee_store_obj = serializer.save()
            for amenity_id in amenities_list:
                amenity_obj = Amenity.objects.get(id=amenity_id)
                # coffee_store_obj.amenities.add(
                #     name=amenity_obj.name, decription=amenity_obj.description)
                coffee_store.objects.get(
                    id=coffee_store_obj.id).amenities.add(amenity_obj)
                # c1.amenities.add(amenity_obj)
            coffee_store_obj.save()
            response['success'] = True
            response['message'] = 'successfull'
            response['data'] = serializer.data
            return Response(response, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def amenities(request):
    response = {
        'success': False,
        'message': 'Sorry Something went wrong',
        'data': []
    }
    if request.method == 'GET':
        amenities_list = Amenity.objects.all()
        total_count = len(amenities_list)
        if total_count > 0:
            amenities_serializers = AmenitySerialiers(
                amenities_list, many=True)
            response['success'] = True
            response['message'] = "Succeessfull"
            response['total_count'] = total_count
            response['data'] = amenities_serializers.data
            return Response(response, status=200)
        else:
            return Response(response, status=404)

    if request.method == 'POST':
        serializer = AmenitySerialiers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['success'] = True
            response['message'] = "Succeessfull"
            response['total_count'] = total_count
            response['data'] = serializer.data
            return Response(response, status=200)
        else:
            response['data'] = serializer.errors
            return Response(response, status=400)
