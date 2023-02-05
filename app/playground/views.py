from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import requests
from rest_framework.views import APIView

class HelloView(APIView):
    @method_decorator(cache_page(3 * 10))
    def get(self, request):
        response = requests.get('http://httpbin.org/delay/5')
        data = response.json()
        return render(request, 'hello.html', {'name': 'mohammad'})


