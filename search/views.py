from django.shortcuts import render
from django.http import HttpResponse
from search.models import Web, Persona, Usuario
#from django.shortcuts import render_to_response (BOOSTRAP)

#def index(request):
#   return render_to_response('index.html')
#INDEX PRINCIPAL, PLANTILLA CON BOOSTRAP

def crear_web(request):
    pass

#! creating a instance of  
#! GeeksModel 
#! geek_object = GeeksModel.objects.create(geeks_field ="https://www.geeksforgeeks.org / charfield-django-models/") 
#! geek_object.save() 


# Create your views here.

# from bs4 import BeautifulSoup
# from requests import get

# #FUNCION en views
# def busqueda_producto():
#     headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

#     search = input("¿Qué quieres buscar?:  ")
#     search = search.replace(" ","+")
#     # search = 'auriculares'

#     pc_componentes = 'https://www.pccomponentes.com'
#     pc_componentes_buscar = pc_componentes+'/buscar/?query='+search       # #pg-2&or-search esto controlaria las paginas donde 2 se refiere al num de pag
#     response = get(pc_componentes_buscar, headers=headers)
#     html_soup = BeautifulSoup(response.text, 'html.parser')
#     results_containers = html_soup.find_all("div", class_ = "col-xs-6 col-sm-4 col-md-4 col-lg-4")

# #FUNCION
# def filtro():
#     if results_containers != []:
        
#         for product in results_containers:
#             article_tag = product.find("article")

#             #!DATOS
#             description = article_tag['data-name']
#             price = float(article_tag['data-price'])
#             discount = product.find('span', class_ = "c-badge c-badge--discount cy-product-discount-ammount") #.text
#             old_price = product.find('div', class_ = 'c-product-card__prices-pvp cy-product-price-normal')    #.text
#             img = product.find('img')['src']
#             href = pc_componentes+(product.find('a')['href'])

#             print('None' if discount == None else f'{discount.text}','None' if old_price == None else f'{old_price.text}',f' -- {price}',' '*(15-len(str(price)+str(old_price)+' -- ')), f'{description}')
#             print(f'{href}')

#     else:

#         print("\nNo hay resultados para su búsqueda")


# busqueda_producto()
# filtro()