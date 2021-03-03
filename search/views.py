from django.shortcuts import render
from django.http import HttpResponse
from search.models import Web, Article, Alert
from bs4 import BeautifulSoup
from requests import get

#! creating a instance of  
#! GeeksModel 
#! geek_object = GeeksModel.objects.create(geeks_field ="https://www.geeksforgeeks.org / charfield-django-models/") 
#! geek_object.save() 

def article_exist(description):
    try:
        obj = Article.objects.get(description = description)
    except Exception:
        return False
    else:
        return True


def pccomponentes(request):
    to_search = 'auriculares'
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
                article_exist(description)
                old_price = old_price.text.replace('€','').replace(',','.')
                discount = discount.text.replace('%','')
                Article.create(description,price,old_price,discount,img,href)

    else:

        print("\nNo hay resultados para su búsqueda")

    return HttpResponse(Article.read())