from django.shortcuts import render
from django.conf import settings

# pjt/urls 에서 사용하는 함수
def main(request):
    return render(request, 'about/main.html')

def contact(request):
    context = {
        'NAVER_MAP_API_KEY': settings.NAVER_MAP_API_KEY,
        'menu': '찾아오시는 길'
    }
    return render(request, 'about/contact.html', context)