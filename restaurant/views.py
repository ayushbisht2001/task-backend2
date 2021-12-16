from django.shortcuts import render

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from.models import *
from rest_framework.decorators import api_view


class RestaurantView(APIView):
    def post(self, request, *args, **kwargs):       
            serializer = RestaurantSerializers(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"data":request.data, "status":status.HTTP_201_CREATED, "msg" : "Restaurant Added" })
            else:
                return Response({"data": serializer.errors, "status" : status.HTTP_400_BAD_REQUEST })

    def get(self, request, *args, **kwargs):
        obj = Restaurant.objects.all()
        if obj.exists():
            serializer = RestaurantSerializers(obj, many=True)
            data =   {'data': serializer.data, 'status': status.HTTP_200_OK }
            return Response(data)
        else:
            return Response({'data': "No restaurants ", 'status': status.HTTP_404_NOT_FOUND})

@api_view(['GET'])
def search_restaurant(request, **kwargs):
    query = kwargs.get("query").lower()
    qs = Restaurant.objects.search(query=query)
    serializer = RestaurantSerializers(qs, many=True)
    if qs.exists():        
        return Response({"data": serializer.data, "status": status.HTTP_200_OK })
    else:
        return Response({'data': "No restaurants ", 'status': status.HTTP_404_NOT_FOUND})


@api_view(['GET'])
def sort_restaurant(request, **kwargs):
    query = kwargs.get("query").lower()
    if query == "votes":
        qs = Restaurant.objects.order_by("votes")
    elif query == "rating":
        qs = Restaurant.objects.order_by("agg_rating")
    elif query == "avg_cost_for_2":
         qs = Restaurant.objects.order_by("avg_cost_for_2")
    else:
        qs = Restaurant.objects.order_by("updated_on")
    serializer = RestaurantSerializers(qs, many=True)
    if qs.exists():        
        return Response({"data": serializer.data, "status": status.HTTP_200_OK })
    else:
        return Response({'data': "No restaurants ", 'status': status.HTTP_404_NOT_FOUND})
        