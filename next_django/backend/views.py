from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def products(request):
    if request.method == 'GET':
        return JsonResponse([{'foo':'bar','id':1}],safe=False)
    if request.method == 'POST':
        pass