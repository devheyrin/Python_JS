import time
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from data.adata import Adata
from data.tempa import Tempa


def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    print(id,pwd);
    return render(request, 'jq04.html')

def registerimpl(request):
    id = request.GET['id'];
    pwd = request.GET['pwd'];
    name = request.GET['name'];
    print(id, pwd, name);
    context = {
        'name' : name
    }
    return render(request, 'jq05.html',context)

def ajs01(request):
    now = time.time();
    return HttpResponse(time.ctime(now));

def ajs01(request):
    now = time.time();
    return HttpResponse(time.ctime(now));

def ajs011(request):
    data = Adata().aj011();
    return HttpResponse(json.dumps(data),content_type='application/json');

def ajs02(request):
    cmd = request.GET['cmd'];
    data = Adata().aj02(cmd);
    return HttpResponse(json.dumps(data),content_type='application/json');

def ajs03(request):
    cmd = request.GET['cmd'];
    data = Adata().aj03(cmd);
    return HttpResponse(json.dumps(data),content_type='application/json');

def ajs04(request):
    year = int(request.GET['year']);
    month = int(request.GET['month']);
    print(type(year),type(month));
    data = Tempa().seoulam(year,month);
    print(data)
    return HttpResponse(json.dumps(data),content_type='application/json');
