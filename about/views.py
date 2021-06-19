from django.shortcuts import render
from django.conf import settings

def contact(request):
    context = {
        'NAVER_MAP_API_KEY': settings.NAVER_MAP_API_KEY,
        'menu': '찾아오시는 길'
    }
    return render(request, 'about/contact.html', context)