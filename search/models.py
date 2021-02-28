from django.db import models

#ARTICULOS LISTA
class Article(models.Model):
    description = models.TextField()
    new_price = models.FloatField()
    old_price = models.FloatField()
    discount = models.FloatField()
    img = models.ImageField()
    href = models.URLField()

#WEB 
class Web(models.Model):
    name = models.CharField(max_length=100)
    href = models.URLField(max_length=100)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def to_Str(self):
        return Web.__str__(self)

    def create(name:str, href, articles):
        return Web.objects.create(name=name, href=href, articles=articles)

    def read():
        return Web.objects.all()

class Alert(models.Model):
    email = models.EmailField()
    price_limit = models.FloatField()
    product = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

