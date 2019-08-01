# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.views.decorators.csrf import csrf_exempt
# our piece of code….
from django.http import JsonResponse
from django.shortcuts import render
from construction_app.models import site

def test_view(requests):
    response = {"message": "API Working Successfully"}
    return JsonResponse(response)

@csrf_exempt
def sample_db_test(requests):
    if(requests.method == "GET"):
        response_obj = site.objects.all()
        response ={"data":[]}
        for element in response_obj:
            response["data"].append(
                {"site_name":element.site_name, "site_location":element.site_location, "site_area":element.site_area, "site_cost":element.site_cost}
            )
        #print (a)
        #response = {"message": "GET Method Working Successfully"}
    elif(requests.method == "POST"):
        requests_body = json.loads(requests.body)
        site.objects.create(**requests_body)
        response = {"message": "POST Method Working Successfully"}
    elif (requests.method == "PUT"):
        response = {"message": "PUT Method Working Successfully"}
    else:
        response = {"message": "Delete Method Working Successfully"}
    return JsonResponse(response)
