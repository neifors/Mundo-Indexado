from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('''
<!DOCTYPE html>
<html>
<head>
    <title>Mundo Indexado</title>
</head>

<body>
    <h1>BIENVENIDO A NUESTRA WEB DE OFERTAS ELECTRÓNICAS</h1>
    <p>Aquí encontrarás todos los productos electrónicos que se encuentren en oferta.</p>
</body>
</html>
''')