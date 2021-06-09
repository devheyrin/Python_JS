from django.shortcuts import render

# Create your views here.

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