from django.shortcuts import render
from django.core.paginator import Paginator
from .scraping import *
import time

def index(request):
    # Renderiza la vista de index.html
    return render(request, "search/index.html")

def content(request):
    # Renderiza la vista de content.html
    return render(request, "search/content.html")

def search(request):
    # Renderiza la vista de results.html pasandole como contexto la variable list_result a partir del segundo elemento
    # ya que el primero sólo contiene la fecha actual
    
    inicio = time.time()
    
    if request.method == "POST":
        to_search = request.POST.get("search")
        list_result = super_search(to_search)
        
        #? Hemos intentado paginar los resultados pero nos faltan conocimientos html para poder hacerlo
        # paginator = Paginator(list_result, 20)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        
        #? Pensabamos pasarle en el contexto la misma lista resultado ordenada pero luego no sabíamos como enlazarla con los botones de ordenar
        # sorted_ascending= sort_by_price_ascending(list_result[1:])
        # sorted_descending= sort_by_price_descending(list_result[1:])
        
        
        context = { "page_obj": list_result[1:]}
        
        fin = time.time()
        print(fin-inicio)
        
        return render(request, "search/results.html", context)
    
