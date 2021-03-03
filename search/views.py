from django.shortcuts import render
from django.http import HttpResponse
from search.models import Web, Article, Alert
from bs4 import BeautifulSoup
from requests import get
import datetime

#! creating a instance of  
#! GeeksModel 
#! geek_object = GeeksModel.objects.create(geeks_field ="https://www.geeksforgeeks.org / charfield-django-models/") 
#! geek_object.save() 

def article_exist(desc):
    try:
        obj = Article.objects.get(description=desc)
    except Exception:
        return False
    else:
        return True


def pccomponentes(to_search):
    # to_search = 'auriculares'
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    # to_search = to_search.replace(" ","+")

    pc_componentes = 'https://www.pccomponentes.com'
    pc_componentes_buscar = pc_componentes+'/buscar/?query='+to_search       
    response = get(pc_componentes_buscar, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    results_containers = html_soup.find_all("div", class_ = "col-xs-6 col-sm-4 col-md-4 col-lg-4")

    if results_containers != []:
        
        for product in results_containers:
            article_tag = product.find("article")

            #!DATOS
            description = article_tag['data-name']
            price = float(article_tag['data-price'])
            discount = product.find('span', class_ = "c-badge c-badge--discount cy-product-discount-ammount") #.text
            old_price = product.find('div', class_ = 'c-product-card__prices-pvp cy-product-price-normal')    #.text
            img = product.find('img')['src']
            href = pc_componentes+(product.find('a')['href'])

            if old_price != None:
                if article_exist(description) == False:
                    old_price = old_price.text.replace('€','').replace(',','.')
                    discount = discount.text.replace('%','')
                    Article.create(description,price,old_price,discount,img,href)
                else: 
                    obj = Article.objects.get(description = description)
                    obj.updated_date = datetime.date.today()


# def mediamarkt(to_search):
        
#     headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

#     # to_search = to_search.replace(" ","+")
#     # to_search = 'auriculares'

#     mediamarkt = 'https://www.mediamarkt.es/es/search.html?query='+to_search+'&searchProfile=onlineshop&channel=mmeses'
#     # https://www.mediamarkt.es/es/search.html?query=auriculares&t=1614762089084&user_input=auriculares&query_from_suggest=true
#     response = get(mediamarkt, headers=headers)

#     html_soup = BeautifulSoup(response.text, 'html.parser')
#     results_containers = html_soup.find_all("div", class_ = "ProductFlexBox__StyledListItem-sc-1xuegr7-0 cBIIIT")

#     if results_containers != []:

#         for product in results_containers:

#             #!DATOS
#             description = product.find_all("a")[-1].text[6:]
#             price = product.find("div", class_ = "price small").text        # ERROR: SI UN PRODUCTO ESTÁ AGOTADO NO TIENE PRECIO
#             price = price.replace(",-","")
#             price = float(price.replace(",","."))

#             try:
#                 old_price = product.find("div", class_ = "price price-xs price-old").text[11:]
#                 old_price = old_price.replace(",-","")                                          
#                 old_price = float(old_price.replace(",","."))
#                 discount = int(((old_price-price)*100/old_price)*-1)
#             except AttributeError:
#                 old_price = "None"
#                 discount = "None"

#             img = product.find('img')['data-original']
#             href = product.find('a', itemprop="url")['href']

#             if old_price != None:
#                 if article_exist(description) == False:
#                     Article.create(description,price,old_price,discount,img,href)
#                 else: 
#                     obj = Article.objects.get(description = description)
#                     obj.updated_date = datetime.date.today()
#     else:
#         print('No hay resultados en mediamarkt')


def super_search(request):
    to_search = 'auriculares'
    pccomponentes(to_search)
    # mediamarkt(to_search)
    return HttpResponse(Article.read())