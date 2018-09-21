from django.http import HttpResponse


def index(request):
    return HttpResponse('개인 프로젝트 준비 중')
