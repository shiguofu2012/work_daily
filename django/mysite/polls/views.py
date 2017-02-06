from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
import requests
# Create your views here.
PATH_INDEX = '/var/app/enabled/webfront/'
DOMAIN = 'http://192.168.50.128/'


def get_url(url, method, headers=None, data=None):
    res = None
    print url
    for i in range(3):
        try:
            if method == 'get':
                res = requests.get(
                        url, timeout=10, headers=headers)
            elif method == 'post':
                res = requests.post(
                        url, data=data, timeout=10, headers=headers)
            break
        except Exception as e:
            res = None
            continue
    return res.content


def hello(request):
    params = request.META
    ret = {}
    result = []
    for key in params.keys():
        ret[key] = params.get(key)
    for k, v in ret.items():
        result.append(str(k) + ':' + str(v))
    return HttpResponse(result)


def download(request):
    with open('~/t.txt') as f:
        c = f.read()
    return HttpResponse(c)


@require_POST
def test(request):
    params = request.POST
    print params
    if not params:
        return HttpResponse('parameter error')
    url = params.get("url")
    content = get_url(url, 'get')
    print len(content)
    name = 'cralwer.html'
    f = open(PATH_INDEX + name, 'w')
    f.write(content)
    f.close()
    return HttpResponse(DOMAIN + name)
