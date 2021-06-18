from django.http.response import HttpResponse
from django.shortcuts import render
from .scraping import *

def index(request):
    return render(request, "search/index.html")

def content(request):
    return render(request, "search/content.html")

def search(request):
    if request.method == "POST":
        to_search = request.POST.get("search")
        print("##########################################")
        print(to_search)
        list_result = super_search_to_json(to_search)
        context = { "resultados": list_result[1:]}
        return render(request, "search/results.html", context)