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
        list_result = super_search(to_search)
        sorted_ascending= sort_by_price_ascending(list_result[1:])
        sorted_descending= sort_by_price_descending(list_result[1:])
        context = { "resultados": list_result[1:], "ascending": sorted_ascending, "descending": sorted_descending}
        
        return render(request, "search/results.html", context)
    
        