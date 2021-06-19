from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .scraping import *

def index(request):
    return render(request, "search/index.html")

def content(request):
    return render(request, "search/content.html")

def search(request):
    if request.method == "POST":
        to_search = request.POST.get("search")
        list_result = super_search(to_search)
        paginator = Paginator(list_result, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # sorted_ascending= sort_by_price_ascending(list_result[1:])
        # sorted_descending= sort_by_price_descending(list_result[1:])
        context = { "page_obj": page_obj}
        
        return render(request, "search/results.html", context)
    
        