from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

def football(request):
    return HttpResponse('This is FOOTBALL')

def basketball(request):
    return HttpResponse('This is Basketball')    

def box(request):
    return HttpResponse('This is Box')

def detail(request, sport_id):
    return HttpResponse(f'Sport id = {sport_id}')    