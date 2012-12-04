from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template.response import TemplateResponse

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('success!')
    else:
        context={}
    return TemplateResponse(request, 'login.html', context)


