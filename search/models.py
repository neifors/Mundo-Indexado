from django.db import models


class Article(models.Model):
    description = models.TextField()
    new_price = models.FloatField()
    old_price = models.FloatField()
    discount = models.FloatField()
    img = models.URLField()
    href = models.URLField()

    def __str__(self):
        return self.description

    def to_Str(self):
        return Article.__str__(self)

    def create(description,new_price,old_price,discount,img,href):
        return Article.objects.create(description=description,new_price=new_price,old_price=old_price,discount=discount,href=href)

    def read():
        aux = Article.objects.all()
        result_to_Str = ''
        for article in aux:
            result_to_Str += article.to_Str() + '<br>'
        return result_to_Str
        
class Web(models.Model):
    name = models.CharField(max_length=100)
    href = models.URLField(max_length=100)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def to_Str(self):
        return Web.__str__(self)

    def create(name, href, articles):
        return Web.objects.create(name=name, href=href, articles=articles)

    def read():
        return Web.objects.all()

class Alert(models.Model):
    email = models.EmailField()
    price_limit = models.FloatField()
    product = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

