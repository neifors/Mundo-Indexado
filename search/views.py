from django.http.response import HttpResponse
from django.shortcuts import render
from . import scraping

def search():
    return HttpResponse( scraping.super_search())
