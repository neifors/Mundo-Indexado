from django.http import HttpResponse
from bs4 import BeautifulSoup
from requests import get
import datetime
import pandas as pd
import json


def pccomponentes(to_search):
    
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    pc_componentes = 'https://www.pccomponentes.com'
    page = 1
    data=[]
    while page <= 4:
        uri_to_search = pc_componentes+'/buscar/?query='+to_search+"&page="+str(page)+"&or-relevance"     
        response = get(uri_to_search, headers=headers)
        ##? Si response 200:
        html_soup = BeautifulSoup(response.text, 'html.parser')
        results_container = html_soup.find_all("a", class_="Wrapper-sc-8udqwp cIlLgX sc-amkrK dmBMsh")
                                                        
        if results_container != []:
            for product in results_container:
                current_price = product.find("span", class_ = "sc-jfkLlK bQYAGo" ) #precio actual si tiene descuento
                if current_price != None:
                    price = float(current_price.text.replace("€",""))
                    description = product["data-name"]
                    old_price = float(product["data-price"]) # precio antiguo si tiene aplicado descuento
                    img = product.find('img')['src']
                    href = product["href"]
                    discount = (old_price-price)*100/old_price
                    data.append({'description':description ,'price':price ,'discount':f"{discount:.2f}%" ,'old_price':old_price ,'img_url':img ,'product_href':href})
        page += 1
        
    return data        


def blackmarket(to_search):
    
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    blackmarket = 'https://www.backmarket.es'
    page = 1
    data=[]
    while page <= 4:
        
        uri_to_search = blackmarket+"/search?page="+str(page)+"&q="+to_search
        response = get(uri_to_search , headers=headers)
        ##? Si response 200:
        html_soup = BeautifulSoup(response.text, 'html.parser')
        results_container = html_soup.find_all("a", class_ = '_1ZlCRqz2JUYpCj9FH8PF7C -RBehapDA-mZPY-4bKLAq')
        
        if results_container != []:
            for product in results_container:
                check_old_price = product.find("span", class_= "_3JZtHpVH _3-l8YfN0CFL6l6M_x8eyKI")
                if check_old_price != None:
                    try:
                        old_price = float(check_old_price.text.strip().replace("€","").replace(",", "."))
                    except ValueError:
                        continue
                    current_price = float(product.find("span", class_="_3OcKBk8D _2SrrvPwuOVjCyULC_FKjin").text.replace("€","").replace(",","."))
                    description = product.find("h2", class_="_2RGsPtNo JmqhBfpGehDVZ-r086xn8").text.strip()
                    href = blackmarket+product["href"]
                    img = product.find("img")["src"]
                    discount = (old_price-current_price)*100/old_price
                    data.append({'description':description ,'price':current_price ,'discount':f"{discount:.2f}%" ,'old_price':old_price ,'img_url':img ,'product_href':href})
        page += 1

    return data
          
    
    
def super_search_to_json(to_search):
    
    list_result = [{"date":f"{datetime.datetime.now()}"}]
    data_pccomp = pccomponentes(to_search)
    data_blackm = blackmarket(to_search)
    list_result.extend(data_blackm)
    list_result.extend(data_pccomp)
        
    with open(f"./search/backup/{to_search}.json", "w", encoding= "utf8") as file:
        json.dump( list_result, file, ensure_ascii = False)

super_search_to_json("raton")