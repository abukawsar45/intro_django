from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(requers):
  return HttpResponse("Hey all base data")