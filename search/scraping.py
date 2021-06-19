from django.http import HttpResponse
from bs4 import BeautifulSoup
from requests import get
import datetime, json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import pandas as pd 



#! RESPONSE [403] FORBIDDEN (Nos han bloqueado el acceso)
# def pccomponentes(to_search):
    
#     headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
#     headers = ({'User-Agent':'Chrome/41.0.2228.0'})
#     pc_componentes = 'https://www.pccomponentes.com' #pc_componentes+'/buscar/?query='+to_search+"&page="+str(page)+"&or-relevance"
#     page = 1
#     data=[]
#     while page <= 4:
#         uri_to_search = f"https://www.pccomponentes.com/buscar/?query=auriculares&page={page}&or-relevance"   
#         print(uri_to_search)
#         response = get(uri_to_search, headers=headers)
#         print(response)
#         html_soup = BeautifulSoup(response.text, 'html.parser')
#         results_container = html_soup.find_all("a", class_="Wrapper-sc-8udqwp cIlLgX sc-amkrK dmBMsh")
                                                        
#         if results_container != []:
#             for product in results_container:
#                 current_price = product.find("span", class_ = "sc-jfkLlK bQYAGo" ) #precio actual si tiene descuento
#                 if current_price != None:
#                     price = float(current_price.text.replace("€",""))
#                     description = product["data-name"]
#                     old_price = float(product["data-price"]) # precio antiguo si tiene aplicado descuento
#                     img = product.find('img')['src']
#                     href = product["href"]
#                     discount = (old_price-price)*100/old_price
#                     data.append({'description':description ,'price':price ,'discount':f"{discount:.2f}%" ,'old_price':old_price ,'img_url':img ,'product_href':href})
#         else:
#             print("sudo pollas de pccomponentes")
#         page += 1
        
#     return data        

def mediamarkt (to_search):
    #class_ = ProductFlexBox__StyledListItem-nk9z2u-0 kzcilw
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    mediamarkt = 'https://www.mediamarkt.es'
    page = 1
    data=[]

    
    while page <= 4:
        uri_to_search = mediamarkt+"/es/search.html?query="+to_search+"&page="+str(page)
        response = get(uri_to_search , headers=headers)
        ##? Si response 200:
        html_soup = BeautifulSoup(response.text, 'html.parser')
        results_container = html_soup.find_all("div", class_ = 'ProductFlexBox__StyledListItem-nk9z2u-0 kzcilw')
        
        if results_container != []:
            for product in results_container:
                prices=product.find_all("span", class_="ScreenreaderText__ScreenreaderTextSpan-sc-11hj9ix-0 bSZZfe")
                if len(prices) == 2:
                    try:
                        old_price = float(prices[0].text)
                        current_price = float(prices[1].text)
                        description = product.find("p", class_="Typostyled__StyledInfoTypo-sc-1jga2g7-0 fuXjPV").text
                        href = mediamarkt+product.find("a", class_="Linkstyled__StyledLinkRouter-sc-1drhx1h-2 iDDAGF ProductListItemstyled__StyledLink-sc-16qx04k-0 dYJAjV")["href"]
                        discount = (old_price-current_price)*100/old_price
                        data.append({'description':description ,'price':current_price ,'discount':f"{discount:.2f}%" ,'old_price':old_price,'product_href':href})
                    except AttributeError:
                        print("No se puede extraer .text de un NoneType")
                        continue
        page += 1
        
    return data
        
def backmarket(to_search):
    
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    backmarket = 'https://www.backmarket.es'
    page = 1
    data=[]
    while page <= 4:
        
        uri_to_search = backmarket+"/search?page="+str(page)+"&q="+to_search
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
                    description = product.find("h2", class_="_2RGsPtNo").text.strip()
                    href = backmarket+product["href"]
                    # img = product.find("img")["src"]
                    discount = (old_price-current_price)*100/old_price
                    data.append({'description':description ,'price':current_price ,'discount':f"{discount:.2f}%" ,'old_price':old_price,'product_href':href})
                    
                    
        page += 1

    return data
          
          
def dell(to_search):
    
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    dell = 'https://www.dell.com'
    page = 1
    data=[]
    while page <= 4:
        
        uri_to_search = dell+"/es-es/search/"+to_search+"?p="+str(page)+"&t=Product"
        response = get(uri_to_search , headers=headers)
        ##? Si response 200:
        html_soup = BeautifulSoup(response.text, 'html.parser')
        results_container = html_soup.find_all("article", class_ = 'stack-accessories ps-stack')
    
        if results_container != []:
            for product in results_container:
                check_price = product.find("div", class_="ps-orig ps-simplified" )
                if check_price:
                    old_price = float(check_price.find("span", class_="strike-through").text.replace(".","").replace(",",".").replace("€",""))
                    current_price = float(product.find("div", class_="ps-dell-price ps-simplified").find_all("span")[1].text.replace(".","").replace(",",".").replace("€",""))
                    description = product.find("h3", class_="ps-title").text.strip()
                    href = product.find("h3", class_="ps-title").find("a")["href"][2:]
                    discount = (old_price-current_price)*100/old_price
                    data.append({'description':description ,'price':current_price ,'discount':f"{discount:.2f}%" ,'old_price':old_price,'product_href':href})
                else:
                    continue
        page += 1

    return data
    
    
def tien21(to_search):
    pass
    
    
def super_search(to_search):
    
    list_result = [{"date":f"{datetime.datetime.now()}"}]

    with ThreadPoolExecutor() as executor:
        data_dell = executor.submit(dell, to_search=to_search)
        data_mediamarkt = executor.submit(mediamarkt, to_search=to_search)
        data_backm = executor.submit(backmarket, to_search=to_search)
        
    #with open(f"./search/backup/{to_search}.json", "w", encoding= "utf8") as file:
    #    json.dump( list_result, file, ensure_ascii = False)
    
    list_result.extend(data_dell.result())
    list_result.extend(data_backm.result())
    list_result.extend(data_mediamarkt.result())
    
    return list_result


def sort_by_price_ascending(list_result):
    sorted_list = pd.DataFrame(list_result[1:]).sort_values("price")
    return sorted_list
    
def sort_by_price_descending(list_result):
    sorted_list = pd.DataFrame(list_result[1:]).sort_values("price", ascending= False)
    return sorted_list



