from django.test import TestCase
import requests
from .views import api_mpg
import json

## Running the test in Django with python manage.py test

## Here we perform an integration test which test if the prediction by the ML Flask is correct or not!
class test_model_api(TestCase):

    def test_api(self):


        # Defining a car example which we already know its corresponding prediction by the model

        car_example = {"cylinders": 8.0,
                         "displacement":    390.0,
                         "horsepower":      190.0,
                         "weight":         3850.0,
                         "acceleration":     8.5,
                         "modelYear":        70.0,
                         "region": "usa"}

   
        # Here we send a request to the Django API from the MÖ_API app
        response = self.client.post("http://localhost:8000/app/ml/mpg", car_example, follow=True) 
        print("This is response!")
        print(response)   

        # converting the bytes to json and then return the prediction value
        prediction = json.loads(json.loads(response.content.decode("utf-8"))['result'])['predictions'].pop()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(prediction, 
                             124.69535064697266)
