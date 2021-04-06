from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import requests
# Create your views here.
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
import os

'''
Here we define the API to receive a post request in the form of a JSON object including the features.

The API asks the ML Flask API regarding the predictions.

'''


@api_view(('POST',))
@permission_classes([AllowAny])
def api_mpg(request, *args, **kwargs):
    
    print("request received!")
    print(request.data)
    data = request.data

    europe = 0.0
    usa = 0.0
    japan = 0.0

    if data['region']=='europe':
        europe = 1.0
    elif data['region']=='usa':
        usa = 1.0
    elif data['region']=='japan':
        japan = 1.0      

        
    car_record = {"received_record":{"Cylinders" : float(data['cylinders']),
    "Displacement" :    float(data['displacement']),
    "Horsepower":      float(data['horsepower']),
    "Weight":         float(data['weight']),
    "Acceleration":     float(data['acceleration']),
    "Model Year":        float(data['modelYear']),
    "Europe":             europe,
    "Japan":             japan,
    "USA": usa }}

    print(car_record)

    result = requests.post("http://"+ os.environ['AUTH_ADDRESS']  + ":8002/api/mpg", json=car_record) # os.environ['AUTH_ADDRESS'] 

    print("This is the result of flask ML api")
    print(result.content)

    return Response({'message':'successfully performed','result':result.content}, status= HTTP_200_OK)


