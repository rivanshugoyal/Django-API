from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Create your views here.

def home(request):
	print(User.objects.values())
	data = list(ActivityPeriod.objects.values())
	return JsonResponse({'data': data})