# Indexed-World

This is a project based in web scraping as a final project for our studies of Python.

It consist of a web page where the user can search any electronic product and get only all of them with a discount applied as a result.

Our python code is responsible to scrap different spanish electronic webs to get those results.

There are some problems we still haven't found the solution to:
- www.mediamarkt.es is kind of blocking the product image so we show an appologise image instead.
- We couldn't make the pagination works so our results view is showing all the products in the same page.
- We had to avoid the scraping to some web pages (www.amazon.es, www.pccomponentes.es, www.worten.es, ...) as they are detecting the bots and immediatly blocking us.


### PREREQUISITES

- Python (3.8.10 version)
- Django
- BeautifulSoup
- request
- concurrent.futures

#### ANY DOUBT, DON'T HESITATE TO EMAIL US:
* veronicasalguero.95@gmail.com / isargp@gmail.com
