import psutil

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .models import Room, Reservation

import datetime

from django.shortcuts import render

# Create your views here.

@api_view(["GET"])
def cpu_count(request):

    cpu_count = psutil.cpu_count()

    return Response({"cpu_count": cpu_count})