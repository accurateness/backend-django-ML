from django.test import TestCase
import requests
from .views import api_mpg
class test_model_api(TestCase):

    def test_api(self):


        car_example = {"cylinders": 8.0,
                         "displacement":    390.0,
                         "horsepower":      190.0,
                         "weight":         3850.0,
                         "acceleration":     8.5,
                         "modelYear":        70.0,
                         "region": "usa"}

         

       # response = requests.post(
        #            "http://localhost:8000/app/ml/mpg", car_examples)

        response = self.client.post("http://localhost:8000/app/ml/mpg", car_example, follow=True) 
        print("This is response!")
        print(response)   

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 
                             124.69535827636719)
